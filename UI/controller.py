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
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        self._view.dd_biblioteche.options = [
            ft.DropdownOption("Nessun filtro")
        ]

        self._view.dd_generi.options = [
            ft.DropdownOption("Nessun filtro")
        ]

        if biblioteche is not None:
            for biblioteca in biblioteche:
                self._view.dd_biblioteche.options.append(
                    ft.DropdownOption(biblioteca.nome)
                )

        if generi is not None:
            for genere in generi:
                self._view.dd_generi.options.append(
                    ft.DropdownOption(genere)
                )

        self._view.dd_biblioteche.value = "Nessun filtro"
        self._view.dd_generi.value = "Nessun filtro"

        self.biblioteca_selezionata = "Nessun filtro"
        self.genere_selezionato = "Nessun filtro"

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_biblioteca_change(self, e):
        self.biblioteca_selezionata = e.control.value

    def on_genere_change(self, e):
        self.genere_selezionato = e.control.value


    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self._view.lv_libri.controls.clear()

        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        if not libri:
            self._view.show_alert("Nessun libro trovato.")
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(
                ft.Text(str(libro))
            )

        self._view.update()

