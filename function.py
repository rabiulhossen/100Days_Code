# Example 1
# lists

fruits = ["apple", "banana", "cherry"]
quantities = [1, 2, 3]

# using zip to iterate over two lists
for fruit, quantity in zip(fruits, quantities):
     print(f"We have {quantity} {fruit}")
     
     
     
# Example 2

flowers = ["rose", "tulip", "daisy"]
# using enumerate to iterate over a list
for index, flower in enumerate(flowers):
    print(f"flower at index {index}: {flower}") 
    

# dictionaris
# Example 3

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# using zip to iterate over key-value pairs
for name, grade in student_grades.items():
    print(f"{name}'s grade: {grade}")
    

"""
Explanation:
Example 1: The zip function combines corresponding elements of multiple lists, allowing us to iterate over them simultaneously.

Example 2: The enumerate function provides both the index and value of each element in the list during iteration.

Example 3: The items method of dictionaries provides key-value pairs, enabling iteration over both keys and values.

Question:
How can you handle exceptions effectively in Python, and why is it important in the context of robust programming?

"""