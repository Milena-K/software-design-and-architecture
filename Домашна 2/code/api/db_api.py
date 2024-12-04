import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/companies-10', methods=['GET'])
def get_companies():
    app.logger.debug('Request received for /users')
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM company_logo_name_link LIMIT 10;')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": "Something went wrong"}), 500


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
    app.run(debug=True)
