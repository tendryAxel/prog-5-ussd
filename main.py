from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Select
from textual.containers import Vertical
from textual.screen import Screen
from textual.message import Message

class MainScreen(Screen):
    BINDINGS = [("q", "quit", "Quitter")]

    def compose(self) -> ComposeResult:
        yield Static("Choisis un objet à louer :", id="title")
        yield Input(placeholder="Date de début (AAAA-MM-JJ)", id="start")
        yield Input(placeholder="Date de fin (AAAA-MM-JJ)", id="end")
        yield Button("Louer", id="submit")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        selector = self.query_one("#selector", Select)
        start_input = self.query_one("#start", Input)
        end_input = self.query_one("#end", Input)
        output = self.query_one("#output", Static)
        
        selected_name = selected.name

        try:
            start_date = date.fromisoformat(start_input.value.strip())
            end_date = date.fromisoformat(end_input.value.strip())
            loc.louer(DateRange(start_date, end_date))
            output.update(f"[green]{selected_name} réservé ! Dates:\n{'locations'}[/green]")
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

