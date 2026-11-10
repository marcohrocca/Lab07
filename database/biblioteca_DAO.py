from database.DB_connect import DBConnect    #Serve per parlare col Database
from model.biblioteca_DTO import Biblioteca  #Serve per creare l'oggetto biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteca(self): #Metodo per ottenere i nomi delle biblioteche dal database
        cnx = DBConnect.get_connection()        # Cerco di connettermi al database
        lista_biblioteche = []  # lista dove salvare biblioteche
        if cnx is not None:     #Indica se sono connesso faccio...
            print("Connection established")   #Se mi son connesso lo printo nel terminal
            cursor=cnx.cursor(dictionary=True) #Apro cursore di tipo dizionario, più comodo da usare
            #cursor.execute("select nome from biblioteca")
            # #sarebbe corretto se non avessi classe biblioteca_DTO da popolare, ha bisogno
            # di 3 parametri quindi devo estrarli tutti e 3 potrebbero servirmi in
            # futuro, anche se per questo compito per popolare drop down basta nome
            cursor.execute("SELECT id,nome,indirizzo FROM biblioteca") #Dentro inserisco la query,la domanda per mysql
            for riga in cursor:
                lista_biblioteche.append(Biblioteca(riga["id"], riga["nome"], riga["indirizzo"]))
                #Nella lista metto oggetto DTO
                #Aggiungo ala lista_biblioteche tanti oggetti Biblioteca
            cursor.close()
            cnx.close()
        return lista_biblioteche


#Test per vedere se tutto funziona, print di debug
if __name__ == "__main__":   #Ricorda __ prima di main sennò da errore
    dao = BibliotecaDAO()
    print(dao.get_biblioteca())


