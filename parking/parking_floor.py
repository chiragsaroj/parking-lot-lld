from typing import Dict
from parking.parking_spot import ParkingSpot


class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.parking_spots: Dict[str, ParkingSpot] = {}