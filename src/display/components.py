from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.widgets import Static, OptionList
from typing_extensions import override
from textual.widgets.option_list import Option

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
        yield Static(f"Votre solde : {self.account.solde}")


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

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre solde : {self.account.solde}", id="solde")
        yield OptionList(
            *map(MvolaOption.get_option, self.options),
            id="select",
        )

    @on(OptionList.OptionSelected)
    def update_account(self) -> None:
        self.options[self.query_one("#select", OptionList).highlighted].apply(self.account)
        self.query_one("#solde", Static).update(f"Votre solde : {self.account.solde}")
