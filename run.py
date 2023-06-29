# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import plotext
from datetime import datetime
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('orchard_farm_weather_data')

weather_data = SHEET.worksheet('data')

all_data = weather_data.get_all_values()

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
    print("\n")
    while True:
        print(f"{temp} today.")
        print("Please enter a whole number. Example: 12")
        try:
            user_data = int(input(f"Enter the {temp} here:\n"))
        except ValueError:
            print("That wasn't a number. Please enter a number")        # If user doesn't enter a number, throws error.
            continue
        else:
            while user_data not in range(range1, range2):               # Checks for excessive input value beyond expected amount.
                print(f"You typed {user_data} this seems unusual: Current UK record = {record_num}")
                print(f'Please try again.')
                user_data = int(input(f"Enter today's {temp} here:\n"))    
            user_data = round(user_data, 1)
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
    print("Would you like the following values to be added to the spreadsheet?")
    #print(f"\n {user_input_checks}")
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

def duplicate_find():
    """
    Function to get all weather data for the same day of year. This brings back a list of cell and row numbers.
    The function then converts to string. Strips it back into the row number.
    It then retrieves whole row data for the matching cells.
    It then prints out the weather data to the user.
    """
    day_of_year = datetime.now().strftime('%j') 
    duplicates = SHEET.worksheet('data').findall(f"{day_of_year}")
    row_summary = []
    for row in range(len(duplicates)):
        string = str(duplicates[row])
        string_parts = string.split(" ")
        string_row = string_parts[1]
        string_row_num = string_row[1:]
        string_row_2 = string_row_num.split("C")
        row_num = string_row_2[0]
        all_row_values = SHEET.worksheet('data').row_values(row_num)
        row_summary.append(all_row_values)
    print(row_summary)
    # historical_data = {}
    # keys_list = []
    # values_list = []
    # for data in range(len(row_summary)):
    #     first_row = row_summary[data]
    #     keys = first_row[0]
    #     keys_list.append(keys)
    #     values = first_row[2:5]
    #     values_list.append(values)
    # print(keys_list)
    # print(values_list)
    for data in range(len(row_summary)):
        print(f"Year: {row_summary[data][0]}. Rainfall: {row_summary[data][2]}mm Min Temp: {row_summary[data][3]}°C Max Temp: {row_summary[data][4]}°C")

def send_new_row(new_row):
    """
    Send list of user input data to spreadsheet   
    """
    print("Sending data to spreadsheet...")
    worksheet_to_change = SHEET.worksheet("data")
    worksheet_to_change.append_row(new_row)
    print("Successfully sent.")
    
def thank_you():
    print("Thank you for collecting data with Orchard Farm Weather Data Collection.")
    print("This will help with all future crop plans alongwith the understanding of climate change in our area.")
    
def main():
    """
    Runs all program functions in correct order
    """
    new_row = []                                                          # List for new row
    new_date(new_row)                                                     # Today's date input
    new_weather(new_row, "Rainfall in millimeters", 0, 450, "341.4mm")             # Rainfall input
    new_weather(new_row, "Lowest temperature in °C", -40, 50, "-27.4°C")  # Min temp input
    new_weather(new_row, "Highest temperature in °C", -40, 50, "40.3°C")  # Max temp input
    check_inputs(new_row)
    #send_new_row(new_row)
    duplicate_find()
    thank_you()
    
print("\n")    
print("Welcome to Orchard Farm Weather Data Collection.")
duplicate_find()
main()
    
    
    
# Functions below for use later
    
    
def new_worksheet_row():
    """
    Sends user input data to worksheet if it has been validated correct.
    """
    
def sort_worksheet():
    """
    Sort worksheet to create a dataset in contrast to corresponding 
    same day in previous years.
    """
    
def display_chart():
    """
    Display a chart to the user comparing weather data with all 
    past data on the same day of each year.
    """




    # """
    # User input rainfall data for the day.
    # """     
    # while True:
    #     print("Please enter the millimeters of rain today")
    #     print("All numbers will be converted to decimals upto 1 decimal place")
    #     print("Example input: 1.23456 Example output: 1.2")

    #     try:
    #         rain_num = float(input("Enter the amount of rain here:\n"))
    #     except ValueError:
    #         print(f"That wasn't a number. Please enter a number")
    #         continue
    #     else:
    #         while rain_num not in range(0, 450): # Checks for excessive input value beyond expected amount.
    #             print(f'You typed {rain_num} mm, this seems unusual: highest recorded UK rainfall in any 24hr period is 341.4mm')
    #             print(f'Please try again.')
    #             rain_num = float(input("Enter the amount of rain here:\n"))    
    #         rain_num = round(rain_num, 1)
    #         new_row_data.append(rain_num) # Add rainfall number to new row data list
    #         print(new_row_data)                
    #         break
    # """
    # User input minimum temperature data for the day.
    # """
    # while True:
    #     print("Please enter the lowest temperature of rain today")
    #     print("All numbers will be converted to decimals upto 1 decimal place")
    #     print("Example input: 1.23456 Example output: 1.2")
    #     try:
    #         temp_min_num = float(input("Enter the lowest temperature here:\n"))
    #     except ValueError:
    #         print(f"That wasn't a number. Please enter a number")
    #         continue
    #     else:
    #         while temp_min_num not in range(-40, 50): # Checks for excessive input value beyond expected amount.
    #             print("You typed {temp_min_num} this seems unusual: coldest day on UK records = -27.2 'C")
    #             print(f'Please try again.')
    #             temp_min_num = float(input("Enter the lowest temperature here:\n"))    
    #         temp_min_num = round(temp_min_num, 1)
    #         new_row_data.append(temp_min_num) # Add min temperature number to new row data list
    #         print(new_row_data)                
    #         break
    # """
    # User input maximum temperature data for the day.
    # """    
    # while True:
    #     print("Please enter the maximum temperature of rain today")
    #     print("All numbers will be converted to decimals upto 1 decimal place")
    #     print("Example input: 1.23456 Example output: 1.2")
    #     try:
    #         temp_max_num = float(input("Enter the highest temperature here:\n"))
    #     except ValueError:
    #         print(f"That wasn't a number. Please enter a number")
    #         continue
    #     else:
    #         while temp_max_num not in range(-40, 50): # Checks for excessive input value beyond expected amount.
    #             print("You typed {temp_max_num} this seems unusual: hottest day on UK records = 40.3 'C")
    #             print(f'Please try again.')
    #             temp_max_num = float(input("Enter the highest temperature here:\n"))    
    #         temp_max_num = round(temp_max_num, 1)
    #         new_row_data.append(temp_max_num) # Add max temperature number to new row data list
    #         print(new_row_data)                
    #         break