# appointment.py
#group number : sec I group 4
# Team members : Vraj Patel, Dev Mandora, Parv Patel
class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        # Constructor to initialize appointment attributes
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

    def get_client_name(self):
        # Getter method to retrieve the client's name
        return self.client_name

    def get_client_phone(self):
        # Getter method to retrieve the client's phone number
        return self.client_phone

    def get_appt_type(self):
        # Getter method to retrieve the appointment type
        return self.appt_type

    def get_day_of_week(self):
        # Getter method to retrieve the day of the week
        return self.day_of_week

    def get_start_time_hour(self):
        # Getter method to retrieve the start time hour
        return self.start_time_hour

    def get_end_time_hour(self):
        # Getter method to calculate and retrieve the end time hour
        return self.start_time_hour + 1

    def get_appt_type_desc(self):
        # Getter method to retrieve the description of the appointment type
        types = {0: "Available", 1: "Mens Cut $50", 2: "Ladies Cut $80", 3: "Mens Colouring $50", 4: "Ladies Colouring $120"}
        return types.get(self.appt_type, "Invalid Type")

    def set_client_name(self, name):
        # Setter method to set the client's name
        self.client_name = name

    def set_client_phone(self, phone):
        # Setter method to set the client's phone number
        self.client_phone = phone

    def set_appt_type(self, appt_type):
        # Setter method to set the appointment type
        self.appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        # Method to schedule the appointment with client details and appointment type
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type

    def cancel(self):
        # Method to cancel the appointment by resetting client details and appointment type
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0

    def format_record(self):
        # Method to format appointment details as a string for saving to a file
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour:02d}"

    def __str__(self):
        # String representation of the appointment for display purposes
        return f"{self.client_name.ljust(20)} {self.client_phone.ljust(15)} {self.day_of_week.ljust(9)} {self.start_time_hour:02d}:00 - {self.get_end_time_hour():02d}:00 {self.get_appt_type_desc()}"
