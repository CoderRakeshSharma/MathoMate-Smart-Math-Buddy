import math
import time
import os


def main():
    while True:
        print("""
Choose what you want to perform:
A) Calculation
B) Trigonometric calculation
C) Number check
D) Number range condition
E) Temperature conversion
F) Geometry calculations
G) Pythagoras theorem
H) Number theory
Q) Quit
        """)
        choice = input("Enter your choice: ").upper()

        if choice == 'A': basic_calculator()
        elif choice == 'B': trig_calculator()
        elif choice == 'C': number_checks()
        elif choice == 'D': range_conditions()
        elif choice == 'E': temp_converter()
        elif choice == 'F': geometry_calculations()
        elif choice == 'G': pythagoras_solver()
        elif choice == 'H': number_theory()
        elif choice == 'Q': 
            print("Goodbye!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else: print("Invalid choice, try again.")


def basic_calculator():
    print("\n--- Basic Calculator ---")
    print("""Choose operation:
1. +\n2. -\n3. *\n4. /\n5. //\n6. %\n7. root\n8. **""")
    op = input("Enter operation number: ")
    if op == '7':
        c = float(input("Enter the number: "))
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))


    if op == '1': print(a + b)
    elif op == '2': print(a - b)
    elif op == '3': print(a * b)
    elif op == '4': print(a / b)
    elif op == '5': print(a // b)
    elif op == '6': print(a % b)
    elif op == '7': print(math.sqrt(c))
    elif op == '8': print(a ** b)
    else: print("Invalid operation.")


def trig_calculator():
    print("\n--- Trigonometric Calculator ---")
    print("\nChoose function: sin, cos, tan, cosec, sec, cot")
    func = input("Function: ").lower()
    angle = math.radians(float(input("Enter angle in degrees: ")))

    funcs = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'cosec': lambda x: 1 / math.sin(x),
        'sec': lambda x: 1 / math.cos(x),
        'cot': lambda x: 1 / math.tan(x)
    }
    try:
        print(funcs.get(func, lambda x: "Invalid function")(angle))
    except ZeroDivisionError:
        print("Math error: Division by zero in trig function.")



def number_checks():
    print("\n--- Number Checks ---")
    print("""Choose check:
1. Prime\n2. Palindrome\n3. Even/Odd\n4. Armstrong""")
    ch = input("Enter choice: ")
    n = int(input("Enter number: "))

    if ch == '1':
        if n < 2: print("Not prime")
        elif all(n % i for i in range(2, int(n**0.5)+1)): print("Prime")
        else: print("Not prime")
    elif ch == '2': print("Palindrome" if str(n) == str(n)[::-1] else "Not palindrome")
    elif ch == '3': print("Even" if n % 2 == 0 else "Odd")
    elif ch == '4': print("Armstrong" if sum(int(d)**len(str(n)) for d in str(n)) == n else "Not Armstrong")
    else: print("Invalid")


def range_conditions():
    print("\n--- Range Conditions ---")
    print("""Choose condition:
1. Fibonacci\n2. Even\n3. Odd\n4. Natural\n5. Prime""")
    cond = input("Enter choice: ")
    low = int(input("Enter lower range: "))
    high = int(input("Enter higher range: "))

    if cond == '1':
        a, b = 0, 1
        while a <= high:
            if a >= low: print(a, end=' ')
            a, b = b, a + b
    elif cond == '2': print(*[i for i in range(low, high+1) if i % 2 == 0])
    elif cond == '3': print(*[i for i in range(low, high+1) if i % 2 != 0])
    elif cond == '4': print(*[i for i in range(max(1, low), high+1)])
    elif cond == '5':
        for i in range(low, high+1):
            if i > 1 and all(i % j for j in range(2, int(i**0.5)+1)): print(i, end=' ')
    else: print("Invalid")


def temp_converter():
    print("\n--- Temperature Converter ---")
    scale = input("Enter scale (C/F/K): ").upper()
    temp = float(input("Enter temperature: "))
    if scale == 'C':
        print(f"F: {temp * 9/5 + 32}, K: {temp + 273.15}")
    elif scale == 'F':
        print(f"C: {(temp - 32) * 5/9}, K: {(temp - 32) * 5/9 + 273.15}")
    elif scale == 'K':
        print(f"C: {temp - 273.15}, F: {(temp - 273.15) * 9/5 + 32}")
    else: print("Invalid scale")


def geometry_calculations():
    print("\n--- Geometry Calculator ---")
    print("1. Square\n2. Rectangle\n3. Triangle\n4. Circle")
    ch = input("Enter shape: ")
    if ch == '1':
        s = float(input("Side: "))
        print(f"Area: {s**2}, Perimeter: {4*s}")
    elif ch == '2':
        l = float(input("Length: "))
        b = float(input("Breadth: "))
        print(f"Area: {l*b}, Perimeter: {2*(l+b)}")
    elif ch == '3':
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        c = float(input("Side c: "))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print(f"Area: {area}, Perimeter: {a + b + c}")
    elif ch == '4':
        r = float(input("Radius: "))
        print(f"Area: {math.pi * r**2}, Circumference: {2 * math.pi * r}")
    else: print("Invalid")


def pythagoras_solver():
    print("Find missing side of right triangle")
    print("1. Hypotenuse\n2. Base\n3. Perpendicular")
    ch = input("Enter choice: ")
    if ch == '1':
        b = float(input("Base: "))
        p = float(input("Perpendicular: "))
        print(f"Hypotenuse: {math.sqrt(b**2 + p**2)}")
    elif ch == '2':
        h = float(input("Hypotenuse: "))
        p = float(input("Perpendicular: "))
        print(f"Base: {math.sqrt(h**2 - p**2)}")
    elif ch == '3':
        h = float(input("Hypotenuse: "))
        b = float(input("Base: "))
        print(f"Perpendicular: {math.sqrt(h**2 - b**2)}")
    else: print("Invalid")


def number_theory():
    print("1. GCD\n2. LCM\n3. Mod")
    ch = input("Enter choice: ")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if ch == '1': print(math.gcd(a, b))
    elif ch == '2': print(abs(a*b) // math.gcd(a, b))
    elif ch == '3': print(a % b)
    else: print("Invalid")



if __name__ == "__main__":
    main()
