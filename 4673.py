def d(n):
    numList = list(map(int,str(n))) 
    num = sum(numList) + n
    return num

result = [x for x in range(1,10000)]
for i in range(1,10000):
    temp = d(i)
    if temp in result:
        result.remove(temp)
for el in result:
    print(el)