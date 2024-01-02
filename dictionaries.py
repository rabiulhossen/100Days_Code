# dictionaries
# dictonaries is javascript object
dic = {
          "name": "John",
          "age": 36,
          "country": "Norway"
}




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
