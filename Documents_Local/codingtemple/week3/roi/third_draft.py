import math

class Calculator:

    def __init__(self):
        self.d_income = ()
        self.d_expenses = ()
        self.d_investments = ()

    def get_income(self):
        self.rental = int(input("Enter monthly rent: ")) 
        self.laundry = int(input("Enter monthly laundry: "))
        self.storage = int(input("Enter monthly storage: "))
        self.misc = int(input("Enter monthly misc: "))
        x = sum([self.rental, self.laundry, self.storage, self.misc])
        self.total_income = str(x)
        self.d_income = {'rent': self.rental, 'laundry' : self.laundry, 'storage' : self.storage, 'misc' : self.misc}
        # for k,v in self.d_income.items():
        #     print (f"{k.title()}: {v}")
        print ("="*29)
        print ("Total monthly income = $" + self.total_income)
        print ("="*29)
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
        # for k, v in self.d_expenses.items():
        #     print (f"{k.title()}: {v}")
        # print(self.d_expenses)
        print ("="*29)
        print ("Total Monthly Expenses = $" + self.total_expenses)
        print ("="*29)
        return self.total_expenses
        

    def get_cash_on_cash(self):
        self.down_payment = int(input("Enter down payment: "))
        self.closing_costs = int(input("Enter closing costs: "))
        self.rehab_budget = int(input("Enter rehab budget: "))
        self.misc = int(input("Enter any misc costs: "))

        self.d_investments = {'Down Payment' : self.down_payment, 'Closing Costs' : self.closing_costs, 'Rehabilitation' : self.rehab_budget, 'Miscellaneous' : self.misc}
        z = sum([self.down_payment, self.closing_costs, self.rehab_budget, self.misc])
        self.total_investment = str(z)
        # for k, v in self.d_investments.items():
        #     print(f"{k.title()}: {v}")
        # print(self.d_investments)
        print ("="*29)
        print ("Total investments = $" + self.total_investment)
        print ("="*29)
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
                print ("="*29)
                print("Value has been updated")
                print ("="*29)
                print (self.d_income)
                print ("="*29)

        elif which_field == 'expenses':
            print(self.d_expenses)
            to_remove2 = input("Which value would you like to change?: ")
            if to_remove2 in self.d_expenses:
                new_value2 = input("Enter new value: ")
                self.d_expenses[to_remove2] = new_value2
                print ("="*29)
                print("Value has been updated")
                print (self.d_expenses)
                print ("="*29)

        elif which_field == 'investment':
            print(self.d_investments)
            to_remove3 = input("Which value would you like to change?: ")
            if to_remove3 in self.d_investments:
                new_value3 = input ("Enter new value: ")
                self.d_investments[to_remove3] = new_value3
                print ("="*29)
                print("Value has been updated")
                print(self.d_investments)
                print ("="*29)
                return self.d_investments

        elif which_field == 'menu':
            editing_input = False

        else:
            which_field = input ("Input not recognized, please type: income, expenses, investment, or menu")

    def calculate(self):      
        cashflow = (int(self.total_income) - int(self.total_expenses))*12
        self.return_on_investment = ((float(cashflow))/int(self.total_investment)*100)
        print("Return on Investment = " + str(self.return_on_investment) + "%")
        print ("="*29)
        return self.return_on_investment

def run_script():

    roi = Calculator() #instantiating a new object
    # print(roi)
    # entering_data = True
    menu_choice = input()

    while True:
            # menu_choice = int(input("Menu. \nType: \n'1' for add income, \n'2' for roi calculations and breakdown, \n'3' edit data \n'4' quit \nEnter number:  "))
            if menu_choice !='':
                menu_choice = input("Menu. \nType: \n'1' for add income, \n'2' for roi calculations and breakdown, \n'3' edit data \n'4' quit \nEnter number:  ")
                if menu_choice == '1':
                    roi.get_income()
                    roi.get_expenses()
                    roi.get_cash_on_cash()
                    roi.calculate()
                elif menu_choice == '2':
                    print ("="*29)
                    # print("ROI is %")
                    roi.calculate()
                    print ("="*29)
                elif menu_choice == '3':
                    roi.edit_numbers()
                    roi.calculate()
                elif menu_choice == '4':
                    print('Thank you for using the ROI calculator')
                    # entering_data == False
                    break
                else:
                    print("Please choose a number from the list")

run_script()                    




