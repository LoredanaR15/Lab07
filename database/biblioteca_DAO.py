from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass


    def get_all_biblioteche(self) -> list[Biblioteca] | None:
        conn = DBConnect.get_connection()

        if conn is None:
            return None

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)

        for row in cursor:
            biblioteca = Biblioteca(
                row["id"],
                row["nome"],
                row["indirizzo"]
            )
            results.append(biblioteca)

        cursor.close()
        conn.close()

        return results

