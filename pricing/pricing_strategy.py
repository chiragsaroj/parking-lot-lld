from abc import ABC, abstractmethod
from parking.parking_ticket import ParkingTicket


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fees(self, parking_ticket: ParkingTicket) -> float:
        pass