sandwich_orders = ['BLT', 'PB&J', 'Honey Mustard', 'Grilled Cheese', 'Bacon']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwiche)
    print(f"I made your {finished_sandwiche} sandwich.")

print(f"I have made {finished_sandwiches}")

sandwich_orders = ['BLT', 'PB&J', 'Honey Mustard', 'pastrami', 'Grilled Cheese', 'Bacon''pastrami','pastrami']
print('The pastrami sandwiches is sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What is your favorite color? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("Survey results:")
for name,response in responses.items():
    print(f"{name} likes {response}!")