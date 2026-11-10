import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self): #Da commentare bene
        self._view._ddbiblioteche.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view._ddbiblioteche.options.append(ft.dropdown.Option(b.nome))

        self._view._ddgeneri.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            self._view._ddgeneri.options.append(ft.dropdown.Option(g))


    # CALLBACKS DROPDOWN
    def scegli_biblioteca(self,e): #Da commentare
        valore = e.control.value
        self.biblioteca_selezionata = None if valore == "Nessun filtro" else valore
        #print(self.biblioteca_selezionata)
    def scegli_genere(self,e): #Da commentare
        valore = e.control.value
        self.genere_selezionato = None if valore == "Nessun filtro" else valore
        #print(self.genere_selezionato)



    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self._view.lista_libri.controls.clear()
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))
        self._view.update()

