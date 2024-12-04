import psycopg2
from psycopg2 import sql


def insert_data(data):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123456",
        host="0.0.0.0",
        port="5432"
    )
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS company_logo_name_link (
        id SERIAL PRIMARY KEY,
        logo TEXT NOT NULL,
        name TEXT NOT NULL,
        link TEXT NOT NULL
    );
    """

    cur.execute(create_table_query)

    conn.commit()

    insert_query = """
    INSERT INTO company_logo_name_link (logo, name, link)
    VALUES (%s, %s, %s);
    """

    cur.executemany(insert_query, data)

    conn.commit()

    cur.close()
    conn.close()
