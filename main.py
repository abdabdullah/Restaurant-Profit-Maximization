import pulp as p
prob = p.LpProblem("Maximization_of_Restaurant_Profit", p.LpMaximize)
items = {"x1": "Burger", "x2": "French Fries", "x3": "Pizza", "4": "Cold Drinks", "x5": "Pasta", "x6": "Salad", "x7": "Momos",
         "x8": "Ice Cream", "x9": "Sandwich", "x10": "Samosa"}
x1 = p.LpVariable("x1", lowBound=35, cat = 'Integer')
x2 = p.LpVariable("x2", lowBound=16, cat = 'Integer')
x3 = p.LpVariable("x3", lowBound=20, cat = 'Integer')
x4 = p.LpVariable("x4", lowBound=11, cat = 'Integer')
x5 = p.LpVariable("x5", lowBound=12, cat = 'Integer')
x6 = p.LpVariable("x6", lowBound=5, cat = 'Integer')
x7 = p.LpVariable("x7", lowBound=15, cat = 'Integer')
x8 = p.LpVariable("x8", lowBound=30, cat = 'Integer')
x9 = p.LpVariable("x9", lowBound=18, cat = 'Integer')
x10 = p.LpVariable("x10", lowBound=25, cat = 'Integer')

#Objective Function
prob += 70 * x1 + 80 * x2 + 100 * x3 + 45 * x4 + 40 * x5 + 45 * x6 + 55 * x7 + 20 * x8 + 50 * x9 + 15 * x10

#Constraints

# Max cost per item per day
prob += 150 * x1 + 90 * x2 + 250 * x3 + 95 * x4 + 110 * x5 + 50 * x6 + 75 * x7 + 80 * x8 + 40 * x9 + 20 * x10 <= 20000
# 8 workers work 12 hours per day
prob += 25 * x1 + 20 * x2 + 30 * x3 + 5 * x4 + 40 * x5 + 10 * x6 + 25 * x7 + 7 * x8 + 10 * x9 + 50 * x10 <= 5760
# Appliances and utensils used for all items per day is 350
prob += 1 * x1 + 2 * x2 + 2 * x3 + 1 * x4 + 3 * x5 + 4 * x6 + 3 * x7 + 2 * x8 + 1 * x9 + 2 * x10 <= 350
# Minimum no of sale should be 150
prob += x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 >= 150
# For a mix of a burger and pizza, people will buy 3 drinks
prob += 3 * x1 + 3 * x3 - 2 * x4 >= 0
# From total sales, 30 % sales should be at least of pizza and burger
prob += x1 + x3 >= 0.3 * (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10)

# print(prob)

status = prob.solve()
print(p.LpStatus[status])

x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
print("The Restaurant needs to produce the items in following quantities:\n")
for i, j in zip(items, x):
    print(items[i], "  =   ", p.value(j))

print("\nAnd the maximum profit is : Rs. ", p.value(prob.objective))