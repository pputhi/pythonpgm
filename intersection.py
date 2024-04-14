set1={'raj','new','Bubu','Dudu'}
set2=('Dudu','Bubu')

set3=set1.union(set2)
print(set3)
#set3=set1|set2  #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
print(set3)
set1.update(["laddu","Tavakkalai"])
print(set1)
#intersection
set1.intersection_update(set2)
print(set1)
print(set1&set(set2))
