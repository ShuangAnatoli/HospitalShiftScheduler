import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('John Doe',))
    conn.commit()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/groups')
def group():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            weight INT DEFAULT 0
        )
    ''')
    cursor.execute('INSERT INTO groups (name, weight) VALUES (?, ?)', ('Everyone', 10))
    conn.commit()
    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()
    conn.close()
    return render_template('index.html', groups=groups)
if __name__ == '__main__':
    app.run(debug=True)