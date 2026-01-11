b = 1200   # initial bank balance

print("Bank balance-1\nCash Withdraw-2\nFast Cash-3")
a = int(input())

if a == 1:
    print("Bank Balance:", b)

elif a == 2:
    w = int(input("Enter cash: "))
    if w < b and w > 200:
        b -= w
        print("Withdraw:", w)
        print("Remaining balance:", b)
    else:
        print("Insufficient balance")

elif a == 3:
    print("1. 500\n2. 1000\n3. 1500\n4. 2000\n5. 3000\n6. 5000\n7. 10000")
    c = int(input())

    if c == 1:
        d = 500
    elif c == 2:
        d = 1000
    elif c == 3:
        d = 1500
    elif c == 4:
        d = 2000
    elif c == 5:
        d = 3000
    elif c == 6:
        d = 5000
    elif c == 7:
        d = 10000
    else:
        print("Invalid Fast Cash")
        exit()

    if d > b:
        print("Insufficient balance")
    else:
        b -= d
        print("Withdrawn:", d)
        print("Remaining Balance:", b)

else:
    print("Invalid option")
