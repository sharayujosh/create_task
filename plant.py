# THIS CODE IS WRITTEN INDEPENDANTLY BY ME.

import json

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
with open("schedule.txt") as schedule:
    tasks = [schedule.read()]

    print(tasks)

with open("record.txt") as record:
    records = [record.read()]

    print(record)

print(f"Welcome to the tasks tracker! You have {len(tasks)//2} tasks scheduled.")
possible_commands = ['N', 'E', 'D', 'A', 'T', 'U', 'X']
print("Possible commands: \nN = New task\nE = Edit record notes\nD = Delete task\nA = See all tasks\nT = Today's Tasks\nU = Upcoming tasks\nX = Exit")


def see_all():
    # print all plants, use repr
    print("Tasks in schedule: ")
    print(tasks)

def add_new_task():
    # get necessary info, make new Plant, add Plant to list
    name = input("What is the name of your task? ")
    cycle = input(f"After how many days should \"{name}\" be repeated? Enter an integer. ")
    t1 = {"name":name, "cycle":cycle}
    tasks.append(t1)
    # with open("schedule.txt", 'w') as schedule:
    #     schedule.write(json.dumps(tasks))
    last_done = input(f"Enter the last time the task was completed in the format MM/DD/YYYY: ")
    notes = input(f"Notes: ")
    t2 = {"name": name, "last_done":last_done, "notes":notes}
    records.append(t2)
    # with open("record.txt", 'w') as record:
    #     record.write(json.dumps(record))

def delete_task():
    # Use enumerate to print plants in a list
    see_all()
    key = input("Name of task to delete: ")
    try:
        del tasks[key]
    except KeyError:
        print("Invalid key. Must be EXACT.")

def edit_record():
    # Use enumerate to print plants in a list
    see_all()

def to_do_today():
    #print all plants to be watered today, include date
    print("Tasks to do today, insert-date-here :")

def upcoming():
    #print all plants to be watered today, include date
    print("Tasks to do today, insert-date-here :")

# Find a way to make function that takes in a date and returns which plants need watering on that date

action = 'S'
while(action != 'E'):
    action = input("What would you like to do? ")

    if action not in possible_commands:
        print("Please enter a valid action. This is case sensitive.")
        continue
    
    if action == 'N':
        add_new_task()
    if action == 'E':
        edit_record()
    if action == 'D':
        delete_task()
    if action == 'A':
        see_all()
    if action == 'T':
        to_do_today()
    if action == 'U':
        upcoming()
    if action == 'X':
        print("Thanks for visiting :)")
        break

    with open("schedule.txt", 'w') as schedule:
        schedule.write(json.dumps(tasks))
    with open("record.txt", 'w') as record:
        record.write(json.dumps(records))