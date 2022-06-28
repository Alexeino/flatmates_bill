
class Bill:
    """
    Object that contains about a bill, such as total amount and 
    period of the bill.
    """
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

        self.display()

    def display(self):
        print("Total Amount - ",self.amount)
        print("Billing Period - ",self.period)

class Flatmate:

    """ Creates a flatmate person which displays name, period and amount 
    he/she has to pay.
     """

    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self,bill,other_flatmate):
        """Logic for bill share calculation..."""
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
    