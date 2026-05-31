class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        return total_fare + (total_fare * 10 / 100)


# Create a Bus object with seating capacity 50
school_bus = Bus(50)

# Display the total fare
print("Total Bus Fare:", school_bus.fare())