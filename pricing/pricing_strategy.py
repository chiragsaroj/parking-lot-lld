from abc import ABC, abstractmethod
from ticket.ticket import Ticket


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, ticket: Ticket) -> float:
        pass