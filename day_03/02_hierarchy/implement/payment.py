class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit):
        """Set attributes here"""
        self.amount = amount
        self.limit = limit

    def total(self):
        """Raise error if amount is beyond limit"""
        try:
            if self.amount > self.limit:
                raise ValueError()
            else:
                # self.amount += self.amount
                return self.amount
        except ValueError:
            print('Exceed limit')


class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""
        self.amount = amount
        self.fee = fee

    def total(self):
        """Return amount + fee"""
        return self.amount + self.fee


class DiscountedPayment:
    def __init__(self, amount, discount):
        """Set attributes here"""
        self.amount = amount
        self.discount = discount

    def total(self):
        """Return amount - discount"""
        return self.amount - self.discount



payments = [
    CashPayment(1_000),
    CreditPayment(2_000, 3000),
    CreditPayment(2_000, 1000)
]



for payment in payments:
    print(payment.total())
