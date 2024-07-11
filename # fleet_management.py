# fleet_management.py

class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return super().display_info() + f", Number of Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f", Cargo Capacity: {self.cargo_capacity}"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f", Engine Capacity: {self.engine_capacity}"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.display_info())

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(vehicle.display_info())
                return
        print("Vehicle not found.")

def main():
    fleet = Fleet()

    try:
        while True:
            print("\n1. Add a vehicle")
            print("2. Display all vehicles")
            print("3. Search for a vehicle by registration number")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                reg_num = input("Enter registration number: ")
                make = input("Enter make: ")
                model = input("Enter model: ")
                vehicle_type = input("Enter vehicle type (Car/Truck/Motorcycle): ").lower()

                if vehicle_type == 'car':
                    seats = int(input("Enter number of seats: "))
                    vehicle = Car(reg_num, make, model, seats)
                elif vehicle_type == 'truck':
                    capacity = float(input("Enter cargo capacity: "))
                    vehicle = Truck(reg_num, make, model, capacity)
                elif vehicle_type == 'motorcycle':
                    engine_capacity = float(input("Enter engine capacity: "))
                    vehicle = Motorcycle(reg_num, make, model, engine_capacity)
                else:
                    print("Invalid vehicle type.")
                    continue

                fleet.add_vehicle(vehicle)
            elif choice == '2':
                fleet.display_vehicles()
            elif choice == '3':
                reg_num = input("Enter registration number to search: ")
                fleet.search_vehicle(reg_num)
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Exiting...")

if __name__ == "__main__":
    main()
