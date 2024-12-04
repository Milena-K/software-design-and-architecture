import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mse",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/companies-10', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM company_logo_name_link LIMIT 10;')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
