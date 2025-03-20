import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear tabla (si no existe)
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, email TEXT)""")
conn.commit()

# Funciones CRUD
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user(id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
