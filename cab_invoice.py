class CabInvoice:
    def __init__(self):
        self.cost_per_km = 10
        self.cost_per_time = 1

    def calculate_fare(self, distance, time):
        MINIMUM_FARE = 5
        totalFare = distance * self.cost_per_km + time * self.cost_per_time
        if totalFare < MINIMUM_FARE:
            return MINIMUM_FARE
        return totalFare


if __name__ == '__main__':
    cab = CabInvoice()
    cab.calculate_fare(2, 5)