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

def main():
    try:
        choice = input("Choose operation: add, subtract, multiply, factorial, prime, power: ").lower()
        if choice in ['add', 'subtract', 'multiply', 'power']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == 'add':
                print("Result:", add(a, b))
            elif choice == 'subtract':
                print("Result:", subtract(a, b))
            elif choice == 'multiply':
                print("Result:", multiply(a, b))
            elif choice == 'power':
                print("Result:", power(a, b))
        elif choice == 'factorial':
            a = int(input("Enter a number: "))
            print("Result:", factorial(a))
        elif choice == 'prime':
            a = int(input("Enter a number: "))
            print("Result:", "Prime" if is_prime(a) else "Not Prime")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
