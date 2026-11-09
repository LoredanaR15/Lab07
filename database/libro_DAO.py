from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass


    def get_all_libri(self) -> list[Libro] | None:
        conn = DBConnect.get_connection()

        if conn is None:
            return None

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM libro"
        cursor.execute(query)

        for row in cursor:
            libro = Libro(
                row["id"],
                row["titolo"],
                row["autore"],
                row["genere"],
                row["anno_pubblicazione"],
                row["id_biblioteca"]
            )
            results.append(libro)

        cursor.close()
        conn.close()

        return results

