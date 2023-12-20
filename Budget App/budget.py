class Category: # Creates the class Category

    def __init__(self,name): # Initilizes the varibles needed for the class to work
        self.ledger=[]
        self.name=name
        self.balance=0
        

    def deposit(self,money,title=''): # Takes input for how much money was deposited, can also have an description
        self.balance = money
        base_deposit = ({"amount":int(money),"description":title})
        self.ledger.append(base_deposit)

        return base_deposit

    def withdraw(self,money,title=''): # Takes input for how much money was withdrawled, can also have an description
        money=money*-1 # Turns the amount negative
        base_withdrawl = ({"amount":money,"description":title})

        if not self.ledger: 
            return False    
        
        if self.check_funds(money) == False: # This checks the funds availble to be withdrawled, If false it can not withdrawl funds
            return False
        else:    
            self.ledger.append(base_withdrawl) # If there are available funds to be withdrawled then it is added to the class list
            return True
    
    
    def get_balance(self): # Formats the current balance of the account
        formatted_balance = format(self.balance, '.2f')
        return formatted_balance
    
    def transfer(self,money,title): # Checks to see if there is availble money and then transfer that as a deposit in the other account
        
        if self.withdraw(money,'Transfer to '+title.name) == True:
            title.deposit(money,'Transfer from '+self.name)
        

    def check_funds(self,amount): # Checks to see if the account has funds that can be withdrawled and updates the balance if True
        if amount > 0:
            amount=amount*-1
        if self.balance + amount < 0:
            return False
        else:
            self.balance = self.balance + amount
            return True

    def __str__(self): # Formats the output if the class is called
        formatted_balance = format(self.balance, '.2f') # Makes sure the balance has 2 floating points

        stars=f'******************************'
        total_length=len(stars)
        stars_on_sides=(total_length - len(self.name)) // 2
        formatted_title = stars[:stars_on_sides] + self.name + stars[-stars_on_sides:] # Centers the name of the class in the stars
        final_str=formatted_title+'\n'

        for iterator in self.ledger: # Prints out all of the Withdrawls, Deposits, and the Total to finish it off
            description=str(iterator['description'])
            amount=str(iterator['amount'])
            formatted_amount=format(float(amount), '.2f')
            formatted_description=f"{description[:23]:23}" # Cuts off any text after 23 Characters
            final_str+=formatted_description+format(formatted_amount.rjust(7))+'\n' # Right justifies the dollar amount 
        return(final_str+'Total: '+formatted_balance)


def create_spend_chart(categories): # Creates a chart of all the categories inputed and displays a the % spent in total by each
    
    total_spent=0
    average_list=[]
    new_average_list=[]
    final_result=''

    for cata in categories: # Creates a list of all the categories and finds the total spent by each one
        length=len(cata.ledger)
        average=0
        for withdraw_balance in range(length):
            if withdraw_balance==0: continue
            total_spent=total_spent+cata.ledger[withdraw_balance]['amount']
            average=average+cata.ledger[withdraw_balance]['amount']
            if withdraw_balance == length-1:
                average_list.append(average)

    for averages in average_list: # Finds the % spent by each returning all of the categories % in a list
        new_average = ((averages/total_spent)*1000)//100*10
        new_average_list.append(new_average)
    
    final_result='Percentage spent by category'+'\n' # Making the final output one variable
    
    # Preping Varibles for the Chart
    colomns=len(categories)
    vertical_rows=0
    amount_of_rows=11
    starting_percent=100
    dashes = '    ---'
    while vertical_rows < amount_of_rows: # This makes the chart the correct format based on what % it is at
        vertical_rows=vertical_rows+1
        if starting_percent < 10:
            row='  '+str(starting_percent)+'|'
        elif starting_percent < 100:
            row=' '+str(starting_percent)+'|'
        else:
            row=str(starting_percent)+'|'
        
        for x in new_average_list: # This checks to see if based on the % in the average list if it will output a ' o ' or not
            if starting_percent <= x:
                row= row+' o '
            else:
                row+= '   '
        final_result=final_result+row+'\n'
        

        starting_percent=starting_percent-10 # Decreases the starting percent by 10
        

        if starting_percent == -10: # Checks to see if the percent hits below 0 then checks to see how many dashes need to be added based on categories inputed
            for dashrows in range(colomns-1):
                if dashrows == 0:
                    new_dashes= dashes+dashes[4:]
                else:
                    new_dashes = new_dashes+dashes[4:]
            
    new_dashes=new_dashes+'-'
    
    final_result=final_result+new_dashes+'\n'

    # Format the categories since they will be vertical
    starting_space='     '
    category_list=[]
    
    for add_names in range(len(categories)): # Adds all of the names of the categories to a list
        listnames=categories[add_names].name
        category_list.append(listnames)
    
    max_string_len=max(len(string) for string in category_list) # Finds the longest name out of the entire list

    for lines in range(max_string_len):   # Starts to format the names vertically based on the longest string
        final_result += starting_space
        for string in category_list:         
            if lines < len(string):
                    final_result += string[lines] +'  ' # Goes through each string one letter at a time
            else:
                final_result+='   '
        final_result+='\n'

    return final_result # Sends the output as one varible