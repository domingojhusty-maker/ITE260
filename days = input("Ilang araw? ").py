days = int(input("Ilang araw? "))
stay = int(input("Magkano stay per day? "))
food = int(input("Magkano pagkain per day? "))
fare = int(input("Magkano pamasahe? "))

total_stay = days * stay
total_food = days * food
total = total_stay + total_food + fare

print("Total sa stay:", total_stay)
print("Total sa pagkain:", total_food)
print("Lahat ng gastos:", total)