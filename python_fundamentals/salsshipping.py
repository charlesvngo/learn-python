# Determine the cost it is to ship a product via ground or air

weight = 41.5
cost_ground = 0
cost_drone = 0

# Ground shipping
if weight <= 2.00:
    cost_ground = 20 + 1.50 * weight
elif weight > 2.00 and weight <= 6.00:
    cost_ground = 20 + 3.0 * weight
elif weight > 6.00 and weight <= 10.00:
    cost_ground = 20 + 4.00 * weight
else:
    cost_ground = 20 + 4.75 * weight

# Premium ground shipping
cost_premium_ground = 125.00

# Drone shipping
if weight <= 2.00:
    cost_drone = 4.50 * weight
elif weight > 2.00 and weight <= 6.00:
    cost_drone = 9.0 * weight
elif weight > 6.00 and weight <= 10.00:
    cost_drone = 12.00 * weight
else:
    cost_drone = 14.25 * weight

print("Weight :" + str(weight))
print("Ground Shipping: " + str(cost_ground))
print("Premium Ground Shipping: " + str(cost_premium_ground))
print("Drone Shipping: " + str(cost_drone))
