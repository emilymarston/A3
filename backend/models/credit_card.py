from payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    surcharge: float = 0.02  # 2% surcharge

    def get_payment_method(self) -> str:
        return "Debit Card"

    def process_payment(self, amount: float) -> None:
        # Add logic to process payment by debit card with surcharge
        final_amount = amount * (1 + self.surcharge)
        print(f"Processing debit card payment of {final_amount:.2f}")

    def get_surcharge(self) -> float:
        return self.surcharge
