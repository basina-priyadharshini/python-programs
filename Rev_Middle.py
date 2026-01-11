num = int(input("Enter n value: "))

n = num
r = 0
p = 1
digits = 0   

l = n % 10 

while n != 0:
    d = n % 10
    r = (r * 10) + d
    n = n // 10

print(r)

f = r % 10  

print("First:", f)
print("Last:", l)

for i in range(1, digits - 1):
    p = p * 10

m = num % p
print("Middle numbers:", m)
