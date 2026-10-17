from datetime import datetime
from uuid import uuid4
from vehicle.vehicle import Vehicle
from parking.parking_spot import ParkingSpot


class Ticket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self.ticket_id = str(uuid4())
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_timestamp = datetime.now()
        self.exit_timestamp = None
        self.charges = 0.0


    def close_ticket(self, charges: float):
        self.charges = charges


    def set_exit_timestamp(self, exit_time: datetime):
        self.exit_timestamp = exit_time


    def get_entry_timestamp(self):
        return self.entry_timestamp


    def get_exit_timestamp(self):
        return self.exit_timestamp


    def get_ticket_id(self):
        return self.ticket_id


    def get_vehicle(self):
        return self.vehicle


    def get_parking_spot(self):
        return self.parking_spot


    def get_charges(self):
        return self.charges