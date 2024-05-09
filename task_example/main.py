from manager import Manager

account = 10000.0
inventory = {
    "bike" : {'price': 300, 'quantity' : 10},
    "Scooter" : {'price': 500, 'quantity' : 5}
}
history = []


# Create an instance of Manager
manager = Manager()

@manager.assign("balance")
def balance(manager):
    global account
    money = float(input("Provide amount of money to add/subtract: "))
    account += money
    print(f"Currrnt balance is: {account}")

@manager.assign("Sale")
def sale(manager):
    pass

@manager.assign("purchase")
def purchase(manager):
    pass

@manager.assign("account")
def account_money(manager):
    global account
    print(f"current balance: {account}")

@manager.assign('list')
def list_inventory(manager):
    for item in inventory:
        print(item)
        print(f"-Price per unit: {inventory[item]['price']}")
        print(f"-quantity: {inventory[item]['quantity']}")

@manager.assign("warehouse")
def warehouse(manager):
    pass

@manager.assign("review")
def review(manager):
    pass

while True:
    command = input("Provide command: ")

    if command == 'balance':
        manager.execute('balance')
    elif command == 'sale':
        manager.execute('sale')
    elif command == 'purchase':
        manager.execute('purchase')
    elif command == 'account':
        manager.execute('account')
    elif command == 'list':
        manager.execute('list')
    elif command == 'warehouse':
        manager.execute('warehouse')
    elif command == 'review':
        manager.execute('review')
    elif command == 'end':
        break
    else:
        print('NO')
        break