import sys
import timeit

def square_numbers(n):
    return[i ** 2 for i in range(1, n + 1)]

def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    return merged_list

n = 10
print(f"Squares from 1 to {n}: {square_numbers(n)}")

# Task 2 Example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i, j = 2, 6
print(f"Original list: {lst}")
print(f"List after reversing sublist from index {i} to {j}: {reverse_sublist(lst, i, j)}")

# Task 3 Example
lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]
print(f"Merging lists {lst1} and {lst2}: {merge_sorted_lists(lst1, lst2)}")

# Complexity Analysis
# Task 1: List Comprehension
print("\nTask 1 Complexity Analysis")
n = 1000
print(f"Time to create list of squares for n={n}: {timeit.timeit(lambda: square_numbers(n), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(square_numbers(n))} bytes")

# Task 2: Reverse Sublist
print("\nTask 2 Complexity Analysis")
lst = list(range(1000))
i, j = 100, 900
print(f"Time to reverse sublist for n={len(lst)} from {i} to {j}: {timeit.timeit(lambda: reverse_sublist(lst, i, j), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(lst)} bytes")

# Task 3: Merge Two Sorted Lists
print("\nTask 3 Complexity Analysis")
lst1 = list(range(0, 1000, 2))
lst2 = list(range(1, 1000, 2))
print(f"Time to merge two sorted lists of size {len(lst1)} and {len(lst2)}: {timeit.timeit(lambda: merge_sorted_lists(lst1, lst2), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(merge_sorted_lists(lst1, lst2))} bytes")
        