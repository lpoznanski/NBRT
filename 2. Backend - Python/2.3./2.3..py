# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
users_pl = [user for user in users if len(user) > 1 and user["country"] == "Poland"]
print(users_pl)

# Display sum of first ten elements starting from element 5:
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
result = sum(numbers[4:14])
print(result)

# Fill list with powers of 2, n [1..20]
result = [2**n for n in range(1, 21)]
print(result)