from parking.parking_lot import ParkingLot
from vehicle.vehicle import Vehicle
from ticket.ticket import Ticket

class EntryGate:
    parking_lot = ParkingLot.get_instance()

    def park(self, vehicle: Vehicle) -> Ticket:
        return self.parking_lot.park_vehicle(vehicle)


class ExitGate:
    parking_lot = ParkingLot.get_instance()

    def unpark(self, ticket: Ticket) -> float:
        return self.parking_lot.unpark_vehicle(ticket)