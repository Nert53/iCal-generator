import uuid
from datetime import date


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
    calendar_file.write("BEGIN:VCALENDAR\r\n")
    calendar_file.write("VERSION:2.0\r\n")
    calendar_file.write("PRODID:-//K Desktop Environment//NONSGML v1.0//EN\r\n")


def write_end(calendar_file):
    calendar_file.write("END:VCALENDAR")


def create_uid():
    return str(uuid.uuid4())


def create_event(calendar_file, name, year, month, day):
    calendar_file.write("BEGIN:VEVENT\r\n")
    calendar_file.write(f"UID:{create_uid()}\r\n")

    calendar_file.write(f"DTSTAMP:{get_todays_date()}T000000Z\r\n")
    calendar_file.write(f"SUMMARY:{name}")
    calendar_file.write("STATUS:CONFIRMED\r\n")
    calendar_file.write(f"RRULE:FREQ=YEARLY;BYMONTH={month}\r\n")

    calendar_file.write(f"DTSTART;VALUE=DATE:{year}")
    right_entry_format(calendar_file, month)
    right_entry_format(calendar_file, day)
    calendar_file.write("\r\n")

    calendar_file.write(f"DTEND;VALUE=DATE:{year}")
    right_entry_format(calendar_file, month)
    right_entry_format(calendar_file, day)
    calendar_file.write("\r\n")
    
    calendar_file.write("END:VEVENT\r\n")


def right_entry_format(calendar_file, data):
    if data < 10:
        calendar_file.write(f"0{data}")
    else:
        calendar_file.write(f"{data}")


def set_days_in_month(month):
    if month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
       return 31
    else:
        return 30


def get_todays_date():
    today = date.today()
    formated_str = today.strftime("%Y%m%d")
    return formated_str
    

if __name__ == "__main__":
    main()