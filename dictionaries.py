# dictionaries
# dictonaries is javascript object
dic = {
          "name": "John",
          "age": 36,
          "country": "Norway"
}


eng2ban = {
    'one': 'ak', 'two': 'dui', 'three': 'tin'
}

print(eng2ban['one'])
print('two' in eng2ban)
print(dict())


def histogram (s):
    d = dict()
    for c in s:
        print(c)
        '''
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
'''
print(histogram('rabiulsimon'))




"""
print(dic.keys())
print(dic.values())
dic2= (dic.copy()) value copy
print(dic2)
"""


dic["department"] = "IT" #value add

# dic.popitem() #last value remove
del dic["age"] #value remove
print(dic)

# print all time
for x in dic:
    print(x, dic[x])


students_data = { 

 'Stud1': ['CS1101', 'CS2402', 'CS2001'], 
 'Stud2': ['CS2402','CS2001','CS1102']
    

    } 

reversed_data = {
    
}

for key in students_data:

    for value in students_data[key]:
        reversed_data[value] = key
        
print(reversed_data)
        
        
        
"""

Inverted Output: 

{ 

‘CS1101’: [‘Stud1’], 

‘CS2402’:['Stud1’,’Stud2’], 

‘CS2001’: ['Stud1’,’Stud2’] 

‘CS 1102’[‘Stud2’] 

} 

"""