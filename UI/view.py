import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"  #Titolo della finestra che si apre sarà Lab07
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK #Indica tema scuro come tema iniziale

        # Alert
        self.alert = AlertManager(page) #Crea gestore dell'alert e gli da argomento page

        # Controller
        self.controller = None  #Messo None perchè uno fra controller e view deve esistere prima dell'altro
        self._ddbiblioteche=None #Inizializzo il drop down delle biblioteche
        self._ddgeneri=None #Inizializzo dei genere
    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)  #delega all’AlertManager la visualizzazione
                                          #di un messaggio. # Il controller lo userà per
                                          #segnalare errori o avvisi, ad esempio
                                          #“inserisci un titolo”.

    def set_controller(self, controller):
        self.controller = controller #Collega il controller alla view

    def update(self):
        self.page.update() #aggiorma la pagina

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self._ddbiblioteche=ft.Dropdown(label="Biblioteca",on_select=self.controller.scegli_biblioteca,width=400)
        self._ddgeneri=ft.Dropdown(label="Genere",on_select=self.controller.scegli_genere,width=240)

        # Sezione 3: Libri
        self.pulsante_mostra_libri=ft.Button(content="Mostra libri",on_click=self.controller.mostra_libri) #Bottone con
        #scritto Mostra libri nella sezione 3

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.lista_libri = ft.ListView(spacing=5, height=400)
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # Sono già in add quindi creo riga contentente i due menu a tendina centrati
            ft.Row(spacing=50, #Quando distano i due elementi
                controls=[self._ddbiblioteche, self._ddgeneri] , #che elementi aggiungo
                   alignment=ft.MainAxisAlignment.CENTER), #come li allineo
            ft.Divider(), #Metto divisore

            # Sezione 3: Libri
            self.pulsante_mostra_libri,
            self.lista_libri,
        )

        self.page.scroll = "adaptive"
        self.controller.popola_dropdown() #Da commentare
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()



#View quasi finita manca aumentare dimensione dei dropdown come larghezza
