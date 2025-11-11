import sqlite3


conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS Producto (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    quantity TEXT,
    due_date DATETIME
);
''')

conn.commit()

def agregar_producto(nombre,cantidad,vencimiento):
    cur.execute('''INSERT OR IGNORE INTO Producto (name,quantity,due_date) 
            VALUES ( ?,?,? )''', (nombre,cantidad,vencimiento))
    conn.commit()

def mostrar_productos():
    cur.execute('''SELECT * FROM Producto''')
    productos = cur.fetchall()
    return productos