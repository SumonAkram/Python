class Payment:
    def __init__(self, amount: float = 0.0) -> None:
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount


class Cash(Payment):
    def __init__(self, amount: float = 0.0, cash_trans_id: float = 0.0) -> None:
        super().__init__(amount)
        self.cash_trans_id = cash_trans_id

    def get_cash_trans_id(self) -> float:
        return self.cash_trans_id


class Cheque(Payment):
    def __init__(self, amount: float = 0.0, name: str = "Q", bank_id: str = "R") -> None:
        super().__init__(amount)
        self.name = name
        self.bank_id = bank_id

    def authorization(self) -> None:
        # Perform authorization logic for cheque payment
        pass


class Creditcard(Payment):
    def __init__(self, amount: float = 0.0, card_number: str = "S", card_type: str = "T", exp_date: str = "17.05.2023") -> None:
        super().__init__(amount)
        self.card_number = card_number
        self.card_type = card_type
        self.exp_date = exp_date

    def authorization(self) -> None:
        # Perform authorization logic for credit card payment
        pass


# Example usage
cash_payment = Cash(100.0, 123456)
cheque_payment = Cheque(200.0, "John Doe", "Bank XYZ")
cheque_payment.authorization()
credit_card_payment = Creditcard(300.0, "1234567890", "Visa", "17.05.2023")
credit_card_payment.authorization()

print("Cash Payment Amount:", cash_payment.get_amount())  # Output: Cash Payment Amount: 100.0
print("Cheque Payment Amount:", cheque_payment.get_amount())  # Output: Cheque Payment Amount: 200.0
print("Credit Card Payment Amount:", credit_card_payment.get_amount())  # Output: Credit Card Payment Amount: 300.0
print("Cheque Payment Name:", cheque_payment.name)  # Output: Cheque Payment Name: John Doe
print("Credit Card Payment Type:", credit_card_payment.card_type)  # Output: Credit Card Payment Type: Visa
