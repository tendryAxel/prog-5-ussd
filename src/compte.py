import uuid

from textual.widgets._option_list import Option


class Account:
    def __init__(self, numero: str):
        self.numero = numero
        self.solde = 0

class MvolaOption:
    def __init__(self, name: str, price: float, quantity: float):
        self.uuid = str(uuid.uuid4())
        self.option = Option(f"{name} - {quantity}Go {price} Ar", id=self.uuid)
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply(self, account: Account) -> Account:
        account.solde -= self.price
        return account

    @staticmethod
    def get_option(source: 'MvolaOption') -> Option:
        return source.option
