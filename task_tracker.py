# THIS CODE IS WRITTEN INDEPENDANTLY BY ME.

import json
from datetime import date, timedelta

tasks = {}
records = {}
def load_from_file():
    with open("schedule.txt") as schedule:
        for row in schedule:
            tasks.update(json.loads(row)) 

    with open("record.txt") as record:
        for row in record:
            records.update(json.loads(row))

def save_to_file():
    with open("schedule.txt", 'w') as schedule:
        schedule.write(json.dumps(tasks))
    with open("record.txt", 'w') as record:
        record.write(json.dumps(records))

load_from_file()
print(f"Welcome to the tasks tracker! You have {len(tasks)} tasks scheduled.")
possible_commands = ['N', 'R', 'E', 'D', 'S', 'A', 'T', 'U', 'X']
print("Possible commands: \nN = New task\nR = New record\nE = Edit task cycle\nD = Delete task\nS = See task info\nA = See all tasks\nT = Today's Tasks\nU = Upcoming tasks\nX = Exit")


def see_all():
    print("Tasks in schedule: ")
    for key in tasks:
        print(key)

def add_record():
    done_today = input("Which task did you do today? ")
    today = date.today()
    records[done_today]["last_done"] = str(today.year) + "-" + f'{str(today.month):0>2}' + "-" + f'{str(today.day):0>2}'
    print("Added!")

def add_new_task():
    name = input("What is the name of your task? ")
    cycle = int(input(f"After how many days should \"{name}\" be repeated? Enter an integer. "))
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

def edit_task():
    see_all()
    key = input("Name of task to edit: ")
    new_cycle = int(input("What is the new cycle period for this task (in days)? "))
    tasks[key] =  {"cycle_days":new_cycle}

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_between(date1, date2 = date.today()):
        if date1.month == date2.month and date1.year == date2.year:
            return abs(date1.day - date2.day)
        days = days_in_month[date2.month - 1] - date1.day

        # date2 is assumed to be after date1, both months are subtracted by one to line up with list index
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
        if(days_between(last) >= tasks[i]["cycle_days"]):
            print(i)

def to_do_someday(day):
    to_do = []
    for i in tasks:
        last = date.fromisoformat(records[i]["last_done"])
        if(days_between(last, day) >= tasks[i]["cycle_days"]):
            to_do.append(i)
    if(len(to_do) != 0):
        return to_do
    else:
        return ["No tasks upcoming"]

def see_task():
    see_all()
    key = input("Name of task to see: ")
    print(key, 'is done every', tasks[key]['cycle_days'], 'days.')
    print('Last done:', records[key]['last_done'], 'with notes \"', records[key]['notes'], '\"')

def upcoming():
    print("Tasks to do in the next 3 days:")
    day = date.today() + timedelta(days = 3)
    to_do = to_do_someday(day)
    for i in to_do:
        print(i)


action = 'S'
while(action != 'X'):
    action = input("\nWhat would you like to do? ")

    if action not in possible_commands:
        print("Please enter a valid action. This is case sensitive.")
        continue
    
    if action == 'N':
        add_new_task()
    if action == 'R':
        add_record()
    if action == 'E':
        edit_task()
    if action == 'D':
        delete_task()
    if action == 'S':
        see_task()
    if action == 'A':
        see_all()
    if action == 'T':
        to_do_today()
    if action == 'U':
        upcoming()
    if action == 'X':
        print("Thanks for visiting :)")
        break
    
    save_to_file()
