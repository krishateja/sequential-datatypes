set1={"apple",100,10.5}
print(set1)#input order is not preserved
#print(set1[2])#input order not preserved so index and slicing is not exit
set2={"apple",100,10.5,"apple",100}
print(set2)#duplication not allowed
set3=set()
print(set3)#it will give empty set
a="apple"
set4=set(a)
print(set4)#set()this is covert to set and input order is not preserved and duplicates not allowed
for i in set4:# in set we cn read data by using for loop only
    print(i)
a={}
print(a)
print(type(a))#if we use empty{}then we call as dictionary not empty set empty set will show like set()
set1.add(200)#it will take exactly only one value
print(set1)
#set1.add([111,222,333])
#print(set1)#list is not allowed in set because list is mutable and changes allowed so we can't do list in set
set1.add((111,222,333))#tuple is immutable we can't changes any values
print(set1)
set1.update((1111,2200,300))#in update we can use any itarable either tuple or list
print(set1)
set1.update([555,"banana",33.6])#in update we can use any itarable either tuple or list
print(set1)
set1.update("teja")#string we can use
print(set1)
set1.remove((111, 222, 333))# we have to give value then it will be remove form the set
print(set1)
set1.pop()
print(set1)
set1.discard("banana")# discard same as remove
print(set1)
#set1.remove("banana")
#print(set1)
#Traceback (most recent call last):
#  File "C:\Users\SANDEEP\Desktop\Basics\sequential data types\sets.py", line 34, in <module>
 #   set1.remove("banana")
#KeyError: 'banana'
set1.discard("banana")# it will not shows any error and if show any error just say set1 is not define
print(set1)
set1.clear()
print(set1)
#del set1
#print(set1)
# print(set1)
#NameError: name 'set1' is not defined
s1={10,20,30,40,50}
print(s1)
print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))
print(any(s1))
print(all(s1))
s2={100,200,300,400,500}
#print(s1+s2)
#TypeError: unsupported operand type(s) for +: 'set' and 'set'
s1.update(s2)#s1 will be updated not s2 .s2 values will be added to s1
print(s1)
print(s2)
s2.update(s1)#s2 will be updated not s1 and s1 values will be added to s2
print(s2)
s1={10,20,30,40,50,200,300}
s2={100,200,300,400,500,50,40}
print(s1.union(s2))#it will give all values in the both sets
print(s1.difference(s2)) #it will give different values in calling values it means s1
print(s2.difference(s1))# it will give different values in calling values it means s2
print(s1.intersection(s2))# it will give similar values between the two sets
s1.difference_update(s2)# it will give difference values and updated to calling set it means s1
print(s1)
s2.difference_update(s1)## it will give difference values and updated to calling set it means s2
print(s2)
s1={10,20,30,40,50,200,300}
s2={100,200,300,400,500,50,40}
s1.intersection_update(s2)# it will give similar values  and updated to calling set it means s1
print(s1)
s1={10,20,30,40,50,200,300}
s2={100,200,300,400,500,50,40}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
s1.clear()
print(s1)
del s1
s1={10,20,30,40,50,200,300}
s2={10,20,30,40}
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
s1={10,20,30,40,50,200,300}
s2={77,88,99,44,55}
print(s2.isdisjoint(s1))