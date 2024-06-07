class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @currency.setter
    def currency(self, value):
        self.__amount = value

    def __add__(self, other):
        if isinstance(other, Money) and self.__currency == other.__currency:
            return Money(self.amount + other.amount, self.currency)
        raise RuntimeError("Mismatched currencies!")

    def __sub__(self, other):
        if isinstance(other, Money) and self.__currency == other.__currency:
            return Money(self.amount - other.amount, self.currency)
        raise RuntimeError("Mismatched currencies!")

    def __mul__(self, other):
        return Money(self.__amount * other, self.__currency)
