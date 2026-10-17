from parking.parking_spot import ParkingSpot
from parking.parking_floor import ParkingFloor
from vehicle.vehicle import VehicleSize
from parking.parking_lot import ParkingLot
from vehicle.bike import Bike
from vehicle.car import Car
from vehicle.truck import Truck
from pricing.vehicle_pricing_strategy import VehiclePricingStrategy
from gate.gate import EntryGate, ExitGate


def main():
    ground_floor_spots = [
        ParkingSpot("G1", VehicleSize.SMALL), 
        ParkingSpot("G2", VehicleSize.MEDIUM),
        ParkingSpot("G3", VehicleSize.MEDIUM)
    ]
    ground_floor = ParkingFloor(0, ground_floor_spots)

    first_floor = ParkingFloor(1, [ParkingSpot("F1", VehicleSize.LARGE)])

    service = ParkingLot.get_instance()
    service.set_pricing_strategy(VehiclePricingStrategy())
    service.add_floors([ground_floor, first_floor])

    bike = Bike("123")
    car = Car("456")

    entry = EntryGate()
    exit = ExitGate()

    bike_ticket = entry.park(bike)
    print(bike_ticket.get_parking_spot().get_id())

    car_ticket = entry.park(car)
    print(car_ticket.get_parking_spot().get_id())

    print(exit.unpark(bike_ticket))
    print(exit.unpark(car_ticket))




if __name__ == "__main__":
    main()
