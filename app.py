import getpass 
import myfitnesspal
import get_info
import json
import webbrowser
import os

from myfitnesspal.exceptions import MyfitnesspalLoginError


# Ask for credentials until corrrect
def get_credentials():
    while True:
        username = input("Enter username: ")    
        password = getpass.getpass(prompt = "Enter password: ")
        try:
            client = myfitnesspal.Client(username, password=password)
            print("Successfully connected!")
            break
        except MyfitnesspalLoginError:
            print("Oops! You entered incorrect credentials. Try again...")
    return client
    
# Ask for specific day and return weeks groceries
def get_starting_day():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1 instead of 01): "))
    day = int(input("Enter day (9 instead of 09): "))
    print("You chose: " + str(day) + '/' + str(month) + '/' + str(year))
    week = get_info.get_weeks_groceries(client, year, month, day)
    return week

def generate_json():
    week_items = week
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(week_items, f, ensure_ascii=False, indent=4)
    return "data.json"

def open_json_in_defaul_browser(file):
    webbrowser.open('file://'+ os.path.realpath(file))

def generate_xlsx():
    pass

client = get_credentials()
week = get_starting_day() 
file_name = generate_json()
open_json_in_defaul_browser(file_name)
