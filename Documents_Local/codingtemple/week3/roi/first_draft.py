
class Calculator():  
    def __init__(self, username):
        self.username = username 
        self.data = ()

    

class Income():
    
    def collate_income():
        rent = int(input("Before any expenses, how much will the property acrue in rent each month?: "))
        
        laundry = input("Are you planning on providing 'for fee' laundry services? y/n?: ")
        if laundry == 'y':
            laundry_income = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
            False
        else: 
            print("Please press y/n")
        
        storage = input("Will there be any 'for fee' storage facility on the property? y/n?: ")
        if storage == 'y':
            storage_income = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
            False
        else: 
            print("Please press y/n")

        misc = input("Will the property acrue any miscellaneous income? y/n: ")
        if misc == 'y':
            misc_income = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
            False
        else: 
            print("Please press y/n")

        monthly_income = sum(rent, laundry_income, storage_income, misc)
        monthly_income = Calculator(monthly_income)
        

    def collate_expenses():
        tax = int(input("What is the properties monthly tax fee?: "))
        insurance = int(input("What are the properties montly insurance premium?: "))
        print("Will the rental free be inclusive of utilites?")
        electricity = ("Is rental fee inclusive of electricity? y/n: ")
        if electricity == 'y':
                electricity_expense = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
                False
        else: 
                print("Please press y/n")
        water = ("Is rental fee inclusive of water? y/n: ")
        if water == 'y':
                water_expense = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
                False
        else: 
                print("Please press y/n")
        sewerage = ("Is rental fee inclusive of sewerage? y/n: ")
        if sewerage == 'y':
                sewerage_expense = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
                False
        else: 
                print("Please press y/n")
        garbage = ("Is rental fee inclusive of garbage? y/n: ")
        if garbage == 'y':
                garbage_expense = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
                False
        else: 
                print("Please press y/n")
        gas = ("Is rental fee inclusive of gas? y/n: ")
        if gas == 'y':
                gas_expense = int(input("How much monthly income do you predict the laundry services will create?: "))        
        elif 'n':
                False
        else: 
                print("Please press y/n")

        hoa = int(input("Will the property incur home owner association fees? If so, how much per month?: "))
        lawn_snow = int(input("Will you be hiring someone to provide lawn/snow care? If so what is the monthly charge?: "))
        vacancy = int(input("How much will you be putting aside each month for a vacancy fund? (contingency fund for unpredicted periods of vacancy): "))
        repairs = int(input("Predicted monthly cost for any repairs required on the property?: "))
        capex = int(input("How much will you be putting aside for capital expenditure? (contingency funds for big repair jobs etc): "))
        poperty_managment = int(input("Will you be hiring an agent to manage the property? What is their monthly charge?: "))
        mortgage = int(input("What are the monthly mortgage payments?: "))

        expenses = sum[tax, insurance, electricity_expense, water_expense, sewerage_expense, garbage_expense, gas_expense, hoa, 
        lawn_snow, vacancy, repairs, capex, poperty_managment, mortgage]


# class Income():
#     def __init__(self):
#         self.rent = int(input("How much is rent per month?: "))
#         self.laundry = int(input("How much in laundry?: "))
#         self.storage = int(input("Do you make any income from storage on the property? If so: How much?: "))
#         self.total = self.rent + self.laundry

    def get_income():
        pass


        

    

    def view_input():
        pass

class Investment():
    pass

    def __init__(self) -> None:
        pass


def run_calculator():
        roi = Income()

        print("Firstly, let's gather the total of your monthly income on the property.")
        
        user1.collate_income()

        
        
        
        
        
        




    # storage = input("Is there an option for charging for storage on the property? Y/N)

    # calc = Calculator()
    # calc.get_income()
    # print(calc.income.total)
run_calculator()

# class User():
#     pass

#     def create_new_user():
#         pass

#     def log_in():
#         pass

#     def log_out():
#         pass