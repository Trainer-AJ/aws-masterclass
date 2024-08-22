'''

AUTHOR: AJ
Purpose: It creates a Random Digit and Stores it in MySQL Database
Pre-Requisite: a MySQL Database 

'''


from flask import Flask, render_template_string
import mysql.connector
from random import choice
import string
import json

app = Flask(__name__)

###################################################
# MySQL connection parameters
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'testdb'
}
###################################################

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_table_if_not_exists():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            value VARCHAR(255) NOT NULL
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

def insert_random_entry():
    create_table_if_not_exists()  # Ensure the table exists before inserting
    connection = get_db_connection()
    cursor = connection.cursor()
    random_string = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))
    cursor.execute("INSERT INTO entries (value) VALUES (%s)", (random_string,))
    connection.commit()
    cursor.execute("SELECT * FROM entries ORDER BY id DESC LIMIT 1")
    entry = cursor.fetchone()
    cursor.close()
    connection.close()
    return entry

@app.route('/')
def index():
    entry = insert_random_entry()
    return render_template_string('''
        <html>
        <head>
            <title>Random Entry Generator</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(to right, #74ebd5, #9face6);
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 500px;
                    width: 100%;
                }
                h1 {
                    color: #333;
                    font-size: 28px;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 16px;
                    color: #666;
                    margin-bottom: 30px;
                }
                .description {
                    background-color: #f8f9fa;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 30px;
                    color: #555;
                    font-size: 18px;
                    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
                }
                .entry {
                    font-size: 20px;
                    color: #007BFF;
                    margin: 15px 0;
                }
                button {
                    padding: 12px 25px;
                    font-size: 18px;
                    color: white;
                    background-color: #28a745;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                button:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="description">
                    <h1>Python App To Generate Random Entries</h1>
                    <p>This is a simple Python app that generates random entries and stores them in a MySQL database.</p>
                </div>
                <h1>Latest Entry</h1>
                <div class="entry">
                    <p>ID: <span id="entry-id">{{ entry[0] }}</span></p>
                    <p>Value: <span id="entry-value">{{ entry[1] }}</span></p>
                </div>
                <button onclick="generateNewEntry()">Generate New Entry</button>
            </div>

            <script>
                function generateNewEntry() {
                    fetch('/new_entry')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('entry-id').textContent = data.id;
                            document.getElementById('entry-value').textContent = data.value;
                        });
                }
            </script>
        </body>
        </html>
    ''', entry=entry)

@app.route('/new_entry')
def new_entry():
    entry = insert_random_entry()
    return json.dumps({'id': entry[0], 'value': entry[1]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
