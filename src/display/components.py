from textual.app import ComposeResult
from textual.widgets import Static
from typing_extensions import override

from src.display.core import SubScreen


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
