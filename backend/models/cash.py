from payment_method import PaymentMethod

class Cash(PaymentMethod):
    def get_payment_method(self) -> str:
        return "Cash"

    def process_payment(self, amount: float) -> None:
        # Add logic to process payment by cash
        print(f"Processing cash payment of {amount:.2f}")
