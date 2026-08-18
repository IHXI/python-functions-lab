# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base, height):
    total = base * height / 2
    return total

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest

def simple_interest(principal, rate, time):
    total = principal * rate * time /100
    return total


print('Exercise 2:', simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount

def apply_discount(price, discount):
    if discount >= 0 and discount <= 100:
        valid_discount = discount / 100
        savings = price * valid_discount
        return price - savings


print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature

def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9 / 5) +32
    elif unit == "F":
        return (temp - 32) * 5 / 9




print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N

def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number

def largest(num1, num2, num3):
    return max(num1, num2, num3)


print('Exercise 6:', largest(0, 9, 1))
# Exercise 7: Calculate a Tip

def calculate_tip(bill, tip):
    tip = tip / 100
    return bill * tip



print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers

def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total
        

print('Exercise 8:', product(-1, 4))

# Exercise 9: Basic Calculator

def basic_calculator(num1, num2, operation):
    total = 0
    if operation == "subtract":
        total = num1 - num2
    elif operation == "add":
        total = num1 + num2
    elif operation == "multiply":
        total = num1 * num2
    elif operation == "divide":
        total = num1 / num2

    return total

print('Exercise 9:', basic_calculator(10, 5, operation="multiply"))



