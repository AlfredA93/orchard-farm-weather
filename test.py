# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import plotext
from datetime import datetime
import pandas as pd

DF = pd.read_csv('orchard_farm_data.csv')

def new_date(new_row):
    """
    User input today's date function.
    """
    while True:
        print("Please enter the date today")
        print("Format: YYYY-MM-DD")
        date_str = input("Enter the date here:\n")
        if date_str != datetime.today().date().strftime('%Y-%m-%d'):    # Is user date entry today?
            print("Error - incorrect date entered. Restarting...\n")
            new_date(new_row)                                           # Go back to beginning if date incorrect
            break
        year_num = int(datetime.today().date().strftime('%Y'))          # Create year number
        day_num_of_year = int(datetime.now().strftime('%j'))            # Create day of year
        new_row.append(year_num)                                        # Add year number to new row data list
        new_row.append(day_num_of_year)                                 # Add day of year to new row data list
        return new_row
    
def new_weather(new_row, temp, range1, range2, record_num):
    """
    Master function for 3 user inputs
    - Rainfall in mm
    - Lowest temperature today
    - Highest temperature today
    """
    print("")
    while True:
        print(f"{temp} today.")
        print("Please enter a whole number. Example: 12")
        try:
            user_data = int(input(f"Enter the {temp} here:\n"))
        except ValueError:
            print("That wasn't a whole number. Please enter a whole number")
            user_data = int(input(f"Enter the {temp} here:\n"))         # If user doesn't enter a number, throws error.
            continue
        else:
            while user_data not in range(range1, range2):               # Checks for excessive input value beyond expected amount.
                print(f"You typed {user_data} this seems unusual: Current UK record = {record_num}")
                print(f'Please try again.')
                try:
                    user_data = int(input(f"Enter the {temp} here:\n"))
                except ValueError:
                    print("That wasn't a whole number. Please enter a whole number") 
                    user_data = int(input(f"Enter the {temp} here:\n"))
            new_row.append(user_data)                                   # Add new data to new row data list               
            break
    return new_row

def check_inputs(new_row):
    """
    Check with user that they want to send inputs to spreadsheet
    """
    user_input_checks = {
        "Date" : datetime.today().date().strftime('%Y-%m-%d'),
        "Rainfall (mm)" : new_row[2],
        "Lowest Temperature (°C)" : new_row[3],
        "Highest Temperature (°C)" : new_row[4]
    }
        
    print("\n")
    print("Would you like the following values to be added to the spreadsheet?\n")
    for keys, values in user_input_checks.items():
        print(keys,':', values)
    send_inputs = input("Please type 'yes' to send and 'no' to restart programme\n")
    if send_inputs.lower() == "yes":
        send_new_row(new_row)
    elif send_inputs.lower() == 'no':
        print("Restarting...")
        main()
    else:
        print("Error... input wasn't 'yes' or 'no'. Try again.")
        check_inputs(new_row)

def send_new_row(new_row):
    """
    Send list of user input data to spreadsheet   
    """
    print("Sending data to spreadsheet...")
    
    print("Successfully sent.\n")
    
def find_rows():
    day_of_year = int(datetime.now().strftime('%j')) 
    all_rows = DF.loc[DF['DOY'] == day_of_year]
    years = all_rows["YEAR"].tolist()
    rainfall = all_rows["RAINFALL"].tolist()
    print(years)
    print(rainfall)
    plotext.scatter(years, rainfall, marker = "braille")
    plotext.title("Scatter Plot of")
    plotext.show()
    
def thank_you():
    print("Thank you for collecting data with Orchard Farm Weather Data Collection.")
    print("This will help with all future crop plans alongwith the understanding of climate change in our area.\n")
    
def main():
    """
    Runs all program functions in correct order
    """
    new_row = []                                                          # List for new row
    new_date(new_row)                                                     # Today's date input
    new_weather(new_row, "Rainfall in millimeters", 0, 450, "341.4mm")    # Rainfall input
    new_weather(new_row, "Lowest temperature in °C", -40, 50, "-27.4°C")  # Min temp input
    new_weather(new_row, "Highest temperature in °C", -40, 50, "40.3°C")  # Max temp input
    check_inputs(new_row)
    find_rows()
    thank_you()
    
print("Welcome to Orchard Farm Weather Data Collection.")
main()
