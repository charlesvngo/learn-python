# Determine the cost it is to ship a product via ground or air
weight = 8.4
cost = 0

# Ground shipping
if weight <= 2.0:
    cost = 20 + 1.5 * weight
elif weight > 2.0 and weight <= 6.0:
    cost = 20 + 3.0 * weight
elif weight > 6.0 and weight <= 10.0:
    cost = 20 + 4.0 * weight
else:
    cost = 20 + 4.75 * weight

print(cost)
