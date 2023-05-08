# Swing List: A Golf Driving Range Practice Tool

[@RobMackowiak](https://twitter.com/RobMackowiak) - May 2023

~~ Still in-development, more motor learning integration coming, but useful as a start ~~

This basic script generates a driving range practice session for golfers that specifies the clubs and number of hits for each club. The goal of the Swing List is to follow motor learning principles to produce a more useful practice session than constant, blocked practice. The schedule is created based on the user inputs of number of balls to hit and variability level (Low, Medium, High). Clubs can be altered within the script.

A higher variability is representative of less blocked practice in the Swing List, more pronounced switching between clubs, with fewer hits at each club. 

## Prerequisites
This script requires the following Python packages to be installed:
- pandas
- random
- datetime

## How to use
1. Change clubs within script based on availability & interest.
2. Enter the number of balls to hit when prompted.
3. Enter the variability level when prompted (Low/Medium/High).
4. The script will generate a Hit List as a pandas dataframe and save it to an Excel file named "SwingList_yyyy-mm-dd.xlsx", where "yyyy-mm-dd" represents the current date.
5. The Excel file will be saved in the same directory as the script.

## Function
The `get_SwingList()` function takes three arguments: `num_balls`, `variability`, and `clubs`. 
- `num_balls`: an integer representing the number of balls to hit during the practice session.
- `variability`: a string representing the variability level of the hit list. Valid options are "Low", "Medium", and "High".
- `clubs`: a list of strings representing the clubs to use during the practice session.
