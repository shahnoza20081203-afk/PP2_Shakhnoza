CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;

    ELSE

        INSERT INTO contacts (first_name, phone)
        VALUES (p_name, p_phone);

    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    IN p_users JSONB,
    INOUT p_invalid JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
    item JSONB;
    v_name TEXT;
    v_phone TEXT;

BEGIN
    p_invalid := '[]'::JSONB;

    FOR item IN
        SELECT value
        FROM jsonb_array_elements(p_users)
    LOOP

        v_name := NULLIF(TRIM(item->>'name'), '');
        v_phone := NULLIF(TRIM(item->>'phone'), '');

        IF v_name IS NULL
           OR v_phone IS NULL
           OR v_phone !~ '^\+?[0-9]{10,15}$'
        THEN

            p_invalid := p_invalid || jsonb_build_array(item);

        ELSE

            IF EXISTS (
                SELECT 1
                FROM contacts
                WHERE first_name = v_name
            ) THEN

                UPDATE contacts
                SET phone = v_phone
                WHERE first_name = v_name;

            ELSE

                INSERT INTO contacts (first_name, phone)
                VALUES (v_name, v_phone);

            END IF;

        END IF;

    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(
    p_name VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN

    IF (p_name IS NULL) = (p_phone IS NULL) THEN
        RAISE EXCEPTION 'Provide exactly one: name or phone';

    ELSIF p_name IS NOT NULL THEN

        DELETE FROM contacts
        WHERE first_name = p_name;

    ELSE

        DELETE FROM contacts
        WHERE phone = p_phone;

    END IF;

END;
$$;
