class Plant:
    def __init__(self, common_name, name = "Unnamed", species = "Unknown", watering_cycle = 1):
        self.plant = common_name
        self.name = name
        self.cycle = watering_cycle
        self.species = species
    def __str__(self):
        return f"Plant named {self.name}"
    def __repr__(self):
        return self.__str__

print("Welcome to the plant calendar!")
possible_commands = ['N', 'D', 'I', 'A', 'T', 'E']
print("Possible commands: \nN = New plant\nD = Delete plant\nI = Info on a specific plant\nA = See all palnts\nT = Which plants to water today\nE = Exit")
plants = []

def add_new_plant():
    # get necessary info, make new Plant, add Plant to list
    common_name = input("What is the common name for your plant? ")
    new_plant = Plant(common_name)
    plants.append(new_plant)

def delete_plant():
    # Use enumerate to print all plants in a list
    print("Which plant would you like to delete? Identify by the corresponding number")

def plant_info():
    # Find the wanted plant, call to string of that plant
    print("Which plant would you like to see? Identify by the corresponding number")

def see_all():
    # print all plants, use repr
    print("Plants in database:")

def to_water_today():
    #print all plants to be watered today, include date
    print("Plants to water today, insert-date-here :")

# Find a way to make function that takes in a date and returns which plants need watering on that date

action = 'S'
while(action != 'E'):
    action = input("What would you like to do? ")

    if action not in possible_commands:
        print("Please enter a valid action. This is case sensitive.")
        continue
    
    if action == 'N':
        add_new_plant()
    if action == 'D':
        delete_plant()
    if action == 'I':
        plant_info()
    if action == 'A':
        see_all()
    if action == 'T':
        to_water_today()
    if action == 'E':
        print("Thanks for visiting :)")
        break