m = int(input("Enter your Meter number: "))

print("Select your Category")
print("Agriculture-1")
print("Residence-2")
print("Commercial-3")

c = int(input())

u = 0
tax = 0
cost = 0.0

if c == 1:   # Agriculture
    u = int(input("Enter your Units: "))
    tax = 20

    if 0 < u <= 50:
        cost = 0.25
    elif 51 <= u <= 100:
        cost = 0.50
    elif 101 <= u <= 200:
        cost = 0.75
    elif 201 <= u <= 300:
        cost = 2.00
    elif 301 <= u <= 400:
        cost = 2.25
    elif 401 <= u <= 500:
        cost = 2.50
    else:
        print("Cost is high")

elif c == 2:   # Residence
    u = int(input("Enter your Units: "))
    tax = 50

    if 0 < u <= 50:
        cost = 0.50
    elif 51 <= u <= 100:
        cost = 1.00
    elif 101 <= u <= 200:
        cost = 1.50
    elif 201 <= u <= 300:
        cost = 2.00
    elif 301 <= u <= 400:
        cost = 2.50
    elif 401 <= u <= 500:
        cost = 3.00
    else:
        print("Cost is high")

elif c == 3:   # Commercial
    u = int(input("Enter your Units: "))
    tax = 100

    if 0 < u <= 50:
        cost = 1.00
    elif 51 <= u <= 100:
        cost = 2.00
    elif 101 <= u <= 200:
        cost = 3.00
    elif 201 <= u <= 300:
        cost = 4.00
    elif 301 <= u <= 400:
        cost = 5.00
    elif 401 <= u <= 500:
        cost = 6.00
    else:
        print("Cost is high")

else:
    print("Invalid Category")

total = (u * cost) + tax

print("Used units:", u)
print("Rate of the units:", cost)
print("Tax:", tax)
print("Total Amount:", total)
