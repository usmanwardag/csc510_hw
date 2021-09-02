# -*- coding: utf-8 -*-
import os
import pandas as pd

dataset = pd.read_csv(f'{os.getcwd()}/data/starbucks-menu-nutrition-drinks.csv')    

#Finding drink with lowest calorie
def find_low_calorie_drink():
    drink = dataset[dataset.Calories == dataset.Calories.min()]
    return drink[['Name','Calories']]

#High protein drinks
def find_high_protein_drink():
    drink = dataset['Protein']>=4
    drink = dataset[drink]
    return drink[['Name','Protein']]

#High carb drinks
def find_high_carb_drink():
    drink = dataset['Carb. (g)']>=30
    drink = dataset[drink]
    return drink[['Name','Carb. (g)']]



