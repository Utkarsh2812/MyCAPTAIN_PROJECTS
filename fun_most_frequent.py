str1 = input("Enter a String: ")
  
res = {}
  
for keys in str1:
    res[keys] = res.get(keys, 0) + 1
  
print (str(res))
