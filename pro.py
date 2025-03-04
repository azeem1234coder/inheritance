# Parent class Vehicle
class Vehicle:
    def __init__(self, make, model, year, passengers=0):
        self.make = make
        self.model = model
        self.year = year
        self.passengers = passengers
    
    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

# Child class Bus inherited from Vehicle
class Bus(Vehicle):
    def __init__(self, make, model, year, passengers, fare_per_passenger):
        super().__init__(make, model, year, passengers)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self):
        return self.passengers * self.fare_per_passenger

    def bus_info(self):
        return f"{self.vehicle_info()} with {self.passengers} passengers."

# Example Usage
bus = Bus("Mercedes", "Sprinter", 2023, 30, 2.5)  # 30 passengers, fare per passenger is $2.5
print(bus.bus_info())  # Vehicle info and passenger count
print(f"Total Fare: ${bus.calculate_total_fare()}")  # Total fare
