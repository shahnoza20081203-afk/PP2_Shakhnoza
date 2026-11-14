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
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Phone type must be home, work, or mobile';
    END IF;

    SELECT id
    INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type);
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id INTEGER;
BEGIN
    SELECT id
    INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;

    INSERT INTO groups (name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id
    INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;
END;
$$;