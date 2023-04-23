# Assignment written by: ___Sejin Yoon___


# Given list
cars = [['BMW', 'Mercedes', 'range Rover', ['Luxury','model-2021']], ['Ferrari', 'Lamborghini', 'Bugatti', ['Expensive','model-2022']], ['Toyota', 'Hyundai', 'Volvo', ['model-2022']]]

# Prints 'Lamborghini' and 'Bugatti'
print("1.",cars[1][1:3])

# Prints 'Hyundai'
print("2.",cars[2][1])

# Prints 'Luxury'
print("3.",cars[0][3][0])

# Prints ['BMW', 'Mercedes']
print("4.",cars[0][:2])

# Prints ['BMW', 'Ferrari', 'Toyota']
print("5.",[car[0] for car in cars])