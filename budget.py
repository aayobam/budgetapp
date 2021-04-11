asterics = "*" * 20
class Budget:
    def __init__(self):
        self.category_list = []  # ["food", "clothing", and "entertainment"] etc
        self.category_balance = {}   # {"food":100, "clothing":1039, "entertainment":454} etc
    
    
   # Start of the App
    """
    This checks if the category list is empty, if empty then user should create categories
    else proceed to operations to be performed.
    Try initializind any or both of them to test this function
    """
    def app_main(self):
        print(asterics + "Welcom to Budget App".upper() + asterics)
        if not(self.category_list and self.category_balance):
            print("Your Categories are empty, please add categories")
            self.create_categories()
        else:
            self.operation()
        
   
       

    """
    To create fresh category list.
    This grabs the categories in the list and also display their available balances.
    """
    def create_categories(self):
        number_of_categories = int(input("How many categories do you want to create?: "))
        for num in range(1, number_of_categories+1):
            supply_category = input(f"Supply Category Name {num}: ")
            self.category_list.append(supply_category)
            
        for category in self.category_list:
            self.category_balance[category] = 0
        print(asterics + "Categories have been successfully created" + asterics)
        print(f"List and Balance: {self.category_balance}\n")
        self.operation()

    
    # To perform basic operations
    def operation(self):
        print("""These are the operations that can be performed\n
            [1] - DEPOSIT TO CATEGORY.
            [2] - WITHDRAWAL FROM CATEGORY.
            [3] - GET CATEGORY BALANCE.
            [4] - TRANSFER BETWEEN CATEGORIES.
            [5] - CREATE NEW CATEGORY.
            [6] - TOTAL BALANCE.
            [0] - EXIT.
        """)
        try:
            action = int(input("Which operation do you want to perform, type 1,2----6: "))
            if action == 1:
                self.deposit_funds()
                
            elif action == 2:
                self.withdraw_funds()
                
            elif action == 3:
                self.get_balance()
                
            elif action == 4:
                self.transfer_funds()
                
            elif action == 5:
                self.add_new_category()
            
            elif action == 6:
                self.get_total_balance()
                
            elif action == 0:
                self.exit_app()
                
            else:
                print("You have supplied an invalid input, please try again\n")
                self.operation()   
        except ValueError:
            print("Digit is expected")
            self.operation()


    # Deposit funds to any category
    def deposit_funds(self):
        print("The below are the categories available for deposit?")
        for category in self.category_list:
            print(self.category_list.index(category)+1, category) # Returns index+1 of category and category name
        try:
            select_category = int(input("Select a category to deposit funds to: "))
            selected_category = select_category - 1 # subtracts 1 from number supplied to match the real index of the select category in category list.
            category = self.category_list[selected_category] # Pass selected category into a variable
            print(f"you have chosen to deposit funds to  {category}".capitalize())
            deposit_amount = int(input(f"How much do you want to deposit to {category}: "))
            self.category_balance[category] += deposit_amount
            print(f"You have deposited {deposit_amount} to {category}")
            print(f"Your New Balance:  {self.category_balance}")
            try:
                reply = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                if reply == "yes" or reply =="y":
                    self.operation()  
                elif reply =="no" or reply == "no":
                    print(asterics + "Thanks for using this app" + asterics)
                    exit()  
                else:
                    print("invalid input")
            except ValueError:
                print("A string is expected, please try again")
        except:
            print("Digit Expected")
            self.operation()

        
    # Withdraw funds from any category
    def withdraw_funds(self):
        print("The below are the categories available for deposit?")
        for category in self.category_list:
            print(self.category_list.index(category)+1, category) # Returns index+1 of category and category name
        try:
            select_category = int(input("Select a category to withdraw funds from: "))
            selected_category = select_category - 1 # subtracts 1 from number supplied to match the real index of the select category in category list.
            category = self.category_list[selected_category]
            print(f"you have chosen to withdraw funds from  {category}")
            withdrawal_amount = int(input(f"How much do you want to Withdraw from {category}: "))
            if withdrawal_amount >= self.category_balance[category] or self.category_balance[category] <= 0:
                print(f"Insufficient funds, your current balance is {self.category_balance[category]}")
                try:
                    response = input("Would you like to make a deposit? type y/yes or n/no: ".lower()) 
                    if response == "yes" or response == "y":
                        self.deposit_funds()
                    elif response == "no" or response =="n":
                        try:
                            reply = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                            if reply == "yes" or reply =="y":
                                self.operation()
                            elif reply =="no" or reply == "no":
                                print(asterics + "Thanks for using this app" + asterics)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                       
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A string value Expected")
                    self.operation()
            else:
                self.category_balance[category] -= withdrawal_amount
                print(f"{withdrawal_amount} successfully withdrawn from {category}")
                print(f"Updated List and Balance:  {self.category_balance}")
                try:
                    reply = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                    if reply == "yes" or reply =="y":
                        self.operation()
                    elif reply =="no" or reply == "no":
                        print(asterics + "Thanks for using this app" + asterics)
                        exit()
                    else:
                        print("invalid value supplied")
                        self.operation()
                except ValueError:
                    print("String value Expected")
                    self.operation()           
        except ValueError:
            print("Digit value expected")
            self.operation()


    # Transfer funds from one category to the other
    def transfer_funds(self):
        try:
            # Category sending funds
            print("The below are the categories available for deposit?")
            for category in self.category_list:
                print(self.category_list.index(category)+1, category.upper())
            selected_category1 = int(input("Select a category to transfer funds from: "))
            sending_category = selected_category1 - 1
            category1 = self.category_list[sending_category]
            
            # Category receiving funds
            selected_category2 = int(input("Select category to transfer funds to:"))
            for category in self.category_list:
                print(self.category_list.index(category)+1, category)
            receiving_category =  selected_category2 - 1
            category2 = self.category_list[receiving_category]
            
            
            print(f"you have chosen to transfer funds from  {category1} to {category2}")
            withdrawal_amount = int(input(f"How much do you want to transfer from {category1} to {category2}: "))
            if withdrawal_amount >= self.category_balance[category1] or self.category_balance[category1] <= 0:
                print(f"Insufficient funds, your current balance is {self.category_balance[category1]}")
                try:
                    response = input("Would you like to make a deposit? type y/yes or n/no: ".lower()) 
                    if response == "yes" or response == "y":
                        self.deposit_funds()
                    elif response == "no" or response =="n":
                        try:
                            reply = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                            if reply == "yes" or reply =="y":
                                self.operation()
                            elif reply =="no" or reply == "no":
                                print(asterics + "Thanks for using this app" + asterics)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.deposit_funds()   
                except ValueError:
                    print("A string value Expected")
                    self.deposit_funds()
            else:
                self.category_balance[category1] -= withdrawal_amount
                self.category_balance[category2] += withdrawal_amount
                print(f"{withdrawal_amount} Successfully transfered from {category1} to {category2}")
                print(f"Updated List and Balance:  {self.category_balance}")
                try:
                    response = input("Would you like to make another transfer? type y/yes or n/no: ".lower()) 
                    if response == "yes" or response == "y":
                        self.transfer_funds()
                    elif response == "no" or response =="n":
                        try:
                            reply = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                            if reply == "yes" or reply =="y":
                                self.operation()
                            elif reply =="no" or reply == "no":
                                print(asterics + "Thanks for using this app" + asterics)
                                self.operation()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A string value Expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A string value Expected")
                    self.operation()
        except ValueError:
            print("Digit value Expected")
            self.transfer_funds()
     
    
    # Get balance of each category
    def get_balance(self):
        for category in self.category_balance:
            balance = self.category_balance[category]
        print(f"{category} balance: # {balance}")
        try:
            response = input("would you like to perform another operation? type y/yes or n/no: ".lower())
            if response == "yes" or response =="y":
                self.operation()
            elif response =="no" or response == "no":
                print(asterics + "Thanks for using this app" + asterics)
                exit()
            else:
                print("input not found, please try again")
                self.get_balance() 
        except ValueError:
            print("A string value Expected")
            self.operation()

    
    # Get total balance of the categories all-together      
    def get_total_balance(self):
        total_balance = 0
        for category in self.category_balance:
            balance = self.category_balance[category]
            total_balance += balance
            print(f"Total Balance : # { total_balance}")
            try:
                response = input("would you like to perform another operation? type y/yes or n/no: ".lower())
                if response == "yes" or response =="y":
                    self.operation()  
                elif response =="no" or response == "no":
                    print(asterics + "Thanks for using this app" + asterics)
                    exit()
                else:
                    print("input not found, please try again")
                    self.get_total_balance()
            except ValueError:
                print("A string value Expected")
                self.operation()
        
    
    # To add new categories
    def add_new_category(self):
        supply_category = input(f"Supply Category Name: ")
        self.category_list.append(supply_category)
        self.category_balance[supply_category] = 0
        print(asterics + "New Category successfully added" + asterics)
        print(f"New Category List: {self.category_list} \nNew List and Balance:  {self.category_balance}.%2f\n")
        try:
            response = input("Would you like add another category? type y/yes or n/no: ".lower()) 
            if response == "yes" or response == "y":
                self.add_new_category()
            elif response == "no" or response =="n":
                try:
                    reply = input("would you like to perform other operations? type y/yes or n/no: ".lower())
                    if reply == "yes" or reply =="y":
                        self.operation()
                    elif reply =="no" or reply == "no":
                        print("Thanks for using this app")
                        exit()
                    else:
                        print("input not found, operation complete")
                        self.operation() 
                except ValueError:
                    print("A string value Expected")
                    self.operation()
            else:
                print("Invalid value Supplied")
                self.operation()    
        except ValueError:
            print("A string value Expected")
            self.operation()
    def exit_app(self):
        print(f"{asterics}Thanks for using this app{asterics}\n".upper())
        exit()
Budget().app_main()