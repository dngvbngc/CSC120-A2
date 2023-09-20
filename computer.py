class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str, 
                 year_made: int, 
                 price: int):
        # Storing information about a specific computer
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Updating a computer's price
    def update_price(self, new_price: int):
        self.price = new_price

    # Updating a computer's OS
    def update_os(self, new_os: str):
        self.operating_system = new_os
