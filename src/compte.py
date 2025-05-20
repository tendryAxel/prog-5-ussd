import uuid

from textual.widgets._option_list import Option


class Account:
    def __init__(self, numero: str, pin_code: str):
        self.numero = numero
        self._solde: float = 0
        self.pin_code: str = pin_code

    def get_solde(self):
        return self._solde

    def modify_solde(self, quantity: float) -> bool:
        self._solde += quantity
        return True

    def correct_pin(self, pin_code: str) -> bool:
        return self.pin_code == pin_code


class MvolaOption:
    def __init__(self, name: str, price: float, quantity: float):
        self.uuid = str(uuid.uuid4())
        self.option = Option(f"{name} - {quantity}Go {price} Ar", id=self.uuid)
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply(self, account: Account) -> Account:
        account.modify_solde(-self.price)
        return account

    @staticmethod
    def get_option(source: 'MvolaOption') -> Option:
        return source.option
