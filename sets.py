# sets

# A set in Python is a collection of unique elements used to store values without duplicates. It is useful in data analytics for removing duplicate values and finding unique items.

# it is closed insidde the curly brackets {} and it is separated by commas


customer_ids = [101, 102, 101, 103, 102, 104]
unique_ids = set(customer_ids)
print(unique_ids)  # o/p => {104, 101, 102, 103}



# to find common costumers

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print(day1.intersection(day2))    # print(day1 & day2) we can use this also for concatenation