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
    # TODO

    # CALLBACKS DROPDOWN
    def scegli_biblioteca(self,e):
        pass
    def scegli_genere(self,e):
        pass



    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self,e):
        pass
