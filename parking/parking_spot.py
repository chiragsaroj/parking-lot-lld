from vehicle.vehicle import Vehicle, VehicleSize
from threading import Lock


class ParkingSpot:
    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.vehicle = None
        self._lock = Lock()


    def park_vehicle(self, vehicle: Vehicle) -> bool:
        with self._lock:
            if self.vehicle is None and self.spot_size == vehicle.get_vehicle_size():
                self.vehicle = vehicle
                return True

            return False


    def remove_vehicle(self):
        with self._lock:
            self.vehicle = None


    def is_spot_available(self) -> bool:
        with self._lock:
            return self.vehicle == None

    
    def get_id(self):
        return self.spot_id


    def get_spot_size(self):
        return self.spot_size


    def get_vehicle(self):
        return self.vehicle