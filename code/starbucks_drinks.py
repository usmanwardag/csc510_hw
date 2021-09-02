# -*- coding: utf-8 -*-
import pandas as pd
dataSet = pd.read_csv(r'../data/starbucks-menu-nutrition-drinks.csv')    

#Finding drink with lowest calorie
def find_low_calorie_drink(dataSet):
    drink = dataSet[dataSet.Calories == dataSet.Calories.min()]
    return drink[['Name','Calories']]

#High protein drinks
def find_high_protein_drink(dataSet):
    drink =   dataSet['Protein']>=4
    drink = dataSet[drink]
    return drink[['Name','Protein']]

#High carb drinks
def find_high_carb_drink(dataSet):
    drink=dataSet['Carb. (g)']>=30
    drink = dataSet[drink]
    return drink[['Name','Carb. (g)']]

print('Lowest Calorie Drink')
print(find_low_calorie_drink(dataSet))
print('High Protein Content Drink')
print(find_high_protein_drink(dataSet))
print('High Carb Drink')
print(find_high_carb_drink(dataSet))


