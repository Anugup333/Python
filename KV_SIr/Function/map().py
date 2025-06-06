def map_square():
    return list(map(lambda num : num**2,[int(i) for i in input("Enter Value: ").split()]))

print("Square of the given number ",map_square())