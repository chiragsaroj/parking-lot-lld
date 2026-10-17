from pricing.pricing_strategy import PricingStrategy


class HourlyPricingStrategy(PricingStrategy):
    RATE_PER_HOUR = 20.0

    def calculate_price(self, ticket):
        hours = (ticket.get_entry_timestamp() - ticket.get_exit_timestamp()).total_seconds() / 3600
        return max(hours, 1) * self.RATE_PER_HOUR