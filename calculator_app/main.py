def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def factorial(n): # Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n): # whole number that can only be divided evenly by 1 and itself.
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): # range(start, stop, step) # e.g. 16, range(2, 5) = 2, 3, 4
        if n % i == 0:
            return False
    return True

def power(a, b):
    return a ** b

def input_number():
   while True: 
        entry = input("Enter one or two numbers separated by a space:")
        numbers = entry.split()
        try:
            if len(numbers) == 1:
                n = int(numbers[0])
                factorial_result = factorial(n)
                prime_result = is_prime(n)
                print(f"Factorial of {n} is {factorial_result}.\n{n} is prime number? {'True' if prime_result else 'False'}.")
        
            elif len(numbers) == 2:
                a, b = map(int, numbers)
                results = {
                    "Addition": add(a, b),
                    "Multiplication": multiply(a, b),
                    "Power": power(a, b),
                    f"Factorial of {a}": factorial(a),
                    f"Factorial of {b}": factorial(b)
                }
                for operation, value in results.items():
                    print(f"{operation}: {value}")
            else:
                return "Please enter one or two numbers only."
        except ValueError:
            return "Invalid input! Please enter valid integers."

# Call the function
result = input_number()
print(result)