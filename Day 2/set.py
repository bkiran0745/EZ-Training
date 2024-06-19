my_set = {23,32,53,34}
#inserting into set
my_set.add(34)
print("After adding the element 34 : ",my_set)
#update 
n = {1}
my_set.update(n)
print("After updating set : ",my_set)
#discard
my_set.discard(4)
print("After discarding set : ",my_set)
#union
new_set = {2,3,4,5,6}
union=my_set.union(new_set)
print("After union operation of set : ",union)
#pop
print("After pop operation set : ",my_set.pop())
#clear
my_set.clear()
print("After clear the set : ",my_set)
