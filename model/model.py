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
        id_biblioteca = None
        if biblioteca is not None:
            for b in self._biblioteca_dao.get_biblioteca():
                if b.nome == biblioteca:
                    id_biblioteca = b.id

        risultato = []
        for libro in self._libro_dao.get_libri():
            biblioteca_ok = (biblioteca is None) or (libro.id_biblioteca == id_biblioteca)
            genere_ok = (genere is None) or (libro.genere == genere)
            if biblioteca_ok and genere_ok:
                risultato.append(libro)
        return risultato

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_genere() #self._libro_dao = LibroDAO() ho dato all'inizio
                                #nell'init questo nome alla variabile che si collega al DAO
    #get_genere è il nome del metodo invece dentro il DAO

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteca()
