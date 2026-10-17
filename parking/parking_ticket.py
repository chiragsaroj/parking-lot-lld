from vehicle.vehicle import Vehicle
from parking_spot import ParkingSpot
from uuid import uuid4
from datetime import datetime


class ParkingTicket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self.ticket_id = str(uuid4())
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_timestamp = datetime.now()
        self.exit_timestamp = None
    

    def set_exit_timestamp(self):
        self.exit_timestamp = datetime.now()