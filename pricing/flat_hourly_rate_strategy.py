from pricing.pricing_strategy import PricingStrategy


class FlatHourlyRateStrategy(PricingStrategy):
    RATE_PER_HOUR = 20.0

    def calculate_fees(self, parking_ticket):
        return super().calculate_fees(parking_ticket)