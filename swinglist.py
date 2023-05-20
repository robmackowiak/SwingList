'''Create schedule for driving range session'''
from utils import define_range_variables,create_golf_df,save_file

def export_swinglist():
    num_balls,variability,clubs = define_range_variables()
    golf_range_df = create_golf_df(num_balls,variability,clubs)
    save_file(golf_range_df)