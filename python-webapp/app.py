from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",          # or your MySQL host
        user="your_user",          # your MySQL username
        password="your_password",  # your MySQL password
        database="demo"            # your MySQL database
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee', methods=['POST'])
def employee():
    search_input = request.form['search_input']
    
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Try searching by employee ID
    query = "SELECT * FROM employees WHERE employee_id = %s OR CONCAT(first_name, ' ', last_name) = %s"
    cursor.execute(query, (search_input, search_input))
    employee = cursor.fetchone()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    if employee:
        return render_template('employee.html', employee=employee)
    else:
        return render_template('index.html', message="Employee not found!")

if __name__ == '__main__':
    app.run(debug=True)
