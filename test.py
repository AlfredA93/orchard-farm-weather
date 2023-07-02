# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import plotext
from datetime import datetime
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
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

term = blessed.Terminal()


def new_date(new_row):
    """
    User input today's date function.
    """
    print(term.clear)
    print("Welcome to Orchard Farm Weather Data Collection.")
    print("")
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


def check_date(choice):
    day_of_year = int(datetime.now().strftime('%j')) 
    year = int(datetime.now().strftime('%Y')) 
    todays_entries = DF.loc[(DF['DOY'] == day_of_year) & (DF['YEAR'] == year)]
    if todays_entries.empty:
        pass
    else:
        print("It seems as if there is an entry for today already in the spreadsheet")
        print("")
        print(todays_entries)
        print("")
        print("We only keep one line of data per day in our records.")
        print("Would you like to delete the entry above and start a new data record?")
        delete_row = input("Type 'yes' or 'no'.\n")
        if delete_row.lower() == "yes":
            DF.drop(DF.index[-1], inplace=True) # Credit 1 - See README.md
        elif delete_row.lower() == 'no':
            thank_you()
            choice ="no"
            return choice
        else:
            print("Error... input wasn't 'yes' or 'no'. Try again.")
            check_date(choice)
    
    
def new_weather(new_row, temp, range1, range2, record_num):
    """
    Master function for 3 user inputs
    - Rainfall in mm
    - Lowest temperature today
    - Highest temperature today
    """
    print(term.clear)
    print("Orchard Farm Weather Data Collection.")
    print("")
    while True:
        print(f"{temp} today.")
        print("Please enter a whole number. Example: 12")
        try:
            user_data = int(input(f"Enter the {temp} here:\n"))
        except ValueError:
            print("That wasn't a whole number. Please enter a whole number") # If user doesn't enter a number, throws error.
            continue
        else:
            while user_data not in range(range1, range2):               # Checks for excessive input value beyond expected amount.
                print(f"You typed {user_data} this seems unusual: Current UK record = {record_num}")
                print(f'Please try again.')
                try:
                    user_data = int(input(f"Enter the {temp} here:\n"))
                except ValueError:
                    print("That wasn't a whole number. Please enter a whole number") 
            new_row.append(user_data)                                   # Add new data to new row data list               
            break
    return new_row

def check_inputs(new_row, dont_send):
    """
    Check with user that they want to send inputs to spreadsheet
    """
    print(term.clear)
    print("Orchard Farm Weather Data Collection.")
    print("")
    user_input_checks = {
        "Date" : datetime.today().date().strftime('%Y-%m-%d'),
        "Rainfall (mm)" : new_row[2],
        "Lowest Temperature (°C)" : new_row[3],
        "Highest Temperature (°C)" : new_row[4]
    }
    
    print("Would you like the following values to be added to the spreadsheet?\n")
    for keys, values in user_input_checks.items():
        print(keys,':', values)
    print("")
    send_inputs = input("Please type 'yes' to send and 'no' to finish.\n")
    if send_inputs.lower() == "yes":
        send_new_row(new_row)
    elif send_inputs.lower() == 'no':
        dont_send = "no"
        return dont_send
    else:
        print("Error... input wasn't 'yes' or 'no'. Try again.")
        check_inputs(new_row)

def send_new_row(new_row):
    """
    Send list of user input data to spreadsheet   
    """
    DF.loc[len(DF)] = new_row # Credit: Code from sparkbyexmaples.com pandas article. URL in README.md
    print("Sending data to spreadsheet.")
    SHEET.worksheet('data').update([DF.columns.values.tolist()] + DF.values.tolist()) # Credit:Code from gspread with pandas documentation. URL in README.md
    print("Data successfully added to spreadsheet.")
    
def chart_question(weather_type):
    print("")
    print(f"Would you like to see a chart for {weather_type} on this day since 1993?\n")
    chart_answer = input("Please type 'yes' to see chart and 'no' continue.\n")
    while chart_answer.lower() not in ("yes", "no"):
        chart_answer = input("Error... input wasn't 'yes' or 'no'. Try again.")
    if chart_answer.lower() == "yes":
        find_rows(weather_type)
    
    
def find_rows(weather_type):
    print(term.clear)
    print("Orchard Farm Weather Data Collection.")
    print("")
    day_of_year = int(datetime.now().strftime('%j')) 
    all_rows = DF.loc[DF['DOY'] == day_of_year] # Get all rows from column DOY (Day Of Year)
    
    if weather_type == "rainfall":
        col_name = "RAINFALL"
    elif weather_type == "minimum temperature":
        col_name = "TEMP_MIN"
    elif weather_type == "maximum temperature":
        col_name = "TEMP_MAX"
    
    years = all_rows["YEAR"].tolist() # Convert dataframe values to list
    rainfall = all_rows[f"{col_name}"].tolist() 
    

    plotext.bar(years, rainfall, marker = "sd")
    plotext.title(f"Bar Chart of {weather_type} of since 1993")
    plotext.xlabel("Year\n")
    plotext.ylabel(f"{weather_type} in mm")
    plotext.plotsize(100,30)
    plotext.show()
    plotext.clear_data()
    
    
def thank_you():
    print("Thank you for collecting data with Orchard Farm Weather Data Collection.")
    print("This will help with all future crop plans alongwith the understanding of climate change in our area.\n")
    
def main():
    """
    Runs all program functions in correct order
    """
    new_row = []  # List for new row
    choice = "" 
    dont_send = ""
    new_date(new_row)                                                     # Today's date input
    #check_date(choice)
    if check_date(choice) == "no":
        pass
    else:    
        new_weather(new_row, "Rainfall in millimeters", 0, 450, "341.4mm")    # Rainfall input
        new_weather(new_row, "Lowest temperature in °C", -40, 50, "-27.4°C")  # Min temp input
        new_weather(new_row, "Highest temperature in °C", -40, 50, "40.3°C")  # Max temp input
        check_inputs(new_row, dont_send)
        if check_inputs(dont_send) == "no":
            thank_you()
            pass
        chart_question("rainfall")
        chart_question("minimum temperature")
        chart_question("maximum temperature")
        thank_you()
main()


# Still to implement
#
# - if column YEAR == %Y and column DOY == %j :
# 	print(”There is an entry for today already in our database”)
# 	input(“Do you want to overwrite the data for today?”)
# 		if user_input == “yes”:
# 		#drop method
# 			data = pd.read_csv("my file")
# 			data = data.drop(data.index[-1])
# 			print(data.tail())
# 		else if user_input == “no”:
# 			thank_you()

# -float(round(input),0.1) on user inputs? Check with range, add range step of 0.1? 
# Putting round function to 0.1 and adding 0.1 step to range may allow it to work together. 


# - Add function to ask whether they want to see rainfall chart
# - Add function to ask whether they want to see min temp chart
# - Add function to ask whether they want to see max temp chart
