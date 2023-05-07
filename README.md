# Golf Hit List Generator

~~ Function still in-development but useful as a start ~~

This script generates a hit list for golfers that specifies the clubs and number of hits for each club during a practice session. The hit list is generated randomly based on the user inputs of number of balls to hit and variability level (Low, Medium, High).

A lower variability is representative of less variable practice in the driving range session, and a higher variability increased the level of variable practice. 

## Prerequisites
This script requires the following Python packages to be installed:
- pandas
- random
- datetime

## How to use
1. Change clubs based on availability & interest.
2. Enter the number of balls to hit when prompted.
3. Enter the variability level when prompted (Low/Medium/High).
4. The script will generate a hit list as a pandas dataframe and save it to an Excel file named "HitList_yyyy-mm-dd.xlsx", where "yyyy-mm-dd" represents the current date.
5. The Excel file will be saved in the same directory as the script.

## Function
The `get_hitList()` function takes three arguments: `num_balls`, `variability`, and `clubs`. 
- `num_balls`: an integer representing the number of balls to hit during the practice session.
- `variability`: a string representing the variability level of the hit list. Valid options are "Low", "Medium", and "High".
- `clubs`: a list of strings representing the clubs to use during the practice session.
