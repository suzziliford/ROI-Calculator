import math

class Calculator:

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.cash_on_cash = 0
        self.the_numbers = []

    def get_income(self):
        self.rental = int(input("Enter monthly rent: ")) #instance attribute
        self.laundry = int(input("Enter monthly laundry: "))
        self.storage = int(input("Enter monthly storage: "))
        self.misc = int(input("Enter monthly misc: "))
        x = sum([self.rental, self.laundry, self.storage, self.misc])
        self.total_income = str(x)
        print ("Total income = " + self.total_income)
        # calculate(total_income)
        return self.total_income
        
    def get_expenses(self):
        self.tax = int(input("Enter monthly tax: "))
        self.insurance = int(input("Enter monthly insurance: "))
        self.electric = int(input("Enter montly electric: "))
        self.water = int(input("Enter montly water: "))
        self.sewer = int(input("Enter montly sewer: "))
        self.garbage = int(input("Enter montly garbage: "))
        self.gas = int(input("Enter montly gas: "))
        self.hoa = int(input("Enter montly hoa: "))
        self.lawn_snow = int(input("Enter montly lawn_snow: "))
        self.vacancy = int(input("Enter montly vacancy: "))
        self.repairs = int(input("Enter montly repairs: "))
        self.capex = int(input("Enter montly capex: "))
        self.management = int(input("Enter montly property management: "))
        self.mortgage = int(input("Enter montly mortgage: "))

        y = sum([self.tax, self.insurance, self.electric, self.water, self.sewer, 
        self.garbage, self.gas, self.hoa, self.lawn_snow, self.vacancy, self.repairs, self.capex, self.management, self.mortgage])
        self.total_expenses = str(y)
        print ("Total Expenses = " + self.total_expenses)
        return self.total_expenses
        

    def get_cash_on_cash(self):
        self.down_payment = int(input("Enter down payment: "))
        self.closing_costs = int(input("Enter closing costs: "))
        self.rehab_budget = int(input("Enter rehab budget: "))
        self.misc = int(input("Enter any misc costs: "))

        z = sum([self.down_payment, self.closing_costs, self.rehab_budget, self.misc])
        self.total_investment = str(z)
        print ("Total investments = " + self.total_investment)
        return self.total_investment

    def calculate(self):      
        cashflow = (int(self.total_income) - int(self.total_expenses))*12
        return_on_investment = ((float(cashflow))/int(self.total_investment)*100)
        print(return_on_investment)
        return return_on_investment

def run_script():

    roi = Calculator() #instantiating a new object
    print(roi)
    entering_data = True

    while True:
            ammend = int(input("Which field would you like to ammend? Choose \n'1' for add income, \n'2' for add expense, \n'3' for add purchase costs, \n'4' for roi calculations and breakdown, \n'5' edit data \n'6' quit \nEnter number:  "))
            while ammend not in {'1', '2', '3', '4', '5', '6'}:
                ammend = input('Not valid. Please choose 1, 2, 3, 4, 5, or 6: ')
                if ammend == '1':
                    roi.get_income()
                elif ammend == '2':
                    roi.get_expenses()
                elif ammend == '3':
                    roi.get_cash_on_cash()
                    roi.calculate()
                elif ammend == '4':
                    entering_data == False
                    print("ROI is %")
                    roi.calculate('total_income', 'total_expenses', 'total_investment')
                elif ammend == '6':
                    break
                elif ammend == '5':
                    edit = int(input("Which field would you like to edit? Choose 1 for income, 2 for expense, 3 for purchase costs"))
                    if ammend == '1':
                        roi.get_income()
                    elif ammend == '2':
                        roi.get_expenses()
                    elif ammend == '3':
                        roi.get_cash_on_cash()
                else:
                    print("Please choose a number from the list")

run_script()                    


#              While True:
# 59	        if self.income == 0:
# 60	            print ("Gather Income.")
# 61	            roi.income()
# 62	        elif roi.expenses == 0:
# 63	            print ("Gather Expenses.")
# 64	            roi.expenses()
# 65	        elif roi.cash_on_cash == 0:
# 66	            print ("Gather Purchase Costs")
# 67	            roi.cash_on_cash()


        #this is where the user is directed to the different functions
        #to gather data
        #will create a while loop to bring them back 




#Questions: How am I defining the objects in this case, seeing as their is only one user at a time?
# As they are a single user, whose data doesn't need to be stored, couldn't I just collect their data in a single funtion and 
# punch it out? Am I missing the goal of the exercise? Do I need to add more functionality to make it meet 
# the assignment's criteria?

#Question: How should I break down the process into different objects? Does the way I'm doing it right now seem sensible?

#Question: How should I orient my dictionary situation for easy return access? ie list of dictionaries, list of lists, dictionary of lists?



