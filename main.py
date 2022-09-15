import uuid

def main():
    months_count = 12
    begin_year = 2020

    calendar = open("calendar.ics", "w+")
    names_file = open("name_list.txt", encoding="utf-16")
    names = names_file.readlines()
    names_file.close()

    write_start(calendar)

    iteration = 1
    for month in range(1, months_count + 1):
        days = set_days_in_month(month)

        for day in range(days):
            name = names.pop(0)
            create_event(calendar, name, begin_year, month, (day + 1))
            iteration += 1

    write_end(calendar)
    calendar.close()

def write_start(calendar_file):
    calendar_file.write("BEGIN:VCALENDAR\n")
    calendar_file.write("VERSION:2.0\n")
    calendar_file.write("PRODID:-//K Desktop Environment//NONSGML v1.0//EN\n")
    
def write_end(calendar_file):
    calendar_file.write("END:VCALENDAR")

def create_uid():
    return str(uuid.uuid4())

def create_event(calendar_file, name, year, month, day):
    calendar_file.write("BEGIN:VEVENT\n")
    calendar_file.write(f"UID:{create_uid()}\n")
    calendar_file.write(f"DTSTAMP:20200101T000000Z\n")
    calendar_file.write(f"SUMMARY:{name}")
    calendar_file.write("STATUS:CONFIRMED\n")
    calendar_file.write(f"RRULE:FREQ=YEARLY;BYMONTH={month}\n")

    calendar_file.write(f"DTSTART;VALUE=DATE:{year}")
    right_entry_format(calendar_file, month)
    right_entry_format(calendar_file, day)
    calendar_file.write("\n")

    calendar_file.write(f"DTEND;VALUE=DATE:{year}")
    right_entry_format(calendar_file, month)
    right_entry_format(calendar_file, day)
    calendar_file.write("\n")

    add_notification(calendar_file)
    
    calendar_file.write("END:VEVENT\n")

def right_entry_format(calendar_file, data):
    if data < 10:
        calendar_file.write(f"0{data}")
    else:
        calendar_file.write(f"{data}")

def add_notification(calendar_file):
    calendar_file.write("BEGIN:VALARM\n")
    calendar_file.write("ACTION:DISPLAY\n")
    calendar_file.write("DESCRIPTION:This is an event reminder\n")
    calendar_file.write("TRIGGER:P0DT9H30M0S\n")
    calendar_file.write("END:VALARM\n")


def set_days_in_month(month):
    if month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
       return 31
    else:
        return 30

if __name__ == "__main__":
    main()