from abc import ABC
from enum import Enum


class VehicleSize(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class Vehicle(ABC):
    def __init__(self, vehicle_number: str, vehicle_size: VehicleSize):
        self.__vehicle_number = vehicle_number
        self.__vehicle_size = vehicle_size


    def get_vehicle_number(self) -> str:
        return self.__vehicle_number


    def get_vehicle_size(self) -> VehicleSize:
        return self.__vehicle_size