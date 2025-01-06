# Importing all app imports
from prochazka_config_appka import *

## Functions
# Basic Data Box: Calculate quintessential data based on weight and skinfold_sum
def calculate_fat_data():
    weight = fat_data['weight']
    skinfolds_sum = fat_data['skinfolds_sum']
    fat_data['bmr'] = round(weight * 24.2, 2)
    fat_data['cal_main_lvl'] = round(float(fat_data['bmr'] * 1.2), 2)
    todays_data_list.clear()
    todays_data_list.append(str(todays_date_str))
    todays_data_list.append(str(weight))
    todays_data_list.append(str(skinfolds_sum))

## Main Window Variables
#Storing Today's Date & Time
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

## Main Window Lists / Dictionaries
# storing picked_user's weight and fat data & ensuing calculations
fat_data = {} # This Dictionary Stores:
"""
1 Weight (in kg)
2 Skinfolds Sum (in mm)
3 Basal Metabbolic Rate
4 Calorie Maintenance Level
"""

# storing user day data to be later inserted into Google Sheets
todays_data_list = []