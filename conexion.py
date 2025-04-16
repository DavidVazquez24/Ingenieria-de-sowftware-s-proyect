import psycopg2

def conexion():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="Cuisinecore",
            user="postgres",
            password="2004",
            port="5432"
        )
        cursor = conn.cursor()
        return conn, cursor  
    except psycopg2.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None, None

def cerrar(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Conexión cerrada correctamente")
