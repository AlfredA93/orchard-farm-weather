# Orchard Farm Weather Data Collection

## Testing
------

Testing is carried out throughout the development of the project. This is often done before committing the changes to the repository, where the file is kept. However, sometimes, changes are committed to the repository before rigorous testing is applied, to control changes being made. Testing happens immediately after and edits are made where necessary. I have carried out comprehensive testing on the application before and post deployment and have exampled the testing I have carried out post-deployment in the documentation below.

### Input Validation
Every input in the application needs to have input validation, to check the user input is the correct data type and within the range expected for the weather data we are collecting. Below is a table of the requirements that each input need for correct validation. All inputs will loop, often using a `while` loop with `try`, `except` and `else` statements following. If they do not use a `while` loop, an `if`/`elif`/`else` statement(s) is(/are) used in the code instead. 

| Input                      | Data Type Required | Format        | Range Start  | Range End    | 
| :------------------------- | :----------------: | :--------:    | :---------:  | :----------: |
| Date                       | Date String        | YYYY-MM-DD    | Today only   | Today only   |
| Date Check                 | String             | yes or no     |              |              |
| Rainfall                   | Integer            | whole number  | 0            | 450          |
| Low Temperature            | Integer            | whole number  | -40          | 50           |
| High Temperature           | Integer            | whole number  | -40          | 50           |
| Send Data                  | String             | yes or no     | no           | yes          |
| Rainfall Chart Question    | String             | yes or no     | no           | yes          |
| Temperature Chart Question | String             | yes or no     | no           | yes          |
| Finished Question          | String             | yes or no     | no           | yes          |


------

### Examples

I will now go through them one by one to showcase how these validations appear within the Terminal.

- Date
    - This input will only accept the date on which the user is using the application
    - This must be in format YYYY-MM-DD, including the hyphens.
    - If the user enters a date that isn't today, the error will still arise
    

![Character test on Date input](/assets/documentation/testimages.webp/date-test-char.webp)
![Old or future Date on Date input](/assets/documentation/testimages.webp/date-test-otherdate.webp)
![Character in Date Check Question](/assets/documentation/testimages.webp/date-check-test.webp)

- Weather data inputs
    - All weather data inputs must be integers (whole numbers).
    - No characters are allowed.
    - It needs to be within the expected range for 'record-breaking weather', as shown in the table's columns, Range Start and Range End, above.
    - All weather-type inputs use the same function, only the parameters change, hence the consistent layout and error messages arising.
    - In the images below, the red/orange line indicates where a float (decimal) number has been used. The green line indicates where the input is an integer, but it is outside the expected range. The blue line indicates where characters were used.

![Errors on rain input](/assets/documentation/testimages.webp/rain-test-all.webp)
![Errors on low temp](/assets/documentation/testimages.webp/lowtemp-test-all.webp)
![Errors on high temp](/assets/documentation/testimages.webp/hightemp-test-all.webp)

- Weather data inputs - continued.
    - If a user initially inputs an integer outside the expected range, this is caught by an `else` statement, and then with the use of a `while` loop, the user is repeatedly asked for an input until an integer within the correct range is used. This is shown in the second image below this paragraph.

![Out of range, then decimal input](/assets/documentation/testimages.webp/lowtemp-test-range.webp)
![Code](/assets/documentation/testimages.webp/test-code-example.webp)

- String inputs - yes or no answers. 
    - These are often questions asked to the user to govern how the app should progress.
    - These must be character only, either yes or no.
    - Capitals may be used within the yes or no inputs. As shown in the second image below.

![Send Data Error](/assets/documentation/testimages.webp/send-test.webp)
![Capitals on string input](/assets/documentation/testimages.webp/send-test-yes.webp)
![Chart Question Error](/assets/documentation/testimages.webp/chart-qu-test.webp)
![Second Chart Question Error](/assets/documentation/testimages.webp/chart-qu-test-2.webp)
![Final Question character error](/assets/documentation/testimages.webp/finish-test.webp)

### CI PEP8 Python Linter
- I checked all of my Python code through the Code Institute Python Linter, which came back all clear.

![CI python linter pass](/assets/documentation/images.webp/python-linter-clear.webp)