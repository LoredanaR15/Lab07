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
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---

        self.dd_biblioteche = ft.Dropdown(
            label="Biblioteca",
            width=300,
            options=[
                ft.DropdownOption("Nessun filtro")
            ],
            value="Nessun filtro",
            on_select=self.on_biblioteca_change
        )

        self.dd_generi = ft.Dropdown(
            label="Genere",
            width=300,
            options=[
                ft.DropdownOption("Nessun filtro")
            ],
            value="Nessun filtro",
            on_select=self.on_genere_change
        )


        # Sezione 3: Libri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.on_mostra_libri
        )

        self.lv_libri = ft.ListView(
            expand=False,
            spacing=10,
            height=400
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
                controls=[
                    self.dd_biblioteche,
                    self.dd_generi
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            # Sezione 3: Libri
            self.btn_mostra_libri,
            self.lv_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

     # --- CALLBACKS DROPDOWN ---
    def on_biblioteca_change(self, e):
        self.controller.on_biblioteca_change(e)

    def on_genere_change(self, e):
        self.controller.on_genere_change(e)

    # --- AZIONE: MOSTRA LIBRI ---
    def on_mostra_libri(self, e):
        self.controller.mostra_libri(e)

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
