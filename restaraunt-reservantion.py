from datetime import datetime

class Costumer():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = int(phone)
        self.email = email


class Table():
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = int(capacity)    # number of people that can sit at the table
        self.reserved = False

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            return True
        return False
    
    
    def cancel_reservation(self):
        if self.reserved:
            self.reserved = False
            return True
        return False
    
    def __str__(self):
        status_table = "Reserved" if self.reserved else "Not Reserverd"
        return (f"Table Number: {self.table_number}\n"
                f"Capacity: {self.capacity}\n"
                f"Status: {status_table}")
    
class Reservation():
    def __init__(self, ocassion, table, date, time, costumer_name):
        self.ocassion = ocassion
        self.table = table
        self.date = date
        self.time = time 
        self.costumer_name = costumer_name


    def __str__(self):
        return (f"Number of People: {self.table}\n"
                f"Costumer: {self.costumer_name}\n"
                f"Ocassion: {self.ocassion}\n"
                f"Date: {self.date.strftime('%d/%m/%Y')}\n"
                f"Time: {self.time.strftime('%H:%M')}")

class Restaurant():
    def __init__(self):
        self.tables = [Table(i, 4) for i in range(1, 5)]
        self.reservations = []
        self.costumers = []

    def add_costumer_details(self, costumer):
        self.costumers.append(costumer)

    def table_list(self):
        for i, table in enumerate(self.tables, 1):
            print(f' {table}')

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def table_reservation(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                if table.reserve():
                    print(f'Table {table_number} has been reserved.')
                    table.reserve()
                    self.add_reservation(Reservation)
                    return True
                else:
                    print(f'Table {table_number} is already reserved.')
                    return False
        print(f'Table {table_number} not found.')
        return False
    
    def cancel_reservation(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                if table.cancel_reservation():
                    print(f'Table {table_number} reservation has been canceled.')
                    self.reservations.remove(Reservation)   
                    return True
                else:
                    print(f'Table {table_number} is not reserved.')
                    return False
        print(f'Table {table_number} not found.')
        return False

    def reservation_list(self):
        for i, reservation in enumerate(self.reservations, 1):
            print(f'{reservation}')
    
    
def table_menu():
    print("Restaurant Table Reservation")
    print("1. Reserve Table")
    print("2. Cancel Reservation")
    print("3. List Reservations")
    print("5. Exit")

def main():
    restaurant = Restaurant()

    while True:
        table_menu()
        choice = input("Enter your choice: ")

        
        if choice == '1':
            restaurant.table_list()
            
            table_number = int(input("Enter the table number: "))
            if restaurant.table_reservation(table_number):
                print("Reservation Details")
                print("------------------")
                ocassion = input("Enter the ocassion: ")
                table = int(input("Quantity of people: "))
                while True:
                    date_str = input("Enter the date: ")
                    try:
                        date = datetime.strptime(date_str, "%d/%m/%Y")
                        if date < datetime.now():
                            print("Invalid date. Try again: ")
                        else:
                            break
                    except ValueError:
                        print("Invalid date. Try again: ")

                while True:
                    time_str = input("Enther the time:")
                    try:
                        time = datetime.strptime(time_str, "%H:%M").time()
                        break
                    except ValueError:
                        print("Invalid time. Try again: ")

                print("Costumer Details: ")
                name = input("Name: ")
                phone = int(input("Phome Number: "))
                email = input("Email: ")
                costumerDetails = Costumer(name, phone, email)
                restaurant.add_costumer_details(costumerDetails)
                reservation = Reservation(ocassion, table, date, time, costumer_name=name)
                restaurant.add_reservation(reservation)
                print("Table reserved successfully.")
              
            else:
                print("Please choose another table.")
                


        elif choice == '2':
            table_number = int(input("Enter the table number: "))
            restaurant.cancel_reservation(table_number)
        elif choice == '3':
            restaurant.reservation_list()
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()