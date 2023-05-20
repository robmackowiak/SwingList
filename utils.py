import random
import datetime
import warnings
import pandas as pd

def define_range_variables():
    num_balls = int(input("Enter the number of balls: "))
    variability = input("Enter the variability of random (Low/Medium/High): ")
    clubs = ['SW','GW','PW','9-Iron','8-Iron','7-Iron','6-Iron','5-Iron','Hybrid','Driver']
    return num_balls,variability,clubs

def create_golf_df(balls,variability_lvl,range_clubs):
    '''Save excel file for driving range schedule'''
    random.shuffle(range_clubs)

    if variability_lvl == "Low":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(range_clubs)
            else:
                club = random.choice([c for c in range_clubs if c != items[-1]])
            value = random.randint(5, 6)
            if sum(values) + value <= balls:
                items.append(club)
                values.append(value)
            if sum(values) == balls:
                break
            if sum(values) + value > balls:
                items.append(club)
                values.append(balls-sum(values))
    elif variability_lvl == "Medium":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(range_clubs)
            else:
                club = random.choice([c for c in range_clubs if c != items[-1]])
            value = random.randint(3, 4)
            if sum(values) + value <= balls:
                items.append(club)
                values.append(value)
            if sum(values) == balls:
                break
            if sum(values) + value > balls:
                items.append(club)
                values.append(balls-sum(values))
    elif variability_lvl == "High":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(range_clubs)
            else:
                club = random.choice([c for c in range_clubs if c != items[-1]])
            value = random.randint(1, 3)
            if sum(values) + value <= balls:
                items.append(club)
                values.append(value)
            if sum(values) + value > balls:
                items.append(club)
                values.append(balls-sum(values))
            if sum(values) == balls:
                break
    else:
        print("Invalid variability_lvl.")

    # Create the pandas dataframe
    df = pd.DataFrame({"Club": items, "Hits": values})
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