import random
import datetime
import warnings
import pandas as pd
import numpy as np

def create_golf_df(num_balls,variability,swing_speed_included,clubs,shot_type_included):
    '''Save excel file for driving range schedule'''
    swing_speed = ['100%','100%','100%','100%','100%','100%','80%','60%','40%']
    shot_type = ['Hook','Pull','Fade','Straight','Straight','Straight','Straight','Straight','Straight','Draw','Push','Slice']
    club_list= []
    reps = []
    shot_type_list = []
    swing_speed_list = []
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
    
    for i in range(len(club_list)):
            swing_speed_list.append(random.choice(swing_speed))
            shot_type_list.append(random.choice(shot_type))
    
    swing_speed_list = pd.DataFrame({"Swing Speeds":swing_speed_list})
    shot_type_list = pd.DataFrame({"Shot Types":shot_type_list})
    df = pd.DataFrame({"Club": club_list, "Hits": reps})
    
    if swing_speed_included == True:
        df = pd.concat([df,swing_speed_list],axis=1)
    
    if shot_type_included == True:
         df = pd.concat([df,shot_type_list],axis=1)

    return df