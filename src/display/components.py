from textual.app import ComposeResult
from textual.widgets import Static, OptionList
from typing_extensions import override
from textual.widgets.option_list import Option

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

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre solde : {self.account.solde}")
        yield OptionList(
            Option("MORA 1000 - 1Go + Appels, 1000 Ar"),
            Option("MORA 2000 - 2Go + Appels, 2000 Ar"),
            Option("MORA NIGHT - Internet illimité 22h-5h, 500 Ar"),
            Option("TELMA NET 500 - 500Mo, 1000 Ar"),
            Option("TELMA COMBO 3000 - 3Go + voix, 3000 Ar")
        )
