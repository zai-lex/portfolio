import budget
from budget import create_spend_chart

# This project creates multiple Categories that can take withdrawls, deposits, and transfers
# It will return all money spent and withdrawled if called
# If create_spend_chart is used it will create a chart based off the % money spent by each Category
# This is my first project using classes


food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))



