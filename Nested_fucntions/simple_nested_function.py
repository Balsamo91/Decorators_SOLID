

def greet_people(names):
    def greet(name):
        print(f"Hello, {name}!")

    for name in names:
        greet(name)

greet_people(["Alice", "Bob", "Charlie"])

# naming = 'Dave', 'Lala'
# greet_people(naming)


