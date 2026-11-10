from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_genere(self):
        lista_generi=[] #Creo lista con generi a prescindere prima della connessione,
                        #così al massimo ho lista vuota
        cnx=DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("select DISTINCT genere FROM libro ORDER BY genere ")
            for riga in cursor:
                lista_generi.append(riga["genere"])
            cursor.close()
            cnx.close()
        return lista_generi


    def get_libri(self):
        lista_libri = []
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca FROM libro")
            for riga in cursor:
                lista_libri.append(Libro(riga["id"],
                                         riga["titolo"],
                                         riga["autore"],
                                         riga["genere"],
                                         riga["anno_pubblicazione"],
                                         riga["id_biblioteca"]))
            cursor.close()
            cnx.close()
        return lista_libri

if __name__ == "__main__":
    libro = LibroDAO()
    print(libro.get_genere())
