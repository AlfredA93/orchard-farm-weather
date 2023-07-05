# Orchard Farm Weather Data Collection

## Testing
------

### Input Validation
Every input in the application needs to have input validation, to check the user input is the correct data type and within the range expected for the weather data we are collecting. Below is a table of the requirements that each input need for correct validation.

| Input                      | Data Type Required | Format        | Range Start  | Range Finish | 
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

I will now go through one by one to showcase how these validations appear within the Terminal.

- Date
    - This will only accept the date on which the user is using the application
    - This must be in format YYYY-MM-DD, including the hyphens.
    - If the user enters a date which isn't today, the error will still arise
    

![](/assets/documentation/testimages.webp/date-test-char.webp)
![](/assets/documentation/testimages.webp/date-test-otherdate.webp)
![](/assets/documentation/testimages.webp/date-check-test.webp)

- Weather data inputs
    - All weather data inputs must be integers (whole numbers).
    - No characters are allowed.
    - It needs to be within the expected range for 'record breaking weather', as shown in the table Range columns above.
    - In the images below, the red/orange line indicates where a float (decimal) number has been used. The green line indicates where the input is a integer, but it is outside the expected range. The blue line indicates where characters were used.

![](/assets/documentation/testimages.webp/rain-test-all.webp)
![](/assets/documentation/testimages.webp/lowtemp-test-all.webp)
![](/assets/documentation/testimages.webp/hightemp-test-all.webp)

- If a user initially inputs an integer outside the expected range, this is caught by an `else` statement, and then with the use of a `while` loop, the user is repeatedly asked for an input until an integer within the correct range is used.

![](/assets/documentation/testimages.webp/lowtemp-test-range.webp)

- String inputs - yes or no answers

![](/assets/documentation/testimages.webp/send-test.webp)
![](/assets/documentation/testimages.webp/send-test-yes.webp)
![](/assets/documentation/testimages.webp/chart-qu-test.webp)
![](/assets/documentation/testimages.webp/chart-qu-test-2.webp)
![](/assets/documentation/testimages.webp/finish-test.webp)