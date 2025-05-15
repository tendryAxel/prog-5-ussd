from textual import events, on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Label, OptionList, Button

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
