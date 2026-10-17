from pricing.pricing_strategy import PricingStrategy
from vehicle.vehicle import VehicleSize
from typing import Dict


class VehiclePricingStrategy(PricingStrategy):
    RATES: Dict[VehicleSize, float] = {
        VehicleSize.SMALL: 20.0,
        VehicleSize.MEDIUM: 50.0,
        VehicleSize.LARGE: 100.0
    }


    def calculate_price(self, ticket):
        hours = (ticket.get_entry_timestamp() - ticket.get_exit_timestamp()).total_seconds() / 3600
        size = ticket.get_vehicle().get_vehicle_size()
        return max(hours, 1) * self.RATES[size]