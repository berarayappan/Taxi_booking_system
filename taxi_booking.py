#l3 question

class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.position = 'A'
        self.earnings = 0
        self.free_time = 0
        self.bookings = []


points = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}


def calculate_fare(pickup, drop):
    distance = abs(points[drop] - points[pickup]) * 15

    if distance <= 5:
        return 100

    return 100 + (distance - 5) * 10


def book_taxi(taxis, customer_id, pickup, drop, pickup_time):

    available_taxis = []

    for taxi in taxis:

        distance_to_customer = abs(
            points[taxi.position] - points[pickup]
        )

        if taxi.free_time + distance_to_customer <= pickup_time:

            available_taxis.append(
                (distance_to_customer,
                 taxi.earnings,
                 taxi)
            )

    if len(available_taxis) == 0:
        print("\nBooking Rejected")
        return

    available_taxis.sort(
        key=lambda x: (x[0], x[1])
    )

    selected_taxi = available_taxis[0][2]

    fare = calculate_fare(pickup, drop)

    trip_time = abs(
        points[drop] - points[pickup]
    )

    selected_taxi.position = drop

    selected_taxi.free_time = pickup_time + trip_time

    selected_taxi.earnings += fare

    selected_taxi.bookings.append({
        "Customer ID": customer_id,
        "Pickup": pickup,
        "Drop": drop,
        "Pickup Time": pickup_time,
        "Fare": fare
    })

    print("\nTaxi", selected_taxi.taxi_id, "Allotted")
    print("Fare =", fare)


def print_details(taxis):

    print("\n===== TAXI DETAILS =====")

    for taxi in taxis:

        print("\n----------------------")
        print("Taxi ID :", taxi.taxi_id)
        print("Position :", taxi.position)
        print("Free Time :", taxi.free_time)
        print("Earnings :", taxi.earnings)

        print("\nBookings:")

        if len(taxi.bookings) == 0:
            print("No Bookings")

        for booking in taxi.bookings:
            print(booking)


def main():

    taxis = []

    for i in range(1, 5):
        taxis.append(Taxi(i))

    while True:

        print("\n===== CALL TAXI BOOKING SYSTEM =====")
        print("1. Book Taxi")
        print("2. View Taxi Details")
        print("3. Exit")

        choice = int(input("Enter Choice : "))

        if choice == 1:

            customer_id = int(
                input("Enter Customer ID : ")
            )

            pickup = input(
                "Enter Pickup Point (A-F): "
            ).upper()

            drop = input(
                "Enter Drop Point (A-F): "
            ).upper()

            pickup_time = int(
                input("Enter Pickup Time : ")
            )

            book_taxi(
                taxis,
                customer_id,
                pickup,
                drop,
                pickup_time
            )

        elif choice == 2:

            print_details(taxis)

        elif choice == 3:

            print("Thank You")
            break

        else:

            print("Invalid Choice")


main()