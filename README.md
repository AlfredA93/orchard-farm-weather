# Orchard Farm Weather Data Collection

Orchard Farm Weather Data Collection is an app for employees of Orchard Farm, Suffolk UK, to input weather data that they have collected for each day. This app then inputs this data into a spreadsheet and brings back a chart of the data, so the user can see the changes in the weather since 1993. The applications aim is to collect data for future use and display comparative historical data with the aim of atmospheric insight - to make the user aware of weather changes and how climate change is affecting the area in Suffolk. You can visit the site [here](https://orchard-farm-weather-9b130ffa81fb.herokuapp.com/).

![am i responsive](/assets/documentation/images.webp/amiresponsive.webp)

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


### Thank you Page
- The thank you page is the last part of the application, where it thanks the user for its use of the application and tells the user how to enter new data, if necessary.

![thank you message](/assets/documentation/images.webp/thankyou-message.webp)

### Input Validation

- All inputs have input validators, which ask the user for either for set words (yes or no), or an integer (whole number). 
- Please see [Testing](assets/documentation//TESTING.md) page for more detailed explanation of this.

### **Potential Future Features**
- Add a menu system at the front of the application, so users can decide whether they wish to just view charts or enter data
- Add more charts showcasing varying values.

## Testing
------
## **CI PEP8 Python Linter**
### **Input Validatation Tests**
- Please see [Testing](assets/documentation//TESTING.md) page
### Bugs

- Problem 1:
    - *Solution 1:`code`*

- Problem 2:
    - *Solution 2:* 
    ![Description](photo-source)

- Problem 3:
    - *Solution 3:*

- Problem 4:
    - *Solution 4:*
    ![photo]()

- Problem 5:
    - *Solution 5:

- Problem 6: 
    - *Solution 6:*
### Unfixed Bugs

- None

## Mistakes
------

Mistake
- *Solution:*

![photo]()

## Deployment
------

![photo]()
![photo]()

## Design - Flow Chart
------
![flowchart](/assets/documentation/images.webp/flowchart.webp)

### Python Libraries Used and Why?
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
