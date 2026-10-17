from pricing.pricing_strategy import PricingStrategy
from vehicle.vehicle_size import VehicleSize


class VehicleBasedRateStrategy(PricingStrategy):
    RATES = {
        VehicleSize.SMALL: 20.0,
        VehicleSize.MEDIUM: 50.0,
        VehicleSize.LARGE: 100.0
    }


    def calculate_fees(self, parking_ticket):
        return super().calculate_fees(parking_ticket)