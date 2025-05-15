from textual.app import ComposeResult
from textual.widgets import Static
from typing_extensions import override

from src.display.core import SubScreen


class MainScreen(SubScreen):
    BINDINGS = [("q", "quit", "Quitter")]
    sub_pages = ["recharge", "achat", "service", "compte"]

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
    sub_pages = ["compte_detail"]

class CompteDetailScreen(SubScreen):
    name = "compte detail"

    @override
    def main(self) -> ComposeResult:
        yield Static(f"Votre Numero : {self.account.numero}", id="title")
        yield Static(f"Votre solde : {self.account.solde}", id="output")
