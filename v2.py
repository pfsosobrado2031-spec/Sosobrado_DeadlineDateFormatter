# FA 4: Deadline and Date Formatter
# Version 2 - Added Date Formatting

# Import the datetime module
from datetime import datetime

# Ask the user for event details
event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Create a date object
event_date = datetime(year, month, day)

# Format the date into readable values
formatted_date = f"{event_date.strftime('%B')} {day}, {year}"
month_name = event_date.strftime("%B")
weekday = event_date.strftime("%A")

# Display the formatted event details
print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", formatted_date)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday)
