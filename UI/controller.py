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
        self.biblioteca_selezionata = None    #Come impostazione predefinita, se non tocco niente ho
        self.genere_selezionato = None        #Nessuna selezione di entrambi

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view._ddbiblioteche.options.append(ft.dropdown.Option("Nessun filtro"))
        #Aggiungo tra le opzioni del dropdwon di nome "ddbiblioteche" l'opzione "Nessun filtro"
        for b in self._model.get_biblioteche(): #Per ogni biblioteca che mi ha dato il model
            self._view._ddbiblioteche.options.append(ft.dropdown.Option(b.nome))
            #Aggiungo questa biblioteca alle opzioni del dropdwon di nome "ddbiblioteche"

        self._view._ddgeneri.options.append(ft.dropdown.Option("Nessun filtro")) #dropdwon di nome "ddgeneri"
        for g in self._model.get_generi(): #Per ogni genere che mi ha dato il model
            self._view._ddgeneri.options.append(ft.dropdown.Option(g))


    # CALLBACKS DROPDOWN
    def scegli_biblioteca(self,e): #è il bottone "e" è la scelta dell'utente su opzione dd
        # “quando l’utente sceglie una voce, esegui questa funzione”.
        valore = e.control.value #value è il valore che l'utente ha scelto nell'evento "e"
        self.biblioteca_selezionata = None if valore == "Nessun filtro" else valore
        #Uguale a versione su più righe se valore nessun filtro scelta rimane None
        #print(self.biblioteca_selezionata)

    #Per scegliere genere analogo a scegliere biblioteca
    def scegli_genere(self,e):
        valore = e.control.value
        self.genere_selezionato = None if valore == "Nessun filtro" else valore
        #print(self.genere_selezionato)



    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self._view.lista_libri.controls.clear() #lista_libri è la listview che a ogni clic devo svuotare
                                                #per togliere risultato precedente e non sovrapporli
        #libri validi chiesti al model,che usa metodo libri_filtrati, dipende dai parametri che abbiamo
        #estratto dalle funzioni precedenti, genere e biblioteca
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if len(libri) == 0:   #Se abbiami trovato 0 libri
            self._view.show_alert("Nessun libro trovato")  #Stampo errore per non lasciare vuoto
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))  #Sennò aggiungo alla listview ogni
                                                                             #singolo libro(ricorda .controls)

        self._view.update()

