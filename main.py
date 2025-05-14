from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Select
from textual.containers import Vertical
from textual.screen import Screen
from textual.message import Message
from compte import Account

class MainScreen(Screen):
    BINDINGS = [("q", "quit", "Quitter")]

    def compose(self) -> ComposeResult:
        self.account = Account("032 12 345 67")
        self.sub_pages = {
            "recharge": "recharge",
            "achat": "achat",
            "service": "service",
            "compte": "compte"
        }

        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Select(list(self.sub_pages.items()), prompt="Choice", id="selector")
        yield Button("Louer", id="submit")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        selector = self.query_one("#selector", Select)
        output = self.query_one("#output", Static)
        
        selected_name = selector.value

        try:
            output.update(f"[green]Redirection vers: {selected_name}[/green]")
        except Exception as e:
            output.update(f"[red]Erreur : {e}[/red]")


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

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


if __name__ == "__main__":
    app = MainApp()
    app.run()

