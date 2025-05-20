from textual.app import App

from src.compte import Account
from src.display import components
from src.display.core import DefaultScreen
from src.utils import extract_dict

structure = {
    "main": {
        "content": components.MainScreen,
        "recharge": components.RechargeScreen,
        "achat": {
            "content": components.AchatScreen,
            "offre": components.OffreScreen,
        },
        "service": components.ServiceScreen,
        "compte": {
            "content": components.CompteScreen,
            "compte_detail": {
                "content": components.CompteDetailScreen,
            },
        }
    },
    "confirmation": components.InputPinCodeScreen,
}


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

    SCREENS = extract_dict(structure)

    def on_mount(self) -> None:
        self.push_screen("main")


if __name__ == "__main__":
    DefaultScreen.account = Account("032 12 345 67", "0000")
    app = MainApp()
    app.run()
