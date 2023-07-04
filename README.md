# Orchard Farm Weather Data Collection

Orchard Farm Weather Data Collection is an app for employees of Orchard Farm, Suffolk UK, to input weather data that they have collected for each day. This app then inputs this data into a spreadsheet and brings back a chart of the data, so the user can see the changes in the weather since 1993. The applications aim is to collect data for future use and display comparative historical data with the aim of atmospheric insight - to make the user aware of weather changes and how climate change is affecting the area in Suffolk. You can visit the site [here](https://orchard-farm-weather-9b130ffa81fb.herokuapp.com/).

![am i responsive](/assets/documentation/images.webp/amiresponsive.webp)

## Design and Inspiration
------
- I was inspired to make a weather data collection app due to living and working on a farm with my parents during the pandemic. I learnt so much during my time there and was interested in how each day they wrote down the rainfall each day by hand in their diary. I wanted to create an application that could span generations and the data be safe and accessible from anywhere with an internet connection.
- Below is the flowchart I created as a guide when I was first visualising how the code would be represented.

![flowchart](/assets/documentation/images.webp/flowchart.webp)

## How to use
------
Orchard Farm Weather Data Collection is a terminal based data input application. The steps are simple to follow and the user is guided through the prompts in terminal. Through the apps progression, the user will go through the following:
- Enter Today's Date
- Enter Rainfall in millimeters on this date
- Enter Lowest Temperature in Celcius on this date
- Enter the Highest Temperature in Celcius on this date
- Rainfall Chart
- Comparative Temperature Chart

## Features 
------

### Date Entry
- Here the user can enter todays date.

![date](/assets/documentation/images.webp/feature-date.webp)
- The app will then check with the spreadsheet where the data is stored whether there has been an entry for today already. The app only stores one data row per day.

![date check](/assets/documentation/images.webp/feature-datecheck.webp)
- The user can input the millimeters of rainfall as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

![rainfall](/assets/documentation/images.webp/feature-rain.webp)
- The user can input the the lowest temperature that day as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

![low temperatures](/assets/documentation/images.webp/feature-lowtemp.webp)
- The user can input the highest temperature that day as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

![high temperatures](/assets/documentation/images.webp/feature-hightemp.webp)
- The user will see the values they inputed to verify whether they would like these data values added to the spreadsheet records.

![values](/assets/documentation/images.webp/feature-values.webp)
- If the user accidently enters the highest and lowest numbers in the wrong input boxes, the app detects this and swaps the values over. In the three images below we can see how this happens.

![low temp swap](/assets/documentation/images.webp/feature-lowtemp-swap.webp)

![high temp swap](/assets/documentation/images.webp/feature-hightemp-swap.webp)

![values swap](/assets/documentation/images.webp/feature-values-swap.webp)

- Once the user enters yes, the data will be sent to the spreadsheet and data added as a new row. If the user enters no, then the app will not send the data to the spreadsheet and will progress the user to the next stage of the process - charts.

![send data](/assets/documentation/images.webp/feature-send.webp)


### Chart Analysis
- The user is asked whether they'd like to view a chart of the rainfall data on this day compared with each year since 1993.

![chart question](/assets/documentation/images.webp/chart-question.webp)
- If they select yes, they then see the rainfall for that date.  If they select no, then the app progresses to the next stage without displaying the chart.

![rainfall chart](/assets/documentation/images.webp/chart-rain.webp)
- They are then asked if they want to view a chart comparing the min and max temperatures since 1993.

![single question](/assets/documentation/images.webp/chart-question-one.webp)
- If they select yes, the chart is presented. If they select no, then the app progresses to the next stage without displaying the chart.

![temp chart](/assets/documentation/images.webp/chart-temps.webp)
- The final part of the chart analysis if when the user is asked whether they are finished viewing the charts. If the user selects yes, then it clears the terminal and the thank you message is displayed. If the user selects no, then an encouraging message is displayed. If the user enters anything else, an error message appears. Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

![finish question](/assets/documentation/images.webp/finish-question.webp)


### Thank You
- The thank you page is the last part of the application, where it thanks the user for its use of the application and tells the user how to enter new data, if necessary.

![thank you message](/assets/documentation/images.webp/thankyou-message.webp)

### Input Validation

- All inputs have input validators, which ask the user for either for set words (yes or no), or an integer (whole number). 
- Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

### Potential Future Features
- Add a menu system at the front of the application, so users can decide whether they wish to just view charts or enter data
- Add more charts showcasing varying values.

## Testing
------
## CI PEP8 Python Linter
- I checked all of my python code through the Code Institute Python Linter, which came back all clear.

![CI python linter pass](/assets/documentation/images.webp/python-linter-clear.webp)

### Input Validatation Tests
- Please see [Testing](assets/documentation//TESTING.md) page
### Bugs

- **Problem 1**: Attempting to print a dictionary with a for loop however the values weren’t being printed out in the terminal and the code was running without errors.
- *Solution 1:`items()` was missing from the end of the for loop.*
- **Problem 2**: When validating the user input for the weather data. If user inputted a value over the range over the accepted values, causing the function to catch the input in the `else` code; then on the second input attempt entered an float number, it causes the app to crash due to trying to convert float into int. 
- *Solution 2: Add a `try`/`except` loop to the `while not in range()` part of the function. Adding a `valueError` to the except; to catch any `valueError` responses that then processes a new user input. I then changed the float to an integer, as catching float errors was causing more bugs to occur than catching integers* 
- **Problem 3**: Google Sheets API read limit of 300 requests per minute exceeding. Due to the loop sending individual requests for each row value, instead of collecting the information in one batch call.

![API bug warning](/assets/documentation/images.webp/bug-api-warning.webp)

![API bug code](/assets/documentation/images.webp/bug-api-code.webp)

- *Solution 3: Use Pandas library, to collect all the data we need in one API call in the beginning, then we can manipulate the data easily within a pandas dataframe on the local system. Write funtion to a new one using pandas library functions*
- **Problem 4**: After updating my requirements.txt using a virtual environment, a warning message was arising in the terminal during the app running, which wasn't happening beforehand when testing. The warning message was about future deprecation of code syntax on a function used in gspread.
- *Solution 4: Change the version of gspread used in the requirements.txt file from 5.10.0 to 5.9.0 - as was used in all testing*

![GSpread Version bug](/assets/documentation/images.webp/bug-version.webp)

### Unfixed Bugs

- None

## Mistakes
------

Mistake: I made a few of my git commits too long, by a few characters. 
- *Solution: Commit more often, with less changes to cover in a commit message* 

## Deployment
------
I deployed the app using the website Heroku, which hosts web based applications. Once you have an account with Heroku, follow these are the steps for deployment - 
- Create a new app 
![create new app](/assets/documentation/images.webp/deployment-new.webp)
- Name the app
![Name the app](/assets/documentation/images.webp/deployment-name.webp)
- Connect the app to Github and find the repository where the code is stored and click connect.
![Github connect](/assets/documentation/images.webp/deployment-github.webp)
- Go to the Settings Tab within the Heroku app. Find the Config Vars and add `PORT` in the key and `8000` in the value. Then for CREDS in the `key` and add the credentials that are copied from the .json credentials file in the IDE. I have blacked mine out, as each set of credentials are unique and private.
![Settings tab, creds](/assets/documentation/images.webp/deployment-creds.webp)
- Add the buildpacks in this order: Python, NodeJS.
![buildpacks](/assets/documentation/images.webp/deployment-buildpacks.webp)
- Go back to the Deploy tab and select automatically update Heroku whenever a new edit is received by GitHub.
![deploy](/assets/documentation/images.webp/deployment-deploy.webp)

## Data Model
------
I didn't use a OOP model such as class for this project; as the structure was quite straight forward and implementing this would not suitable for this project. 

If future features are added, for example a Menu System, where the user could choose various types of chart or whether they wish to only input data and not visualise charts, then I would implement a class based model, however at this moment of writing, I would need to learn more Python skills to implement these extra features. 

## Python Libraries Used and Why?
------
-
-
-
-

## Credits 
------
### **Code**

![Description](photo-source)

- [Description](link)

![Description](photo-source)

- [Description](link)

### Technology
- https://tiny-img.com/webp/ webp converter for README images

### Helpsheets and Learning Resources

- 

- My mentor Alex was absolutely brilliant in his support throughout this project. Continually suggesting ways to continue development of the project and helping to find suitable libraries for a terminal based application.

- [Description](link)
- [Description](link)
- [Description](link)
- [Description](link)
- [Description](link)
- [Description](link)
