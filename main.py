from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Select, Label, OptionList
from textual.screen import Screen
from compte import Account

class MainScreen(Screen):
    BINDINGS = [("q", "quit", "Quitter")]

    def compose(self) -> ComposeResult:
        self.account = Account("032 12 345 67")
        sub_pages = ["recharge", "achat", "service", "compte"]
        self.pages = [k for k, v in list(self.app.SCREENS.items()) if k in sub_pages]

        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield OptionList(*self.pages, id="selector")
        yield Button("Submit", id="submit")
        yield Static("", id="output")

    def on_mount(self) -> None:
        self.query_one(OptionList).border_title = "Next page"

    @on(OptionList.OptionSelected)
    def update_selected_view(self) -> None:
        self.push_screen(self.pages[self.query_one("#selector", OptionList).highlighted])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        selected_name = self.query_one("#selector", Select).value
        output = self.query_one("#output", Static)

        try:
            output.update(f"[green]Redirection vers: {selected_name}[/green]")

            if event.button.id == "submit":
                self.push_screen(selected_name)

        except Exception as e:
            output.update(f"[red]Erreur : {e}[/red]")

    def push_screen(self, selected_name: str) -> None:
        self.app.push_screen(selected_name)


class SubScreen(Screen):
    name: str

    def compose(self) -> ComposeResult:
        yield Label(f"{self.name} du page")
        yield Button("Retour", id="go-back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back":
            self.app.pop_screen()


class RechargeScreen(SubScreen):
    name = "rechage"

class AchatScreen(SubScreen):
    name = "achat"

class ServiceScreen(SubScreen):
    name = "service"

class CompteScreen(SubScreen):
    name = "compte"


class MainApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #title, #output {
        padding: 1;
    }
    #submit {
        margin-top: 1;
    }
    """

    SCREENS = {
        "main": MainScreen,
        "recharge": RechargeScreen,
        "achat": AchatScreen,
	    "service": ServiceScreen,
	    "compte": CompteScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("main")


if __name__ == "__main__":
    app = MainApp()
    app.run()

