# Orchard Farm Weather Data Collection

Orchard Farm Weather Data Collection is an app for employees of Orchard Farm, Suffolk UK. It is used to input weather data that they have collected for each day. This app then inputs this data into a spreadsheet and brings back a chart of the data, so the user can see the changes in the weather that date since 1993. The application aims to collect data for future use and display comparative historical data with the aim of atmospheric insight - to make the user aware of weather changes and how climate change is affecting the area in Suffolk. You can visit the site [here](https://orchard-farm-weather-9b130ffa81fb.herokuapp.com/).

![am i responsive](/assets/documentation/images.webp/amiresponsive.webp)

## Design and Inspiration
------
- I was inspired to make a weather data collection app from living and working on a farm that my parents managed. I learned so much during my 3 years there between 2019-2022. I was interested in how each day they wrote down the rainfall by hand in their diary each day. I wanted to create an application that could span generations and the data be safe and accessible from anywhere with an internet connection.
- Below is the flowchart I created as a guide when I was first visualising how the code would be represented.

![flowchart](/assets/documentation/images.webp/flowchart.webp)

## How to use
------
Orchard Farm Weather Data Collection is a terminal based data input application. The steps are simple to follow and the user is guided through the prompts in the terminal. Through the progression of the app, the user will go through the following:
- Enter Today's Date
- Enter Rainfall in millimeters on this date
- Enter the Lowest Temperature in Celcius on this date
- Enter the Highest Temperature in Celcius on this date
- Rainfall Chart
- Comparative Temperature Chart

## Features 
------

### Date Entry
- Here the user can enter today's date.

![date](/assets/documentation/images.webp/feature-date.webp)
- The app will then check with the spreadsheet where the data is stored whether there has been an entry for today already. The app only stores one data row per day.

![date check](/assets/documentation/images.webp/feature-datecheck.webp)
- The user can input the millimeters of rainfall as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for a more detailed explanation of this.
### Weather Data Inputs
![rainfall](/assets/documentation/images.webp/feature-rain.webp)
- The user can input the lowest temperature that day as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for a more detailed explanation of this.

![low temperatures](/assets/documentation/images.webp/feature-lowtemp.webp)
- The user can input the highest temperature that day as a whole number. Any float numbers (decimal place numbers) or any inputs containing characters will be rejected and the user will be asked for a whole number. Please see [Testing](assets/documentation//TESTING.md) page for a more detailed explanation of this.

![high temperatures](/assets/documentation/images.webp/feature-hightemp.webp)
- The user will see the values they have entered to verify whether they would like these data values added to the spreadsheet records.
### Input Evaluation
![values](/assets/documentation/images.webp/feature-values.webp)
- If the user accidentally enters the highest and lowest numbers in the wrong input boxes, the app detects this and swaps the values over. In the three images below we can see how this happens.

![low temp swap](/assets/documentation/images.webp/feature-lowtemp-swap.webp)

![high temp swap](/assets/documentation/images.webp/feature-hightemp-swap.webp)

![values swap](/assets/documentation/images.webp/feature-values-swap.webp)
### Spreadsheet Update
- Once the user enters yes, the data will be sent to the spreadsheet, then data added as a new row. If the user enters no, then the app will not send the data to the spreadsheet and will progress the user to the next stage of the process - charts.

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
- The final part of the chart analysis is when the user is asked whether they are finished viewing the charts. If the user selects yes, then it clears the terminal and the thank you message is displayed. If the user selects no, then an encouraging message is displayed. If the user enters anything else, an error message appears. Please see [Testing](assets/documentation//TESTING.md) page for a more detailed explanation of this.

![finish question](/assets/documentation/images.webp/finish-question.webp)


### Thank You
- The thank you page is the last part of the application, where it thanks the user for its use of the application and tells the user how to enter new data, if necessary.

![thank you message](/assets/documentation/images.webp/thankyou-message.webp)

### Input Validation

- All inputs have input validators, which ask the user for either of the set words (yes or no), or an integer (whole number). 
- Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

### Potential Future Features
- Add a menu system at the front of the application, so users can decide whether they wish to just view charts or enter data
- Add more charts showcasing varying values.

## Testing
------
### CI PEP8 Python Linter
- I checked all of my Python code through the Code Institute Python Linter, which came back all clear.

![CI python linter pass](/assets/documentation/images.webp/python-linter-clear.webp)

------
### For Manual Testing details, visit [Testing](assets/documentation//TESTING.md) page.
------

### Bugs

- **Problem 1**: Attempting to print a dictionary with a `for` loop however the values weren’t being printed out in the terminal and the codes running without errors.
- *Solution 1:`items()` was missing from the end of the for loop*
- **Problem 2**: When validating the user input for the weather data. If the user inputted a value over the range of the accepted values, causing the function to catch the input in the `else` code; then on the second input attempt entered a float number, it causes the app to crash due to trying to convert float into an integer. 
- ***Solution 2***: *Add a `try`/`except` loop to the `while not in range()` part of the function. Adding a `valueError` to the except; to catch any `valueError` responses that then process a new user input. I then changed the float to an integer, as catching float errors was causing more bugs to occur than catching integers* 
- **Problem 3**: Google Sheets API read limit of 300 requests per minute exceeding. Due to the loop sending individual requests for each row value, instead of collecting the information in one batch call.

![API bug warning](/assets/documentation/images.webp/bug-api-warning.webp)

![API bug code](/assets/documentation/images.webp/bug-api-code.webp)

- ***Solution 3***: *Use Pandas library, to collect all the data we need in one API call in the beginning, then we can manipulate the data easily within a Pandas data frame on the local system. Rewrite the function to a new one using pandas library functions*
- **Problem 4**: After updating my requirements.txt using a virtual environment, a warning message was arising in the terminal during the app running, which wasn't happening beforehand when testing. The warning message was about the future deprecation of code syntax on a function used in gspread.
- ***Solution 4***: *Change the version of gspread used in the requirements.txt file from 5.10.0 to 5.9.0 - as was used in all testing*

![GSpread Version bug](/assets/documentation/images.webp/bug-version.webp)

### Unfixed Bugs

- None

## Mistakes
------

Mistake: I made a few of my git commits too long, by a few characters. 
- *Solution: Commit more often, with fewer changes to cover in a commit message* 

## Deployment
------
I deployed the app using the website Heroku, which hosts web-based applications. Once you have an account with Heroku, follow these steps for deployment - 
- Create a new app 
![create new app](/assets/documentation/images.webp/deployment-new.webp)
- Name the app
![Name the app](/assets/documentation/images.webp/deployment-name.webp)
- Connect the app to GitHub and find the repository where the code is stored and click connect.
![Github connect](/assets/documentation/images.webp/deployment-github.webp)
- Go to the Settings Tab within the Heroku app. Find the Config Vars and add `PORT` in the key and `8000` in the value. Then for CREDS in the `key` and add the credentials that are copied from the .json credentials file in the IDE. I have blacked mine out, as each set of credentials is unique and private.
![Settings tab, creds](/assets/documentation/images.webp/deployment-creds.webp)
- Add the buildpacks in this order: Python, NodeJS.
![buildpacks](/assets/documentation/images.webp/deployment-buildpacks.webp)
- Go back to the Deploy tab and select automatic deploys, so that whenever a new edit is received by GitHub, Heroku also updates the application. Once this has been clicked. Then click the deploy branch button at the bottom and await for the domain URL to be generated.
![deploy](/assets/documentation/images.webp/deployment-deploy.webp)
- We now have a deployed web application!

## Data Model
------
I didn't use an OOP (object-oriented programming) model, such as using classes, for this project; the structure was quite straightforward, and implementing this would not be suitable for this project. 

If future features are added, for example, a Menu System, where the user could choose various types of charts or whether they wish to only input data and not visualise charts, then I would implement a class-based model, however, at this moment of writing, I would need to learn more Python skills to implement these extra features. 

## Python Libraries Used and Why?
------
- `gspread`: I used gspread to access Google spreadsheets, where the data is being stored for this application. It is a library with useful data manipulation functions and allows us to access Google Sheets.
- `google-auth`: I used the Google Auth library to handle the Credentials for the API calls between the application and google sheets.
- `pandas`: I used pandas to create a data frame within the application, pandas, this solved a bug I had where I was making too many API calls to Google Sheets. With Pandas, I could make 1 API call and put all the data into one data frame to later manipulate and then send 1 more API call later to update the spreadsheet accordingly. 
- `plotext`: I used plotext to plot charts in my application. This library allows developers to plot charts within the terminal itself. Which was perfect for this application.
- `blessed`: I used blessed to control terminal functions, i.e. to clear the Terminal for each new function call. This allows a simple and clean-looking terminal space for the user.
- `time`: I used time functions from the inbuild Python library to delay some function calls within the application. For example, when the user enters an input that causes an error, the application prints the reason why and then pauses for a few seconds before performing the function again. It enhances a good user experience.
- `datetime`: I used datetime library to access the date for the instance of when the user is using the application. It is used for input validation and data manipulation.

## Credits 
------
### **Code**
1. Code Institute for the deployment terminal templates.

2. Historical Weather Data came from [NASA's Weather and Energy Data](https://power.larc.nasa.gov/data-access-viewer/) website.

3. [Italics in print statements](https://python-forum.io/thread-27264.html)

4. [Select rows from a dataframe](https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values)

5. [Append data to Pandas Dataframe](https://sparkbyexamples.com/pandas/how-to-append-row-to-pandas-dataframe/?expand_article=1)

6. [Delete row in dataframe](https://stackoverflow.com/questions/26921651/how-to-delete-the-last-row-of-data-of-a-pandas-dataframe)

7. [UK Weather Records](https://en.wikipedia.org/wiki/United_Kingdom_weather_records)

### Helpsheets and Learning Resources

- My mentor Alex was absolutely brilliant in his support throughout this project. Continually suggesting ways to continue the development of the project and helping to find suitable libraries for a terminal based application.

- I researched various libraries a lot for this project. I learned so much from the brilliant documentation online. Below are the links for the main sources of learning for this project.

- [Try, Except, Else explainer](https://www.101computing.net/number-only/)
- [Gspread documentation](https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Plotext documentation](https://pypi.org/project/plotext/)
- [Plotext explainer](https://www.youtube.com/watch?v=9NSo6hQRqqc&t=215s)
- [Looping through a dictionary](https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp)
- [Using datetime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
- [Converting date to number](https://www.geeksforgeeks.org/python-convert-day-number-to-date-in-particular-year/)
- [Python sleep attribute](https://realpython.com/python-sleep/)
- [If Pandas data frame is empty](https://stackoverflow.com/questions/36543606/python-pandas-check-if-dataframe-is-not-empty)
- [Markdown tables](https://www.codecademy.com/resources/docs/markdown/tables)

### Technology
- [Tiny-img](https://tiny-img.com/webp/) webp image converter. Used for README image conversion.