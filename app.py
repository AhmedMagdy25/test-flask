from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connect():
    conn = sqlite3.connect("flask.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = db_connect()
conn.execute( 
    'CREATE TABLE IF NOT EXISTS users (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name TEXT NOT Null UNIQUE,\
        password TEXT NOT Null\
    )') 
conn.close()

@app.route("/api/users", methods=['GET'])
def get_users():
    conn = db_connect()
    cursor = conn.cursor()
    users = cursor.execute('SELECT name FROM users').fetchone()
    conn.close()
    return jsonify(dict(users)), 200

@app.route("/api/users/<string:username>", methods=['POST'])
def check_user_exist(username):
    conn = db_connect()
    cursor = conn.cursor()
    user = cursor.execute('SELECT name FROM users where name=?',(username,)).fetchone()
    conn.close()
    if user is None:
        return {'error': 'user not exist'}, 404
    return {'success': f'user {username} is exist'}, 200

@app.route("/register", methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/register", methods=['POST'])
def registrate():
    username = request.form['username']
    password = request.form['password']

    conn = db_connect()
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return render_template("register.html", msg="Username aleady exist")

    cursor.execute("INSERT INTO users (name, password) VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()
    return render_template("register.html", msg="SUCCESS")

if __name__ == '__main__': 
    app.run(debug=False) 