n = int(input("Enter n value: "))

l = n % 10      # last digit
r = 0
temp = n       # original number save cheyyadam kosam

while temp != 0:
    d = temp % 10
    r = (r * 10) + d
    temp = temp // 10

print("Reversed number:", r)

f = r % 10     # first digit

print("First:", f)
print("Last:", l)

if f % 2 == 0 and l % 2 == 0:
    print("Even numbers:", f, l)
elif f % 2 == 1 and l % 2 == 1:
    print("Odd numbers:", f, l)
else:
    print("Mixed numbers:", f, l)
