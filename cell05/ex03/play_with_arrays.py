old_array = [1, 3, 5, 7, 9, 3, 7]
new_array = list(set(num + 2 for num in old_array if num + 2 > 5)
print("Old Array:", old_array)
print("New Array:", new_array)