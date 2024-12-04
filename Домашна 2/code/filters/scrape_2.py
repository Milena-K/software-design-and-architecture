import psycopg2

def insert_data(data):
    # Establish a connection to the database
    conn = psycopg2.connect(
        dbname="mse",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    # SQL query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS company_logo_name_link (
        id SERIAL PRIMARY KEY,
        logo TEXT NOT NULL,
        name TEXT NOT NULL,
        link TEXT NOT NULL
    );
    """

    # Execute the query to create the table
    cur.execute(create_table_query)

    # Commit the transaction
    conn.commit()

    # SQL query to insert data
    insert_query = """
    INSERT INTO company_logo_name_link (logo, name, link)
    VALUES (%s, %s, %s);
    """

    # Execute the query with the data
    cur.executemany(insert_query, data)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()
