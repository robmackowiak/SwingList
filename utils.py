import random
import datetime
import warnings
import pandas as pd
import numpy as np

def define_range_variables():
    num_balls = int(input("Enter the number of balls: "))
    variability = input("Enter the variability of random (Low/Medium/High): ")
    swing_speed_included = input("Include variable swing speeds? (Y/N): ")
    clubs = ['SW','GW','PW','9-Iron','8-Iron','7-Iron','6-Iron','5-Iron','Hybrid','Driver']
    swing_speed = ['100%','100%','100%','100%','100%','100%','80%','60%','40%']
    return num_balls,variability,swing_speed_included,clubs,swing_speed

def create_golf_df(num_balls,variability,swing_speed_included,clubs,swing_speed):
    '''Save excel file for driving range schedule'''
    club_list= []
    reps = []
    cum_reps = 0
    while cum_reps<num_balls:
        club_list.append(random.choice(clubs))
        if variability == "Low":
            reps.append(random.choice(range(5,7)))
        elif variability == "Medium":
            reps.append(random.choice(range(3,5)))
        elif variability == "High":
            reps.append(random.choice(range(1,3)))
        else:
            print("Variability Syntax Error.")
            break
        cum_reps = np.sum(reps)
    
    df = pd.DataFrame({"Club": club_list, "Hits": reps})
    if swing_speed_included == "Y":
        swing_speed_list = []
        for i in range(len(club_list)):
            swing_speed_list.append(random.choice(swing_speed))
        # Create the pandas dataframe
        swing_speed_df = pd.DataFrame({"Swing Speeds": swing_speed_list})
        df = pd.concat(df,swing_speed_df)
    
    return df

def save_file(df):
    # generate the current date and time as a string
    now = datetime.datetime.now().date().strftime('%Y-%m-%d')
    filename = f'SwingList_{now}.xlsx'
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    writer.save()
    print("...SwingList Created..")
    print("...SwingList Saved to Working Directory..")
    warnings.filterwarnings("ignore")
    return