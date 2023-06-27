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
        print("Please enter the date today")
        print("Format: YYYY-MM-DD")
        date_str = input("Enter the date here:\n")
        while date_str != datetime.today().date().strftime('%Y-%m-%d'):
            print("Error. Date not today. Please try again and input today's date\n")
            return new_weather_data()
       
def new_rain_data():
    """
    User input rainfall data for the day.
    """
        print("Please enter the millimeters of rain today")
        rain_str = input("Enter the amount of rain here:\n")
        while int(rain_str) not in range(0, 1000):
            print(f'You typed {rain_str} this seems unusual, please try again.')
            return new_rain_data()
        return int(rain_str)
            
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
    new_rain_data()
    new_min_temps()
    new_max_temps()
    
print("Welcome to Orchard Farm Weather Data Collection.")

collect_data()