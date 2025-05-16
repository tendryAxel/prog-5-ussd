from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Label, OptionList, Button, Footer, Header

from src.compte import Account


class DefaultScreen(Screen):
    name: str = "__empty__"
    account: Account
    sub_pages = []
    BINDINGS = [
        ("0", "back", "back"),
    ]

    def main(self):
        yield Static("", id="top-section")

    def footer(self) -> ComposeResult:
        yield Static("", id="botton-section")

    def compose(self) -> ComposeResult:
        self.pages = [
            k for k, v in list(
                self.app.SCREENS.items()) if k in self.sub_pages]

        yield Header(show_clock=True)
        yield Label(f"Page: {self.name}")
        yield Label("", id="output")
        yield from self.main()
        if len(self.pages) > 0:
            yield OptionList(*self.pages, id="selector")
        yield from self.footer()
        yield Footer()

    def on_mount(self) -> None:
        if len(self.pages) > 0:
            self.query_one(OptionList).border_title = "Next page"

    @on(OptionList.OptionSelected)
    def update_selected_view(self) -> None:
        if len(self.pages) > 0:
            output = self.query_one("#output", Static)
            output.update("Redirected")
            self.app.push_screen(self.pages[self.query_one(
                "#selector", OptionList).highlighted])

    def action_back(self) -> None:
        self.app.pop_screen()

    @staticmethod
    def project_structure_scan(
            project_structure: dict[str, "DefaultScreen"],
            content_key_match: str = "content"
    ) -> None:
        if content_key_match in project_structure.keys():
            project_structure[content_key_match].pages = [
                key
                for key in project_structure.keys()
                if key != content_key_match
            ]
            print(project_structure[content_key_match].name)
            print(project_structure[content_key_match].pages)
            for page in project_structure[content_key_match].pages:
                sub_structure = project_structure[page]
                if isinstance(sub_structure, dict):
                    DefaultScreen.project_structure_scan(sub_structure)


class SubScreen(DefaultScreen):
    def footer(self) -> ComposeResult:
        yield Button("Retour", id="go-back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back":
            self.app.pop_screen()
