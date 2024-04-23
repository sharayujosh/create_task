# THIS CODE IS WRITTEN INDEPENDANTLY BY ME.

import json
from datetime import date

tasks = {}
records = {}
def load_from_file():
    with open("schedule.txt") as schedule:
        for row in schedule:
            tasks.update(json.loads(row)) 

        print(tasks)
    with open("record.txt") as record:
        for row in record:
            records.update(json.loads(row)) 
    print(records)

def save_to_file():
    with open("schedule.txt", 'w') as schedule:
        schedule.write(json.dumps(tasks))
    with open("record.txt", 'w') as record:
        record.write(json.dumps(records))

load_from_file()
print(f"Welcome to the tasks tracker! You have {len(tasks)} tasks scheduled.")
possible_commands = ['N', 'R', 'E', 'D', 'A', 'T', 'U', 'X']
print("Possible commands: \nN = New task\nR = New record\nE = Edit record notes\nD = Delete task\nA = See all tasks\nT = Today's Tasks\nU = Upcoming tasks\nX = Exit")

def see_all():
    print("Tasks in schedule: ")
    print(tasks)

def add_record():
    done_today = input("Which task did you do today? ")
    today = date.today()
    records[done_today]["last_done"] = str(today.year) + "-" + f'{str(today.month):0>2}' + "-" + f'{str(today.day):0>2}'

def add_new_task():
    name = input("What is the name of your task? ")
    cycle = input(f"After how many days should \"{name}\" be repeated? Enter an integer. ")
    t1 = {name: {"cycle_days":cycle}}
    tasks.update(t1)

    last_done = input(f"Enter the last time the task was completed in the format YYYY-MM-DD: ")
    notes = input(f"Notes: ")
    t2 = {name:{"last_done":last_done, "notes":notes}}
    records.update(t2)

def delete_task():
    see_all()
    key = input("Name of task to delete: ")
    try:
        del tasks[key]
    except KeyError:
        print("Invalid key. Must be EXACT.")

def edit_record():
    see_all()
    print("Currently unavailable")

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_between(date1):
        date2 = date.today()
        if date1.month == date2.month and date1.year == date2.year:
            return abs(date1.day - date2.day)
        days = days_in_month[date2.month - 1] - date1.day

        for i in range(date2.month - 2, date1.month - 1, -1):
            days += days_in_month[i]

        days += date2.day - 1
        days += 365 * (date1.year - date2.year)
        days += abs(date1.year - date2.year) // 4 if date1.month != 1 else 0
        return abs(days)

def to_do_today():
    print("Tasks to do today:")
    for i in tasks:
        last = date.fromisoformat(records[i]["last_done"])
        if(days_between(last) >= int(tasks[i]["cycle_days"])):
            print(i)

def upcoming():
    print("Tasks to do today, insert-date-here :")

action = 'S'
while(action != 'E'):
    action = input("What would you like to do? ")

    if action not in possible_commands:
        print("Please enter a valid action. This is case sensitive.")
        continue
    
    if action == 'N':
        add_new_task()
    if action == 'R':
        add_record()
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

    print(tasks)
    print(records)
    
    save_to_file()