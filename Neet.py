print("East Godavari:")
for i in range(1, 500):
    print(f"{i:04d}-EG")

print("Rayala Sima:")
for j in range(1, 500):

    if 30 <= j <= 50:
        continue
    if 100 <= j <= 120:
        continue
    if 2310 <= j <= 350:   # same condition as C (though logically wrong)
        continue
    if 390 <= j <= 408:
        continue
    if 457 <= j <= 532:
        continue

    print(f"{j:04d}-RSL")

print("West Godavari:")
for j in range(1, 500):

    if 67 <= j <= 100:
        continue

    print(f"{j:04d}-WG")
