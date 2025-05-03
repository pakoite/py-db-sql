import sqlite3

conn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

conn.close()

