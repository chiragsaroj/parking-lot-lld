from typing import List
from parking.parking_spot import ParkingSpot


class ParkingFloor:
    def __init__(self, floor_number: int, parking_spots: List[ParkingSpot]):
        self.floor_number = floor_number
        self.parking_spots = parking_spots


    def get_parking_spots(self):
        return self.parking_spots.copy()


    def get_floor_number(self):
        return self.floor_number