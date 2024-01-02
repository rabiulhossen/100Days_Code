# lists

fruits = ["apple", "banana", "cherry"]
quantities = [1, 2, 3]

# using zip to iterate over two lists
for fruit, quantity in zip(fruits, quantities):
     print(f"We have {quantity} {fruit}")
     
     
     


flowers = ["rose", "tulip", "daisy"]
# using enumerate to iterate over a list
for index, flower in enumerate(flowers):
    print(f"flower at index {index}: {flower}") 
    

# dictionaris

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# using zip to iterate over key-value pairs
for name, grade in student_grades.items():
    print(f"{name}'s grade: {grade}")
