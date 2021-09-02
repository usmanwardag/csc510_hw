import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal 

class TestDrinks(unittest.TestCase):
    
    def test_lowest_calorie(self):
        
        def __init__(self):
            super(TestDrinks, self).__init__()
            
        #Assume
        test_data = pd.read_csv('test-data.csv')
        data = {'Name':'Drink 5', 'Calories':0, 'Fat (g)':0, 'Carb. (g)':0, 'Fiber (g)':0 , 'Protein':5, 'Sodium':0}
        expected = pd.DataFrame(data)
        
        #Assert
        assert_frame_equal(expected,find_low_calorie_drink(test_data))
        
    def test_high_protein(self):
        
        #Assume
        test_data = pd.read_csv('test-data.csv')
        data = {'Name':['Drink 1,Drink 5'], 'Calories':[45,0], 'Fat (g)':[0,0], 'Carb. (g)':[11,0], 'Fiber (g)':[0,0] , 'Protein':[5,5], 'Sodium':[10,0]}
        expected = pd.DataFrame(data)
        
        #Assert
        assert_frame_equal(expected,find_high_protein_drink(test_data))
        
    def test_high_carb(self):
        
        #Assume
        test_data = pd.read_csv('test-data.csv')
        data = {'Name':'Drink 3', 'Calories':60, 'Fat (g)':0, 'Carb. (g)':34, 'Fiber (g)':1 , 'Protein':1, 'Sodium':10}
        expected = pd.DataFrame(data)
        
        #Assert
        assert_frame_equal(expected, find_high_carb_drink(test_data))
        
if __name__ == "__main__":
   unittest.main()
   

