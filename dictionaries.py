import sys
import timeit

def merge_dictionaries(dict1, dict2):
    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    return merge_dict

def intersection_dictionaries(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key in dict2}

def count_word_frequency(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
print(f"Merged dictionaries: {merge_dictionaries(dict1, dict2)}")

# Task 2 Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'e': 6}
print(f"Intersection of dictionaries: {intersection_dictionaries(dict1, dict2)}")

# Task 3 Example
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(f"Word frequency: {count_word_frequency(words)}")

# Complexity Analysis
# Task 1: Merge Dictionaries
print("\nTask 1 Complexity Analysis")
dict1 = {i: i for i in range(1000)}
dict2 = {i: i*2 for i in range(500, 1500)}
print(f"Time to merge dictionaries: {timeit.timeit(lambda: merge_dictionaries(dict1, dict2), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(merge_dictionaries(dict1, dict2))} bytes")

# Task 2: Intersection of Dictionaries
print("\nTask 2 Complexity Analysis")
dict1 = {i: i for i in range(1000)}
dict2 = {i: i*2 for i in range(500, 1500)}
print(f"Time to find intersection: {timeit.timeit(lambda: intersection_dictionaries(dict1, dict2), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(intersection_dictionaries(dict1, dict2))} bytes")

# Task 3: Word Frequency Count
print("\nTask 3 Complexity Analysis")
words = ['word' + str(i) for i in range(1000)] * 2
print(f"Time to count word frequency: {timeit.timeit(lambda: count_word_frequency(words), number=1000)} seconds")
print(f"Memory used: {sys.getsizeof(count_word_frequency(words))} bytes")