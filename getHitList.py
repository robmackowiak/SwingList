import pandas as pd
import random
import datetime

num_balls = int(input("Enter the number of balls: "))
variability = input("Enter the variability of random (Low/Medium/High): ")
clubs = ['SW','GW','PW','9-Iron','8-Iron','7-Iron','6-Iron','5-Iron','Hybrid','Driver']

def get_hitList(num_balls,variability,clubs):
    random.shuffle(clubs)

    if variability == "Low":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(clubs)
            else:
                club = random.choice([c for c in clubs if c != items[-1]])
            value = random.randint(4, 5)
            if sum(values) + value <= num_balls:
                items.append(club)
                values.append(value)
            if sum(values) + value > num_balls:
                items.append(club)
                values.append(num_balls-sum(values))
            if sum(values) == num_balls:
                break
    elif variability == "Medium":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(clubs)
            else:
                club = random.choice([c for c in clubs if c != items[-1]])
            value = random.randint(2, 3)
            if sum(values) + value <= num_balls:
                items.append(club)
                values.append(value)
            if sum(values) + value > num_balls:
                items.append(club)
                values.append(num_balls-sum(values))
            if sum(values) == num_balls:
                break
    elif variability == "High":
        items = []
        values = []
        while True:
            if len(values) == 0:
                club = random.choice(clubs)
            else:
                club = random.choice([c for c in clubs if c != items[-1]])
            value = random.randint(1, 2)
            if sum(values) + value <= num_balls:
                items.append(club)
                values.append(value)
            if sum(values) + value > num_balls:
                items.append(club)
                values.append(num_balls-sum(values))
            if sum(values) == num_balls:
                break
    else:
        print("Invalid variability.")

    # Create the pandas dataframe
    df = pd.DataFrame({"Club": items, "Hits": values})
    
    # generate the current date and time as a string
    now = datetime.datetime.now().date().strftime('%Y-%m-%d')
    filename = f'HitList_{now}.xlsx'
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()

    return

get_hitList(num_balls,variability,clubs)