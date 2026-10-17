from typing import Dict, List
from parking.parking_floor import ParkingFloor
from pricing.pricing_strategy import PricingStrategy
from pricing.hourly_pricing_strategy import HourlyPricingStrategy
from ticket.ticket import Ticket
from vehicle.vehicle import Vehicle, VehicleSize
from datetime import datetime
import threading


class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        self.active_tickets: Dict[str, Ticket] = {}
        self.parking_floors = []
        self.pricing_strategy = HourlyPricingStrategy()
        self._main_lock = threading.Lock()


    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance


    def add_floors(self, parking_floors: List[ParkingFloor]):
        self.parking_floors = parking_floors


    def set_pricing_strategy(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy


    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        with self._main_lock:
            spot = self.__find_available_spot(vehicle.get_vehicle_size())

            if not spot.park_vehicle(vehicle):
                raise Exception("Parking spot was taken concurrently")

            ticket = Ticket(vehicle, spot)
            self.active_tickets[ticket.get_ticket_id()] = ticket
            
            return ticket


    def unpark_vehicle(self, ticket: Ticket):
        with self._main_lock:
            if ticket.get_ticket_id() not in self.active_tickets:
                raise Exception(f"Invalid Ticket: {ticket.get_ticket_id()}")

            ticket.set_exit_timestamp(datetime.now())
            ticket.close_ticket(self.pricing_strategy.calculate_price(ticket))
            ticket.get_parking_spot().remove_vehicle()
            self.active_tickets.pop(ticket.get_ticket_id())

            return ticket.get_charges()


    def __find_available_spot(self, vehicle_size: VehicleSize):
        """Can be extended in parking strategy"""

        for floor in self.parking_floors:
            for spot in floor.get_parking_spots():
                if spot.get_spot_size() == vehicle_size and spot.is_spot_available():
                    return spot

        raise Exception("No spot available!!")