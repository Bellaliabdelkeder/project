import sqlite3
import hashlib

DATABASE = "snake_game.db"


# Create the database and table
def create_user_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def add_user(username, password):
    # Check if the username already exists
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = c.fetchone()
        if existing_user:
            raise ValueError("Username already exists.")

        # If not, insert the new user with hashed password
        password_hash = hash_password(password)
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
        conn.commit()



def authenticate_user(username, password):
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        if user and user[1] == hash_password(password):
            return True
        return False
