CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
)
LANGUAGE sql
AS $$
    SELECT DISTINCT
        c.id,
        c.first_name,
        c.email,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.first_name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
$$;

CREATE OR REPLACE FUNCTION get_contacts_page(
    p_limit INTEGER,
    p_offset INTEGER
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_limit <= 0 OR p_offset < 0 THEN
        RAISE EXCEPTION 'Invalid limit or offset';
    END IF;

    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$;
