from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)


db_config = {
    'host': 'localhost',
    'user': 'root',           # ← cambia se usi un altro utente
    'database': 'piattaforma_studenti'
}

@app.route('/registrati', methods=['POST'])
def registra_studente():
    data = request.get_json()
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO studenti (nome, cognome, data_nascita, email, corso)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data['nome'],
            data['cognome'],
            data['dataNascita'],
            data['email'],
            data['corso']
        ))

        conn.commit()
        return jsonify({'message': 'Studente registrato con successo'}), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/studenti', methods=['GET'])
def get_studenti():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT nome, cognome, data_nascita, email, corso FROM studenti")
        studenti = cursor.fetchall()

        return jsonify(studenti)

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
    # Lancia il server Flask