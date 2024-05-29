from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_payment_method(self) -> str:
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass
