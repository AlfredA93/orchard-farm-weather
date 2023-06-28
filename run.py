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

def new_weather_data():
    """
    User input new daily weather data.
    """
    while True:
        new_row_data = [] # Set up an empty list for user values to be inputted
        print("Please enter the date today")
        print("Format: YYYY-MM-DD")
        date_str = input("Enter the date here:\n")
        while date_str != datetime.today().date().strftime('%Y-%m-%d'): # Is user date entry today?
            print("Error - incorrect value entered. Please try again and input today's date.\n")
            return new_weather_data() # Go back to beginning if date incorrect
        year_num = int(datetime.today().date().strftime('%Y')) # Create year number
        day_num_of_year = int(datetime.now().strftime('%j')) # Create day of year
        new_row_data.append(year_num) # Add year number to new row data list
        new_row_data.append(day_num_of_year) # Add day of year to new row data list
        print(new_row_data)
        break
    """
    User input rainfall data for the day.
    """     
    while True:
        print("Please enter the millimeters of rain today")
        print("All numbers will be converted to decimals upto 1 decimal place")
        print("Example input: 1.23456 Example output: 1.2")

        try:
            rain_num = float(input("Enter the amount of rain here:\n"))
        except ValueError:
            print(f"That wasn't a number. Please enter a number")
            continue
        else:
            while rain_num not in range(0, 450): # Checks for excessive input value beyond expected amount.
                print(f'You typed {rain_num} mm, this seems unusual: highest recorded UK rainfall in any 24hr period is 341.4mm')
                print(f'Please try again.')
                rain_num = float(input("Enter the amount of rain here:\n"))    
            rain_num = round(rain_num, 1)
            new_row_data.append(rain_num) # Add rainfall number to new row data list
            print(new_row_data)                
            break
    """
    User input minimum temperature data for the day.
    """
    while True:
        print("Please enter the lowest temperature of rain today")
        print("All numbers will be converted to decimals upto 1 decimal place")
        print("Example input: 1.23456 Example output: 1.2")
        try:
            temp_min_num = float(input("Enter the lowest temperature here:\n"))
        except ValueError:
            print(f"That wasn't a number. Please enter a number")
            continue
        else:
            while temp_min_num not in range(-45, 45): # Checks for excessive input value beyond expected amount.
                print("You typed {temp_min_num} this seems unusual: coldest day on UK records = -27.2 'C")
                print(f'Please try again.')
                temp_min_num = float(input("Enter the lowest temperature here:\n"))    
            temp_min_num = round(temp_min_num, 1)
            new_row_data.append(temp_min_num) # Add rainfall number to new row data list
            print(new_row_data)                
            break
        
            
def new_min_temps():
    """
    User input minimum temperature for the day.
    """
    print("Please enter the minimum temperature (in celcius) today")
    temps_str = input("Enter minimum temperature here:\n")
        
def new_max_temps():
    """
    User input maximum temperature for the day.
    """
    print("Please enter the maximum temperature (in celcius) today")
    max_temps_str = input("Enter maximum temperature here:\n")
        
    
def check_data():
    """
    Validate user inputted data with required data types.
    """
    
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

def collect_data():
    """
    Runs all program functions in correct order
    """
    new_weather_data()
    #new_rain_data()
    #new_min_temps()
    #new_max_temps()
    
print("Welcome to Orchard Farm Weather Data Collection.")

collect_data()