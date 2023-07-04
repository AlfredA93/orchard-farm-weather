from datetime import datetime
import time
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import plotext
import blessed


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('orchard_farm_weather_data')

DF = pd.DataFrame(SHEET.worksheet('data').get_all_records())

TERM = blessed.Terminal()


def title():
    """
    This function prints the Title whenever this function is called.
    """
    print("Orchard Farm Weather Data Collection.")


def new_date(new_row):
    """
    User input today's date function.
    This function checks that the user input and current date are identical.
    It then generates the first two data points for the new data row.
    These are the Year Number and Day of Year.
    """
    print(TERM.clear)
    print("Welcome to Orchard Farm Weather Data Collection.")
    print("")
    while True:
        print("Please enter the date today.")
        print("\x1B[3mFormat: YYYY-MM-DD\x1B[23m")  # Credit 2 in README.md
        date_str = input("Enter today's date here:\n")
        if date_str != datetime.today().date().strftime('%Y-%m-%d'):
            print("Error - incorrect date entered. Restarting...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            new_date(new_row)  # Go back to beginning if date incorrect
            break
        year_num = int(datetime.today().date().strftime('%Y'))  # Year number
        day_num_of_year = int(datetime.now().strftime('%j'))  # Day of year
        new_row.append(year_num)  # Add year number to new row data list
        new_row.append(day_num_of_year)  # Add day of year to new row data list
        return new_row


def check_date(choice):
    """
    This function checks with the spreadsheet.
    It checks to see if there is an entry for today.
    If so, it asks the user if they'd like to delete the row already there.
    """
    day_of_year = int(datetime.now().strftime('%j'))
    year = int(datetime.now().strftime('%Y'))
    todays_entries = DF.loc[(DF['DOY'] == day_of_year) & (DF['YEAR'] == year)]
    if todays_entries.empty:
        pass
    else:
        print("It seems as if there is already an entry for today")
        print("")
        print(todays_entries)
        print("\x1B[3mDOY: Day of Year\x1B[23m")
        print("")
        print("We only keep one line of data per day in our records.")
        print("Do you want to delete the existing entry and start a new one?")
        delete_row = input("Type 'yes' or 'no'.\n")
        if delete_row.lower() == "yes":
            DF.drop(DF.index[-1], inplace=True)  # Credit 1 - See README.md
        elif delete_row.lower() == 'no':
            choice = "no"
            return choice
        else:
            print("Error... input wasn't 'yes' or 'no'. Try again.")
            print("Reloading...")
            time.sleep(2)
            print(TERM.clear)
            title()
            check_date(choice)


def new_weather(new_row, temp, range1, range2, record_num):
    """
    Master function for 3 user inputs
    - Rainfall in mm
    - Lowest temperature today
    - Highest temperature today
    """
    print(TERM.clear)
    title()
    print("")
    while True:
        print(f"{temp} today.")
        print("Please enter a whole number. \x1B[3mExample: 12\x1B[23m")
        try:
            user_data = int(input(f"Enter the {temp} here:\n"))
        except ValueError:
            print("That wasn't a whole number. Please enter a whole number")
            continue
        else:
            while user_data not in range(range1, range2):
                print("A number not in usual range or not integer was typed.")
                print(f"Current UK record = {record_num}")
                print("Please try again.")
                try:
                    user_data = int(input(f"Enter the {temp} here:\n"))
                except ValueError:
                    print("Error...")
            new_row.append(user_data)  # Add new data to new row data list
            break
    return new_row


def check_inputs(new_row):
    """
    This function checks the user inputs for high or low temperatures.
    If low temp is more than the high temp it swaps the values.
    It displays the values that the user has inputted.
    It asks the user whether they want these data points to be stored.
    It then triggers the next function to add values to the spreadsheet.
    Check with user that they want to send inputs to spreadsheet.
    """
    print(TERM.clear)
    title()
    print("")

    low_temp = new_row[3]
    high_temp = new_row[4]

    if low_temp > high_temp:  # Is low temperature more than high temperature?
        print("We've noticed that the low temp is bigger than the high temp.")
        print("So we've swapped these values for you!")
        new_row[3] = high_temp
        new_row[4] = low_temp

    user_input_checks = {
        "Date": datetime.today().date().strftime('%Y-%m-%d'),
        "Rainfall (mm)": new_row[2],
        "Lowest Temperature (°C)": new_row[3],
        "Highest Temperature (°C)": new_row[4]
    }

    print("Would you like these values to be added to the spreadsheet?\n")
    for keys, values in user_input_checks.items():  # Display user inputs"
        print(keys, ':', values)
    print("")
    send_inputs = input("Type 'yes' to send, 'no' to continue to charts.\n")
    if send_inputs.lower() == "yes":
        send_new_row(new_row)
    elif send_inputs.lower() == 'no':
        print("")
    else:
        print("Error... input wasn't 'yes' or 'no'. Try again.")
        print("Reloading...")
        time.sleep(2)
        check_inputs(new_row)


def send_new_row(new_row):
    """
    This function updates the spreadsheet with a new row.
    """
    DF.loc[len(DF)] = new_row  # Credit: Code from sparkbyexmaples.com
    print("Sending data to spreadsheet.")

    SHEET.worksheet('data').update(
        [DF.columns.values.tolist()] +
        DF.values.tolist()
        )

    print("Data successfully added to spreadsheet.")
    time.sleep(1.5)
    print(TERM.clear)


def chart_question(weather_type):
    """
    This function asks the user whether they'd like to see a chart of the data.
    It loops around the input until yes or no is chosen.
    """
    print(f"Shall we see a chart for {weather_type} on this day since 1993?\n")
    chart_answer = input("Please type 'yes' to see chart and 'no' continue.\n")
    while chart_answer.lower() not in ("yes", "no"):
        chart_answer = input("Error. Input wasn't 'yes' or 'no'. Try again.\n")
    if chart_answer.lower() == "yes":
        find_rows(weather_type)


def find_rows(weather_type):
    """
    This function retrieves row information from the dataframe.
    It splits it into the variables we'd like to show on the chart.
    Rainfall, minimum and maximum temperatures.
    It then shows a different chart depending on the weather_type entered.
    """
    print("")

    day_of_year = int(datetime.now().strftime('%j'))
    all_rows = DF.loc[DF['DOY'] == day_of_year]
    yrs = all_rows["YEAR"].tolist()
    rainfall = all_rows["RAINFALL"].tolist()
    min_temp = all_rows["TEMP_MIN"].tolist()
    max_temp = all_rows["TEMP_MAX"].tolist()

    plotext.title(f"Bar Chart of {weather_type.title()} since 1993")
    plotext.xlabel("Year\n")
    plotext.plotsize(100, 30)

    if weather_type == "rainfall":
        plotext.bar(yrs, rainfall, width=2/5)
        plotext.ylabel("Rainfall in mm")

    elif weather_type == "contrasting temperatures":
        plotext.multiple_bar(
            yrs, [max_temp, min_temp],
            label=["max", "min"],
            width=1/5)
        plotext.ylabel("Temperature in °C")

    plotext.show()
    plotext.clear_data()
    print("")


def finish_question():
    """
    This function asks the user whether they have finished with the charts
    Depending on the user input, it directs the user to the function.
    """
    print("")
    print("Have you finished inspecting the charts?")
    finish_answer = input("When you have, please type 'yes' to finish.\n")
    while finish_answer.lower() not in ("yes", "no"):
        finish_answer = input(
            "Error. Input wasn't 'yes' or 'no'. Try again.\n")
    if finish_answer.lower() == "yes":
        pass
    elif finish_answer.lower() == "no":
        print("Enjoy inspecting the charts!")
        time.sleep(3)
        finish_question()


def thank_you():
    """
    Thank you section.
    This is the final stage of the programme.
    """
    plotext.clear_terminal()
    print(TERM.clear)
    print("Thank you for using Orchard Farm Weather Data Collection.")
    print("")
    print("Your data helps us understand the effects of climate change.")
    print("Alongwith helping us with all future crop plans.")
    print("Have a lovely rest of your day, see you tomorrow.")
    print("")


def chart_path():
    """
    The controls the pathway of the chart creation functions.
    """
    chart_question("rainfall")
    time.sleep(1)
    chart_question("contrasting temperatures")
    time.sleep(1)
    finish_question()
    thank_you()


def main():
    """
    This controls the running order of the functions.
    It can change its pathway depending on the user choices through the app.
    """
    new_row = []  # List for new row
    choice = ""  # Variable for check_date
    new_date(new_row)
    if check_date(choice) == "no":
        print(TERM.clear)
        chart_path()
    else:
        new_weather(new_row, "Rainfall in millimeters", 0, 450, "341.4mm")
        new_weather(new_row, "Lowest temperature in °C", -40, 50, "-27.4°C")
        new_weather(new_row, "Highest temperature in °C", -40, 50, "40.3°C")
        check_inputs(new_row)
        title()
        chart_path()


main()
