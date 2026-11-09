from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteca(self): #Metodo per ottenere i nomi delle biblioteche dal database
        db = DBConnect()        # Cerco di connettermi
        cnx=db.get_connection() # al database
        if cnx is not None:     #Se mi son connesso lo printo nel terminal
            print("Connection established")
            cursor=cnx.cursor(dictionary=True)
            #cursor.execute("select nome from biblioteca")
            # #sarebbe corretto se non avessi classe biblioteca_DTO da popolare,ha bisogno
            # di 3 parametri quindi devo estrarli tutti e 3 potrebbero servirmi in
            # futuro, anche se per questo compito per popolare drop down basta nome
            cursor.execute("SELECT id,nome,indirizzo FROM biblioteca")
            lista_biblioteche=[] #lista dove salvare biblioteche
            for riga in cursor:
                lista_biblioteche.append(Biblioteca(riga["id"], riga["nome"], riga["indirizzo"]))
            cursor.close()
            cnx.close()
            return lista_biblioteche


