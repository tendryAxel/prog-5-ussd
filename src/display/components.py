from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.widgets import Static, OptionList, Input
from typing_extensions import override

from src.compte import MvolaOption
from src.display.core import SubScreen, DefaultScreen


class MainScreen(DefaultScreen):
    BINDINGS = [("q", "quit", "Quitter")]
    sub_pages = ["recharge", "achat", "service", "compte"]

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre Numero : {self.account.numero}", id="title")


class RechargeScreen(SubScreen):
    name = "rechage"


class AchatScreen(SubScreen):
    name = "achat"
    sub_pages = ["offre"]


class ServiceScreen(SubScreen):
    name = "service"


class CompteScreen(SubScreen):
    name = "compte"
    sub_pages = ["compte_detail"]


class CompteDetailScreen(SubScreen):
    name = "compte detail"

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Static(f"Votre solde : {self.account.get_solde()}")


class OffreScreen(SubScreen):
    name = "offre"
    BINDINGS = [
        Binding("enter", "select", "Select", show=True),
    ]
    options = [
        MvolaOption("MORA 1000", 1000, 1),
        MvolaOption("MORA 2000", 2000, 4),
        MvolaOption("MORA 4000", 4000, 10),
    ]
    current_option: MvolaOption = None

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre solde : {self.account.get_solde()}", id="solde")
        yield OptionList(
            *map(MvolaOption.get_option, self.options),
            id="select",
        )

    @on(OptionList.OptionSelected)
    def update_account(self) -> None:
        self.app.push_screen(InputPinCodeScreen(self.options[self.query_one("#select", OptionList).highlighted]))


class InputPinCodeScreen(SubScreen):
    name = "input pin code"
    error_text_id = "output_correct_pin"

    def __init__(self, option: MvolaOption):
        super().__init__()
        self.option = option

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Input(placeholder="Ton code pin")
        yield Static("", id=self.error_text_id)

    def on_mount(self) -> None:
        self.query_one(f"#{self.error_text_id}", Static).styles.color = "red"

    @on(Input.Submitted)
    def confirm(self, event: Input.Submitted) -> None:
        if self.account.correct_pin(event.value):
            self.app.pop_screen()
            self._apply_option_to_account()
        else:
            self.query_one(
                f"#{self.error_text_id}",
                Static).update("Incorrect pin code")

    def _apply_option_to_account(self):
        self.option.apply(self.account)
