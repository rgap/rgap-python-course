# Example: Using map with multiple iterables to sum elements of two lists
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sum_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"Sum of elements from two lists: {sum_numbers}")
