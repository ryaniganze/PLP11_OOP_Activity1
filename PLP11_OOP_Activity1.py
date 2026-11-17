

# ========================================
#  PARENT CLASS - PASSENGER
# ========================================

class Passenger:

    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date
    
    def get_passenger_info(self):
        return (
            f"Passenger Name: {self.name}\n"
            f"Departure Location: {self.location}\n"
            f"Destination: {self.destination}\n"
            f"Travel Date: {self.date}"
        )

    def get_weight_allowance(self):
        return 20

    
# ==========================================
# MEMBER 2: CHILD CLASS - ECONOMY
# ==========================================

class Economy(Passenger):

    def __init__(self, name, location, destination, date,
                 seat_preference):

        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_class_details(self):
        return f"Seat Preference: {self.seat_preference}"
    
# ==========================================
# CHILD CLASS - BUSINESS
# ==========================================

class Business(Passenger):

    def __init__(self, name, location, destination, date,
                 lounge_pass_code):

        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code

    # Method overriding
    def get_weight_allowance(self):
        return 100

    def get_class_details(self):
        return f"Lounge Pass Code: {self.lounge_pass_code}"


