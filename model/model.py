from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        libri = self._libro_dao.get_all_libri()
        biblioteche = self._biblioteca_dao.get_all_biblioteche()

        if libri is None or biblioteche is None:
            return []

        risultati = []

        for libro in libri:

            # Controllo il filtro per genere
            if genere != "Nessun filtro":
                if libro.genere != genere:
                    continue

            # Controllo il filtro per biblioteca
            if biblioteca != "Nessun filtro":
                trovata = False

                for b in biblioteche:
                    if b.nome == biblioteca and b.id == libro.id_biblioteca:
                        trovata = True
                        break

                if not trovata:
                    continue

            risultati.append(libro)

        return risultati


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        libri = self._libro_dao.get_all_libri()

        if libri is None:
            return []

        generi = []

        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)

        generi.sort()

        return generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_all_biblioteche()
