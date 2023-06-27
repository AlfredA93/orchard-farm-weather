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
        
        print("Please enter the millimeters of rain today")
        rain_str = input("Enter the amount of rain here:\n")

        print("Please enter the minimum temperature (in celcius) today")
        temps_str = input("Enter minimum temperature here:\n")
        break
    
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
    
print(new_weather_data())