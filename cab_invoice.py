class Ride:

    def __init__(self, distance, time, type):
        self.distance = distance
        self.time = time
        self.type = type
        self.total_fare = self.calculate_fare()

    def calculate_fare(self):
        """
            This function calculate the total fare

            :return: total fare after calculation
            """
        if self.type == 1:
            MINIMUM_FARE = 5
            if self.distance < 1:
                totalFare = MINIMUM_FARE
            else:
                totalFare = int(self.distance) * 10 + int(self.time) * 1
            # print("Total Fare ", totalFare)
            return totalFare
        elif self.type == 2:
            MINIMUM_FARE = 20
            if self.distance < 5:
                totalFare = MINIMUM_FARE
            else:
                totalFare = int(self.distance) * 15 + int(self.time) * 2
            # print("Total Fare ", totalFare)
            return totalFare
        else:
            print("Invalid Input")


class User:
    def __init__(self, user_id):
        self.rides_list = []
        self.user_id = user_id

    def add_ride(self, ride):
        """
        This function adds the ride object into ride list
        :param ride: ride
        :return: ride object
        """

        self.rides_list.append(ride)
        return self.rides_list


class InvoiceGenerator:

    def __init__(self):
        self.user_list = []

    @staticmethod
    def create_user_object(user_id):
        """
        This function creates the user object
        :param user_id: user id
        :return: user object
        """
        user = User(user_id)
        return user

    @staticmethod
    def ride_object():
        """
        This function creates the ride object
        :return: ride object
        """
        distance = int(input("Enter distance: "))
        time = int(input("Enter time: "))
        type = int(input("Enter type 1.Normal Ride 2. Premium ride\n"))
        ride = Ride(distance, time, type).calculate_fare()
        return ride

    def check_user(self, user_id):
        """
        This function checks whether user is already present in the list
        :param user_id: user id
        :return: 0 if user is not present 1 if user is present
        """
        check = 0
        for user in self.user_list:
            if user.user_id == user_id:
                ride = self.ride_object()
                user.add_ride(ride)
                check = 1
                break
        return check

    def check_invoice(self, user_id):
        """
        This function adds user to the user list
        :param user_id: user id
        :return: user list
        """
        check = self.check_user(user_id)
        if check == 0:
            user_obj = self.create_user_object(user_id)
            ride = self.ride_object()
            user_obj.add_ride(ride)
            self.user_list.append(user_obj)
        print(self.user_list)

    def display_user(self, user_id):
        """
        This functions displays particular user
        :param user_id: user id
        :return: user list of searched id
        """
        for user in self.user_list:
            if user.user_id == user_id:
                for ride in user.rides_list:
                    print(ride)

    def display_all_user(self):
        """
        This function display details of all user
        :return: user list
        """
        for user in self.user_list:
            for ride in user.rides_list:
                print(ride)

    def ride_count(self, user_id):
        for user in invoice_generator.user_list:
            if user.user_id == user_id:
                for ride in user.rides_list:
                    rides_count = len(user.rides_list)
                    print("Total number of rides ", rides_count)
                    return rides_count

    def total_fare(self, user_id):
        total_aggregate = 0
        for user in invoice_generator.user_list:
            if user.user_id == user_id:
                for ride in user.rides_list:
                    total_aggregate = sum((user.rides_list))
                    print("Total aggregate : ", total_aggregate)
                    return total_aggregate

    def calculate_average(self, user_id):
        for user in invoice_generator.user_list:
            if user.user_id == user_id:
                average = self.total_fare(user_id) / self.ride_count(user_id)
                print("Average of rides ", average)
                return average


if __name__ == '__main__':
    invoice_generator = InvoiceGenerator()
    while True:
        choice = int(input("1.Add Ride 2. Invoice by user 3. Total List 4. Calculate average\n"))
        if choice == 1:
            u_id = input("Enter user id: ")
            invoice_generator.check_invoice(u_id)
        elif choice == 2:
            u_id = input("Enter user id: ")
            invoice_generator.display_user(u_id)
        elif choice == 3:
            invoice_generator.display_all_user()
        elif choice == 4:
            u_id = input("Enter user id: ")
            invoice_generator.calculate_average(u_id)

        else:
            exit(0)
