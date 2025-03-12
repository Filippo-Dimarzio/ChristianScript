import time
import os
from datetime import datetime, timedelta

# Lent Prayer Times (Sample Times)
prayer_times = {
    "Morning Prayer (Lauds)": "06:30",
    "Midday Prayer (Sext)": "12:00",
    "Afternoon Prayer (None)": "15:00",  # Jesus' Crucifixion
    "Evening Prayer (Vespers)": "18:30",
    "Night Prayer (Compline)": "21:00"
}

# Convert times to datetime objects
def get_prayer_times():
    return {name: datetime.strptime(time_str, "%H:%M").time() for name, time_str in prayer_times.items()}

prayer_times_today = get_prayer_times()

# Function to calculate time left for each prayer
def get_time_left():
    now = datetime.now()
    time_left = {}

    for name, prayer_time in prayer_times_today.items():
        event_time = datetime.combine(now.date(), prayer_time)

        if now > event_time:
            event_time += timedelta(days=1)  # Move to next day if already passed

        time_left[name] = event_time - now

    return time_left

# Function to display prayer times and countdowns
def display_prayers_and_countdowns():
    last_update_day = datetime.today().day  # Track the day to update times

    while True:
        now = datetime.now()

        # Update prayer times at midnight
        if now.day != last_update_day:
            global prayer_times_today
            prayer_times_today = get_prayer_times()
            last_update_day = now.day

        os.system("clear")  # Clear screen for smooth display

        print("\n✝️ **Lent Prayer Schedule:**\n")
        time_left = get_time_left()

        for name, prayer_time in prayer_times_today.items():
            remaining_time = str(time_left[name]).split('.')[0]  # Remove milliseconds
            print(f"🙏 {name}: {prayer_time.strftime('%H:%M')}")
            print(f"   ⏳ Time left: {remaining_time}\n")

        time.sleep(1)  # Update every second

# Run program
display_prayers_and_countdowns()

