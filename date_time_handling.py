### Date & Time Handling ###
## Characteristics of Date & Time Handling
# - Provides current date and time
# - Allows formatting and parsing dates
# - Supports date arithmetic (addition, subtraction)
# - Handles time zones (with `pytz` module)

from datetime import datetime, timedelta


print("\n $$$Date & Time$$$ \n")


# Get current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Format date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")  # YYYY-MM-DD HH:MM:SS
print("Formatted Date:", formatted_date)

# Extract components from date
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Date Arithmetic (Add/Subtract Days)
future_date = now + timedelta(days=7)  # Add 7 days
past_date = now - timedelta(days=7)  # Subtract 7 days
print("Future Date (After 7 days):", future_date)
print("Past Date (7 days ago):", past_date)

# Convert String to Date
date_str = "2025-03-29 15:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Converted Date Object:", date_obj)

# Get weekday name
weekday_name = now.strftime("%A")  # Full weekday name (e.g., Monday)
print("Today is:", weekday_name)
