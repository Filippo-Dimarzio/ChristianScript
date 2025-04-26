# Lent Prayer Times App

## Overview

This app helps you keep track of the daily prayer schedule during Lent. It provides the remaining time for each prayer, including Morning, Midday, Afternoon, Evening, and Night prayers. The times are based on a fixed schedule, and the app calculates the time left for each prayer dynamically, updating every second.

## Features

- Displays the prayer times for **Morning Prayer (Lauds)**, **Midday Prayer (Sext)**, **Afternoon Prayer (None)**, **Evening Prayer (Vespers)**, and **Night Prayer (Compline)**.
- Shows a countdown for the time left until each prayer.
- Automatically updates prayer times at midnight.
- Works continuously, updating the time remaining for each prayer.
- **(New)** Dropdown language selection to view the app in different languages.

## Installation

To run the app, you’ll need Python 3.x installed on your machine. You will also need to install the following:

- `datetime` (built-in)
- `os` (built-in)
- `time` (built-in)

### Steps to Run:

1. Clone or download the repository.
2. Open the terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the command:
   ```bash
   python lent_prayer_times.py
