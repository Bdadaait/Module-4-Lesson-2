
# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """Method to update the owner of the vehicle."""
        self.owner = new_owner
        print(f"Owner of vehicle{self.registration_number} updated to {new_owner}.")

    # Creating instances of vehicle
vehicle01 = Vehicle(" Y24", "Car", " Bdada Ait") 
vehicle02 = Vehicle(" GXL", "Truck", " Aylan Bell") 

print(f"Vehicle 1 - Reg: {vehicle01.registration_number}, Type: {vehicle01.type}, Owner: {vehicle01.owner}")
print(f"Vehicle 2 - Reg: {vehicle02.registration_number}, Type: {vehicle02.type}, Owner: {vehicle02.owner}")

    # Change the owners
vehicle01.update_owner("Sara cook")
vehicle02.update_owner("Amy Amber")

print(f"Vehicle 1 - Reg: {vehicle01.registration_number}, Type: {vehicle01.type}, Owner: {vehicle01.owner}")
print(f"Vehicle 2 - Reg: {vehicle02.registration_number}, Type: {vehicle02.type}, Owner: {vehicle02.owner}")

# Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added to {self.name}. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count
    
    # Extend an existing Event class 
event1 = Event("Tech Conference", "04-02-2024")
    # adding Participant
event1.add_participant()    
event1.add_participant()
event1.add_participant()

print(f"Total participants in {event1.name}: {event1.get_participant_count()}")
