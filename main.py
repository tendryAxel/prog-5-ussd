from textual import on, events
from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Label, OptionList
from textual.screen import Screen
from typing_extensions import override

from compte import Account

class SubScreen(Screen):
    name: str
    account: Account

    def main(self):
        yield Static("", id="output")

    def compose(self) -> ComposeResult:
        sub_pages = ["recharge", "achat", "service", "compte"]
        self.pages = [k for k, v in list(self.app.SCREENS.items()) if k in sub_pages]

        yield Label(f"{self.name} du page")
        yield OptionList(*self.pages, id="selector")
        yield from self.main()
        yield Button("Retour", id="go-back")

    def on_mount(self) -> None:
        self.query_one(OptionList).border_title = "Next page"

    @on(OptionList.OptionSelected)
    def update_selected_view(self) -> None:
        output = self.query_one("#output", Static)
        output.update("Redirected")
        self.app.push_screen(self.pages[self.query_one("#selector", OptionList).highlighted])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back":
            self.app.pop_screen()

    def on_key(self, event: events.Key) -> None:
        if event.key == "0":
            self.app.pop_screen()


class MainScreen(SubScreen):
    BINDINGS = [("q", "quit", "Quitter")]

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Static("", id="output")

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
    SubScreen.account = Account("032 12 345 67")
    app = MainApp()
    app.run()

