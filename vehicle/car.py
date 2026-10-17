from vehicle.vehicle import Vehicle, VehicleSize


class Car(Vehicle):
    def __init__(self, vehicle_number):
        super().__init__(vehicle_number, VehicleSize.MEDIUM)