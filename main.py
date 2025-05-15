from textual.app import App

from compte import Account
from display.core import SubScreen
from display import components


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
        "main": components.MainScreen,
        "recharge": components.RechargeScreen,
        "achat": components.AchatScreen,
	    "service": components.ServiceScreen,
	    "compte": components.CompteScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("main")

if __name__ == "__main__":
    SubScreen.account = Account("032 12 345 67")
    app = MainApp()
    app.run()

