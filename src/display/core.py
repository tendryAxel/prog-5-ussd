from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Label, OptionList, Button, Footer, Header

from src.compte import Account


class SubScreen(Screen):
    name: str = "__empty__"
    account: Account
    sub_pages = []
    BINDINGS = [
        ("0", "back", "back"),
    ]

    def main(self):
        yield Static("", id="output")

    def compose(self) -> ComposeResult:
        self.pages = [
            k for k, v in list(
                self.app.SCREENS.items()) if k in self.sub_pages]

        yield Header(show_clock=True)
        yield Label(f"Page: {self.name}")
        yield from self.main()
        if len(self.pages) > 0:
            yield OptionList(*self.pages, id="selector")
        yield Button("Retour", id="go-back")
        yield Footer()

    def on_mount(self) -> None:
        if len(self.pages) > 0:
            self.query_one(OptionList).border_title = "Next page"

    @on(OptionList.OptionSelected)
    def update_selected_view(self) -> None:
        output = self.query_one("#output", Static)
        output.update("Redirected")
        self.app.push_screen(self.pages[self.query_one(
            "#selector", OptionList).highlighted])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back":
            self.app.pop_screen()

    def action_back(self) -> None:
        self.app.pop_screen()
