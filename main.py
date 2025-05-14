from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Select, Label
from textual.containers import Vertical
from textual.screen import Screen
from textual.message import Message
from compte import Account

class MainScreen(Screen):
    BINDINGS = [("q", "quit", "Quitter")]

    def compose(self) -> ComposeResult:
        self.account = Account("032 12 345 67")
        sub_pages = ["recharge"]

        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Select([(k, k) for k, v in list(self.app.SCREENS.items()) if k in sub_pages], prompt="Choice", id="selector")
        yield Button("Submit", id="submit")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        selector = self.query_one("#selector", Select)
        output = self.query_one("#output", Static)
        
        selected_name = selector.value

        try:
            output.update(f"[green]Redirection vers: {selected_name}[/green]")

            if event.button.id == "submit":
                self.app.push_screen(selected_name)

        except Exception as e:
            output.update(f"[red]Erreur : {e}[/red]")


class RechargeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Détails du paquet : requests")
        yield Button("Retour", id="go-back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back":
            self.app.pop_screen()


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
        "recharge": RechargeScreen
    }

    def on_mount(self) -> None:
        self.push_screen("main")


if __name__ == "__main__":
    app = MainApp()
    app.run()

