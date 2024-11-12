SECOND LARGEST ELEMENT IN LIST

def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    return unique_lst[-2]

# Example usage
print(second_largest([1, 2, 3, 4, 5]))  # Output: 4

hello......
