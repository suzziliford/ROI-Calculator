import math

class Calculator:

    def __init__(self):
        # self.income = 0
        # self.expenses = 0
        # self.cash_flow = 0
        # self.cash_on_cash = 0
        # self.the_numbers = []
        self.d_income = {}
        self.d_expenses = {}
        self.d_investments = {}

    def get_income(self):
        self.rental = int(input("Enter monthly rent: ")) #instance attribute
        self.laundry = int(input("Enter monthly laundry: "))
        self.storage = int(input("Enter monthly storage: "))
        self.misc = int(input("Enter monthly misc: "))
        x = sum([self.rental, self.laundry, self.storage, self.misc])
        self.total_income = str(x)
        self.d_income = {'rent': self.rental, 'laundry' : self.laundry, 'storage' : self.storage, 'misc' : self.misc}
        for k,v in self.d_income.items():
            print (f"{k.title()}: {v}")
        print ("Total monthly income = $" + self.total_income)
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

        self.d_expenses = {'Tax' : self.tax, 'Insurance' : self.insurance, 'Electric' : self.electric, 'Water' : self.water, 'Sewer' : self.sewer, 
        'Garbage' : self.garbage, 'Gas' : self.gas, 'Hoa' : self.hoa, 'Lawn and Snow' : self.lawn_snow, 'Vacancy' : self.vacancy, 
        'Repairs' : self.repairs, 'Capex' : self.capex, 'Management' : self.management, 'Mortgage' : self.mortgage}
        y = sum([self.tax, self.insurance, self.electric, self.water, self.sewer, 
        self.garbage, self.gas, self.hoa, self.lawn_snow, self.vacancy, self.repairs, self.capex, self.management, self.mortgage])
        self.total_expenses = str(y)
        for k, v in self.d_expenses.items():
            print (f"{k.title()}: {v}")
        # print(self.d_expenses)
        print ("Total Monthly Expenses = $" + self.total_expenses)
        return self.total_expenses
        

    def get_cash_on_cash(self):
        self.down_payment = int(input("Enter down payment: "))
        self.closing_costs = int(input("Enter closing costs: "))
        self.rehab_budget = int(input("Enter rehab budget: "))
        self.misc = int(input("Enter any misc costs: "))

        self.d_investments = {'Down Payment' : self.down_payment, 'Closing Costs' : self.closing_costs, 'Rehabilitation' : self.rehab_budget, 'Miscellaneous' : self.misc}
        z = sum([self.down_payment, self.closing_costs, self.rehab_budget, self.misc])
        self.total_investment = str(z)
        for k, v in self.d_investments.items():
            print(f"{k.title()}: {v}")
        # print(self.d_investments)
        print ("Total investments = $" + self.total_investment)
        return self.total_investment


    def edit_numbers(self):
        editing_input = True
        which_field = input("Which figures would you like to edit? Type: income, expenses, investment. Or to return to the main menu, type: menu. \nType your response: ")        
        if which_field == 'income':
            print(self.d_income)
            to_remove1 = input("Which value would you like to change?: ")
            if to_remove1 in self.d_income:
                new_value1 = input("Enter new value: ")
                self.d_income[to_remove1] = new_value1
                print("Value has been updated")
                print (self.d_income)

        elif which_field == 'expenses':
            print(self.d_expenses)
            to_remove2 = input("Which value would you like to change?: ")
            if to_remove2 in self.d_expenses:
                new_value2 = input("Enter new value: ")
                self.d_expenses[to_remove2] = new_value2
                print("Value has been updated")
                print (self.d_expenses)

        elif which_field == 'investment':
            print(self.d_investments)
            to_remove3 = input("Which value would you like to change?: ")
            if to_remove3 in self.d_investments:
                new_value3 = input ("Enter new value: ")
                self.d_investments[to_remove3] = new_value3
                print("Value has been updated")
                print(self.d_investments)
                return self.d_investments

        elif which_field == 'menu':
            editing_input = False

        else:
            which_field = input ("Input not recognized, please type: income, expenses, investment, or menu")

    def calculate(self):      
        cashflow = (int(self.total_income) - int(self.total_expenses))*12
        self.return_on_investment = ((float(cashflow))/int(self.total_investment)*100)
        print("Return on Investment = " + str(self.return_on_investment) + "%")
        return self.return_on_investment

def run_script():

    roi = Calculator() #instantiating a new object
    # print(roi)
    entering_data = True

    while True:
            ammend = (input("Choose \n'1' to add income, \n'2' for add expense, \n'3' for add purchase costs, \n'4' for roi calculations and breakdown, \n'5' edit data, \n'6' quit \nEnter number:  "))
            while ammend not in ('1', '2', '3', '4', '5', '6'):
                ammend = input("Not valid. Please choose \n'1' to add income, \n'2' for add expense, \n'3' for add purchase costs, \n'4' for roi calculations and breakdown, \n'5' edit data \n'6' quit \nEnter number:  ")
                if ammend == '1':
                    roi.get_income()
                elif ammend == '2':
                    roi.get_expenses()
                elif ammend == '3':
                    roi.get_cash_on_cash()
                    roi.calculate()
                elif ammend == '4':
                    print(f"ROI is %{roi.return_on_investment}")
                elif ammend == '5':
                    roi.edit_numbers()
                    roi.calculate()
                elif ammend == '6':
                    entering_data == False
                    print("Thank you for using this ROI calculator")
                    break
                else:
                    print("Please choose a number from the list")

run_script()                    




