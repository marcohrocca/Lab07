from database.DB_connect import DBConnect

class AutoriDAO:
    def __init__(self):
        pass

    def get_autori(self):
        lista_autori = []
        cnx=DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("select distinct autore from libro order by autore")
            for riga in cursor:
                lista_autori.append(riga["autore"])
            cursor.close()
            cnx.close()
        else:
            print("Connection error")
        return lista_autori

if __name__== "__main__":
    autori = AutoriDAO()
    print(autori.get_autori())

