class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        # Storing information about a specific computer
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Updating a computer's price
    def update_price(self, new_price):
        self.price = new_price

    # Updating a computer's OS
    def update_os(self, new_os):
        self.operating_system = new_os