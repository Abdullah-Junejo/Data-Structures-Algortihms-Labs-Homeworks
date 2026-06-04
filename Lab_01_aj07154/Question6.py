from itertools import combinations

def num_toppings(toppings, budget):
    topping_prices = list(toppings.values())
    count=0
    print(topping_prices)
    for each in combinations(topping_prices, 3):
        total_price = sum(each)
        if total_price <= budget:
            count += 1
    return count

# DO NOT EDIT
toppings = {'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}
budget = 700
assert num_toppings(toppings, budget) == 4 #Possible Combinations