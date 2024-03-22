import csv

# class Task:
#     def __init__(self, name, unit, cycle, last_done):
#         self.name = name
#         self.cycle = cycle
#         self.cycle_unit = unit
#         self.last_done = last_done
#     def __str__(self):
#         return f"{self.name}, last done {self.last_done}, must happen every {self.cycle} {self.cycle_units}"
#     def __repr__(self):
#         return self.__str__

with open("schedule.csv", 'r') as schedule:
    csvreader = csv.DictReader(schedule)
    tasks = []

    for row in csvreader:
        tasks.append(row)
    
    if len(tasks) == 0:
        new = True


print(f"Welcome to the tasks tracker! You have {len(tasks)} tasks scheduled.")
possible_commands = ['N', 'E', 'D', 'A', 'T', 'U', 'X']
print("Possible commands: \nN = New task\nE = Edit task\nD = Delete task\nA = See all tasks\nT = Today's Tasks\nU = Upcoming tasks\nX = Exit")


def add_new_task():
    # get necessary info, make new Plant, add Plant to list
    name = input("What is the name of your task? ")
    unit = input("Is this task repeated every day, month, or year? ")
    cycle = input(f"After how many {unit} should \"{name}\" be repeated? Enter an integer. ")
    last_done = input(f"Enter the last time the task was completed in the format MM/DD/YYYY")
    t = [name, unit, cycle, last_done]
    with open("schedule.csv", 'a') as schedule:
        csvwriter = csv.DictWriter(schedule, fieldnames=["name", "unit", "cycle", "last_done"])
        if new:
            csvwriter.writeheader()
            new = False
        csvwriter.writerow(t)
        print("Task added.")

def delete_plant():
    # Use enumerate to print  plants in a list

    print("Which task would you like to delete?")

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