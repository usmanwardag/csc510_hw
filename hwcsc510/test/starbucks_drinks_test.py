from hwcsc510.code import starbucks_drinks as sbd

class TestDrinks():
    
    def __init__(self):
        self.test_lowest_calorie()
        self.test_high_protein()
        self.test_high_carb()

    def test_lowest_calorie(self):
        lowest_cal = sbd.find_low_calorie_drink().iloc[0]['Name']
        assert lowest_cal == 'Cool Lime Starbucks Refreshers', 'Lowest cal method error'

    def test_high_protein(self):
        highest_protein = sbd.find_high_protein_drink().iloc[0]['Name']
        assert highest_protein == 'Violet Drink', 'Highest protein method error'
        
    def test_high_carb(self):
        highest_carb = sbd.find_high_carb_drink().iloc[0]['Name']
        assert highest_carb == 'Bottled Black Mango', 'Highest carb method error'
        
if __name__ == "__main__":
    test_object = TestDrinks()

