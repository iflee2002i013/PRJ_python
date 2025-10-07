alien_color = 'red'
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")


alien_color = 'yellow'
if alien_color == "green":
    print("You just earned 10 points!")

avaliable_toppings = ['mushrooms', 'onions', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding " + requested_topping + " to your pizza.")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Your pizza is ready!")
print("Enjoy your pizza!")
