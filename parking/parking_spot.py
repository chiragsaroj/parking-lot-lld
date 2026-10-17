from vehicle.vehicle_size import VehicleSize
from vehicle.vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None    


    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.spot_size == vehicle.get_vehicle_size():
            return True
        else:
            return False


    def park_vehicle(self, vehicle: Vehicle):
        if self.can_fit_vehicle(vehicle) and not self.is_occupied:
            self.park_vehicle = vehicle
            self.is_occupied = True


    def unpark_vehicle(self):
        self.park_vehicle = None
        self.is_occupied = False


    def is_available(self) -> bool:
        return not self.is_occupied