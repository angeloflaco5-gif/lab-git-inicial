import sqlite3
from security import hash_password

DB = "usuarios.db"

def es_hash_bcrypt(valor: str) -> bool:
    return isinstance(valor, str) and valor.startswith(("$2a$", "$2b$", "$2y$"))

def migrar():
    conn = sqlite3.connect(DB)
    try:
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT id, password FROM usuarios")
        filas = cursor.fetchall()
        
        total = len(filas)
        migrados = 0
        saltados = 0
        
        for user_id, pwd in filas:
            if pwd is None or pwd == "":
                saltados += 1
                continue

            if es_hash_bcrypt(pwd):
                saltados += 1
                continue
            
            nuevo_hash = hash_password(pwd)
            
            cursor.execute(
                "UPDATE usuarios SET password = ? WHERE id = ?",
                (nuevo_hash,user_id)
            )
            migrados += 1
            
        conn.commit()
        
        print(f"total filas: {total}")
        print(f"password migradas a bycript: {migrados}")
        print(f"password saltadas: {saltados}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    migrar()