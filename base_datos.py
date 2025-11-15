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

def actualizar_titulo_producto(producto_id,titulo):
    cur.execute('UPDATE Producto SET name = ? WHERE id = ?', (titulo, producto_id))
    conn.commit()

def actualizar_cantidad_producto(producto_id,cantidad):
    cur.execute('UPDATE Producto SET quantity = ? WHERE id = ?', (cantidad, producto_id))
    conn.commit()

def actualizar_fecha_vencimiento_producto(producto_id,vencimiento):
    cur.execute('UPDATE Producto SET due_date = ? WHERE id = ?', (vencimiento, producto_id))
    conn.commit()

def eliminar_producto(producto_id):
    cur.execute('DELETE FROM Producto WHERE id = ?', (producto_id))
    conn.commit()

def avisar_productos_por_vencer():
    cur.execute("""
        SELECT id, name, due_date
        FROM Producto
        WHERE
            julianday(
                substr(due_date, 7, 4) || '-' ||
                substr(due_date, 4, 2) || '-' ||
                substr(due_date, 1, 2)
            )
            - julianday('now') BETWEEN -7 AND 7
    """)
    # cur.execute("SELECT id, name, due_date FROM Producto LIMIT 5")

    productos = cur.fetchall()

    if not productos:
        print("No hay productos por vencer en los próximos 7 días.")
        return

    for prod_id, name, due_date in productos:
        print(f"⚠ El producto '{name}' (ID {prod_id}) se vence el {due_date}.")
