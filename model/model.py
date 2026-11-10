from database.biblioteca_DAO import BibliotecaDAO #Gli import portano le due classi DAO,
from database.libro_DAO import LibroDAO           # perché il Model le deve usare.

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
        #In questa parte cerchiamo id biblioteca, del nome biblioteca che ci ha dato il dropdown
        id_biblioteca = None
        if biblioteca is not None: #Se utente ha selezionato qualcosa allora procedo
            for b in self._biblioteca_dao.get_biblioteca():
                if b.nome == biblioteca:   #Se il nome di una b del dao è uguale a Biblioteca data
                    id_biblioteca = b.id   #salvo il suo id

        risultato = []
        for libro in self._libro_dao.get_libri():
            biblioteca_ok = (biblioteca is None) or (libro.id_biblioteca == id_biblioteca) #biblioteca_ok è True
            # in due casi: il filtro è spento (biblioteca is None), oppure il libro appartiene alla biblioteca scelta.
            genere_ok = (genere is None) or (libro.genere == genere) #Stessa cosa vale per il genere
            if biblioteca_ok and genere_ok: #Se vanno bene sia genere che biblioteca
                risultato.append(libro)     #Allora aggiungo oggetto libro con tutte info a risultato libri validi
        return risultato #Return del risultato

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_genere() #self._libro_dao = LibroDAO() ho dato all'inizio
                                #nell'init questo nome alla variabile che si collega al DAO
                                 #get_genere è il nome del metodo invece dentro il DAO

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteca()
        #Interroga il dao che usa metodo get_biblioteca,successivamente restituisce la lista per
        #controller, Non fanno niente di loro, Esistono perché il controller non deve parlare coi DAO
        #Commento che vale anche per get_generi
