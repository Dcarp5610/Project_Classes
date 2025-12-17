class Car:
    def __init__(self, car_id, name, make, body, year, value):
        self.id = int(car_id)
        self.name = name
        self.make = make
        self.body = body
        self.year = int(year)
        self.value = float(value)

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value:.1f}"


class CarInventory:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.cars = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split("\t")
                    if len(parts) == 6:
                        car = Car(*parts)
                        self.cars.append(car)
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.filename, "w") as f:
            for car in self.cars:
                f.write(str(car) + "\n")
        print("Data saved to local file successfully!")

    def add_car(self, car):
        for c in self.cars:
            if c.id == car.id:
                print("Incorrect Id. Id already exist in the system.")
                return
        for c in self.cars:
            if (c.name == car.name and c.make == car.make and
                c.body == car.body and c.year == car.year and
                c.value == car.value):
                print("The car is already in the inventory. No action is required..")
                return
        self.cars.append(car)
        print("car is added to the inventory.")
        print(car)

    def search_by_id(self, car_id):
        for c in self.cars:
            if c.id == car_id:
                print("Car found", c)
                return c
        print("Car not found")
        return None

    def search_by_name(self, name):
        for c in self.cars:
            if c.name.lower() == name.lower():
                print("Car found", c)
                return c
        print("Car not found")
        return None

    def edit_car(self, car_id, name, make, body, year, value):
        for c in self.cars:
            if c.id == car_id:
                c.name = name
                c.make = make
                c.body = body
                c.year = year
                c.value = value
                print("Car's new info is", c)
                return
        print("Car not found")

    def remove_car(self, car_id):
        for c in self.cars:
            if c.id == car_id:
                self.cars.remove(c)
                print("car removed")
                return
        print("Car not found")

    def print_cars(self):
        for c in self.cars:
            print(c)


def main():
    inventory = CarInventory()
    print("Welcome to the cars Inventory system")

    while True:
        print("What would you like to do today?")
        print("-Add a car? enter 1")
        print("-Search for car? enter 2")
        print("-Edit car info? enter 3")
        print("-Remove a car? enter 4")
        print("-Print the car list? enter 5")
        print("-Save the data to a file? enter 6")
        print("-Exit? enter 0.")

        choice = input().strip()
        print(choice)

        if choice == "1":
            while True:
                print("Enter id of the car, followed by the car's information.")
                car_id = int(input("Id:\n"))
                print(car_id)
                name = input("name:\n")
                print(name)
                make = input("make:\n")
                print(make)
                body = input("Body:\n")
                print(body)
                year = int(input("year:\n"))
                print(year)
                value_str = input("value:\n")
                print(value_str)
                value = float(value_str)
                car = Car(car_id, name, make, body, year, value)
                inventory.add_car(car)
                more = input("Do you want to add more cars? y(yes)/n(no) ")
                print(more)
                if more.lower() != "y":
                    break

        elif choice == "2":
            print("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
            sub_choice = input().strip()
            print(sub_choice)
            if sub_choice == "1":
                car_id = int(input("Please Enter the id of the car: "))
                print(car_id)
                inventory.search_by_id(car_id)
            elif sub_choice == "2":
                name = input("Please Enter the name of the car: ")
                print(name)
                inventory.search_by_name(name)
            elif sub_choice == "-1":
                pass
            else:
                print("Invalid choice, please try again.")

        elif choice == "3":
            car_id = int(input("Enter the id of the car. Enter -1 to return to the previous menu "))
            print(car_id)
            if car_id == -1:
                continue
            name = input("Name:\n")
            print(name)
            make = input("make:\n")
            print(make)
            body = input("Body:\n")
            print(body)
            year = int(input("year:\n"))
            print(year)
            value_str = input("value:\n")
            print(value_str)
            value = float(value_str)
            inventory.edit_car(car_id, name, make, body, year, value)

        elif choice == "4":
            car_id = int(input("Enter id of the car that you want to remove from the inventory.\nid: "))
            print(car_id)
            inventory.remove_car(car_id)
            more = input("Do you want to remove more cars? y(yes)/n(no) ")
            print(more)
            if more.lower() != "y":
                continue

        elif choice == "5":
            inventory.print_cars()

        elif choice == "6":
            inventory.save_to_file()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()