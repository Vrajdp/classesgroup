#group number : sec I group 4
# Team members : Vraj Patel, Dev Mandora, Parv Patel
import csv
import os
from Appointment import Appointment

# Global variable to store the weekly calendar
weekly_calendar = []

# Function to display the main menu
def display_menu():
    menu_options = """
    Jojo's Hair Salon Appointment Manager
    ======================================
    1) Schedule an appointment
    2) Find appointment by name
    3) Print calendar for a specific day
    4) Cancel an appointment
    9) Exit the system
    """
    print(menu_options)
    return input("Enter your selection: ")

# Function to initialize the weekly calendar
def create_weekly_calendar():
    global weekly_calendar
    weekly_calendar = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days_of_week:
        for hour in range(9, 17):
            appointment = Appointment(day, hour)
            weekly_calendar.append(["", "", "available", day, hour, hour + 1])

# Function to load appointments from a file
def load_appointments_from_file():
    file_name = input("Enter the appointment file name: ")
    file = open(file_name, "r")
    
    for line in file.readlines():
        client_name, client_phone, appt_type, day, hour = line.strip().split(',')
        appointment = find_appointment(day, int(hour))
        if appointment:
            appointment.schedule(client_name, client_phone, appt_type)

    file.close()

# Function to find an appointment in the weekly calendar by day and start hour
def find_appointment(day, start_hour):
    for obj in weekly_calendar:
        if obj[3] == day and obj[4] == start_hour: 
            return obj

# Function to find and display appointments for a given client name
def find_appointment_by_name(name):
    print(f"Appointments for {name}")
    print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("=" * 120)

    appointment_found = False
    for appointment in weekly_calendar:
        if name.lower() in appointment[0].lower():
            appointment_found = True
            start_time = f"{appointment[4]:02d}:00"
            end_time = f"{appointment[5]:02d}:00"
            appt_type = appointment[2].capitalize() if appointment[2] != "available" else "Available"
            print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format(appointment[0], appointment[1], appointment[3].capitalize(), start_time, end_time, appt_type))

    if not appointment_found:
        print(f"No appointments found for {name}.")

# Function to display appointments for a specific day
def show_appointments_by_day(day):
    day = day.lower()
    print(f"Appointments for {day.capitalize()}")
    print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("=" * 110)

    for appointment in weekly_calendar:
        if appointment[3].lower() == day:
            start_time = f"{appointment[4]:02d}:00"
            end_time = f"{appointment[5]:02d}:00"
            appt_type = appointment[2].capitalize() if appointment[2] != "available" else "Available"
            print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format(appointment[0], appointment[1], appointment[3].capitalize(), start_time, end_time, appt_type))

# Function to schedule a new appointment
def save_scheduled_appointments_list():
    print("**Schedule an appointment**")
    day = input("What day: ").lower()
    startTime = int(input("Enter start hour (24-hour clock): "))

    if startTime not in range(9, 17) or day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
        print("Sorry, that time slot is not in the weekly calendar!")
        return

    for appointment in weekly_calendar:
        if appointment[3].lower() == day and appointment[4] == startTime:
            if appointment[2] != "available":
                print("Sorry, that time slot is already booked")
                return

            name = input("Client Name: ")
            phone = input("Client Phone: ")
            print("Appointment types")
            print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
            appointment_type = input("Type of Appointment: ")
            if appointment_type not in ["1", "2", "3", "4"]:
                print("Sorry, that is not a valid appointment type!")
                return

            appointment[0] = name
            appointment[1] = phone
            appointment[2] = appointment_type
            print(f"OK, {name}'s appointment is scheduled!")
            return

    print("No suitable appointment slot found.")

# Function to save scheduled appointments to a file
def save_scheduled_appointments():
    count = 0
    while True:
        filename = input("Enter appointment filename: ")

        if os.path.exists(filename):
            overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ")
            if overwrite.lower() != "y":
                continue

        filename = input("Enter appointment filename: ")
        file = open(filename, "w", newline='')

        filewriter = csv.writer(file)
        for appointment in weekly_calendar:
            if appointment[2] != "available":
                count += 1
                filewriter.writerow(appointment)

        file.close()

        if count != 0:
            print(f"{count} scheduled appointments have been successfully saved")
            return

# Function to cancel an appointment
def cancel_appointment(day, start):
    day = day.lower()
    if day == "sunday" or start not in range(9, 17):
        print("Sorry, that time slot is not in the weekly calendar!")
        return

    for appointment in weekly_calendar:
        if appointment[3].lower() == day and appointment[4] == start:
            if appointment[2] != "available":
                appointment[0], appointment[1], appointment[2] = "", "", "available"
                print(f"{day.capitalize()} {start}-{start + 1} appointment has been cancelled")
                return
            else:
                print("That time slot isn't booked and doesn't need to be cancelled")
                return

    print("No appointment found for the given time slot")

# Main function to run the appointment manager system
def main():
    print("Starting the Appointment Manager System")
    create_weekly_calendar()
    print("Weekly calendar created")
    load_appointment = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
    if load_appointment.lower() =="y":
        filename = input("Enter appointment filename: ")
        while os.path.exists(filename) == False:
            filename = input("File not found. Re-enter appointment filename: ")
        file = open(filename, "r")
        lines = file.readlines()
        for line in lines:
            newLine = line.rstrip("\n")
            for i in weekly_calendar:
                LineList = newLine.split(",")
                if str(LineList[3]).lower() == str(i[3]).lower() and int(LineList[4]) == int(i[4]) and str(i[2]) == "available":
                    i[0] = LineList[0]
                    i[1] = LineList[1]
                    i[2] = LineList[2]

        print(f"{len(lines)} previously scheduled appointments have been loaded")

    while True:
        user_choice = display_menu()
        if user_choice == "1":
            save_scheduled_appointments_list()
        elif user_choice == "2":
            print("** Find appointment by name **")
            client_name = input("Enter client name to search: ")
            find_appointment_by_name(client_name)
        elif user_choice == "3":
            print("** Print calendar for a specific day **")
            day = input("Enter day of the week: ")
            show_appointments_by_day(day)
        elif user_choice == "4":
            print("** Cancel an appointment **")
            day = input("What day:")
            start = int(input("Enter start hour (24-hour clock): "))
            cancel_appointment(day, start)
        elif user_choice == "9":
            print("** Exit the system** ")
            if input("Save changes to file? (Y/N): ").lower() == 'y':
                save_scheduled_appointments()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()