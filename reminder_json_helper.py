import os
import json

def reminder_json_exists():
    return os.path.isfile(reminder.json)

def read_reminder_json():
    if reminder_json_exists():
        with open('reminder.json') as reminder_json:
            data = json.load(reminder_json)
            return data['reminders']

def create_reminder_json(reminder):
    if not reminder_json_exists():
        data = {}
        data['reminders'] = []
        data['reminders'].append(reminder)
        write_json_reminder(data)
    else:
        update_json_reminder(reminder)

def update_json_reminder(reminder):
    with open('reminders.json') as reminder_json:
        data = json.load(reminder_json)
        reminders = data['reminders']
        reminders.append(reminder)
        write_json_reminder(data)

def write_json_reminder(data, filename='reminder.json'):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)
