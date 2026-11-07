CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    v_name VARCHAR;
    v_phone VARCHAR;
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        v_name := p_names[i];
        v_phone := p_phones[i];
        
        IF v_phone ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = v_name) THEN
                UPDATE contacts SET phone = v_phone WHERE name = v_name;
            ELSE
                INSERT INTO contacts(name, phone) VALUES(v_name, v_phone);
            END IF;
        ELSE
            RAISE NOTICE 'Некорректный телефон для пользователя %: %', v_name, v_phone;
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_term VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts 
    WHERE name = p_term OR phone = p_term;
END;
$$;