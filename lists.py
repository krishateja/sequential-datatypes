#tables
print([(str(i)+"*"+str(j)+"="+str(i*j),  )           for i in range(2,6)  for j in range(1,11)])
#using list employee details
l1=[]
for i in range(5):
    a=input("enter names:")
    l1.append(a)
print(l1)
l2=[]
for i in range(5):
    a=input("enter ages:")
    l2.append(a)
print(l2)
l3=[]
for i in range(5):
    a=input("enter occupation")
    l3.append(a)
print(l3)
l4=[]
for i in range(5):
    a=input("enter salary")
    l4.append(a)
print(l4)
print("@@@@@@@@@@@@@@@@@@@@@")
print(l1)
print(l2)
print(l3)
print(l4)

l5=[]
for i in range(5):
    a="NAME="+l1[i], "AGE="+l2[i] , "OCCUPATION="+l3[i],"SALARY="+l4[i]
    l5.append(a)
print(l5)
#practice
e=list()
print(e)
e.append(7)
print(e)
e.insert(0,8)
print(e)
e.append(["teja","raju","chandu",7])
print(e)
e.extend([1,2,3])
print(e)
e.extend("teja")
print(e)
e.extend("123")
print(e)
f=print(len(e))
e.insert(7,85)
print(e)
e.append(1)
print(e)
print(e.index(1))
print(e[2:6:1])
for i in e:
    print(i)
print(e.index(["teja","raju","chandu",7]))
e.insert(2,8)
print(e)
e[3].append(3)
print(e)
e[2:2]=2000,3000,6000
print(e)
e[2]=4000,77,888
print(e)
e[3]=5000
print(e)
e[3:3]=55,88,99
print(e)
e[6]=55,68,99
print(e)
e[2:4]=1000,400,50,66
print(e)
e.remove(8)
print(e)
e.remove(1)
print(e)
e.remove("1")
print(e)
e.remove(1)
print(e)
e.pop()
print(e)
e.pop()
print(e)
e.pop()
print(e)
e.pop(6)
print(e)
e[2:3]=""
print(e)
e[2:5]=""
print(e)
del e[1]
print(e)
del e[4:7]
print(e)
list1=[]
for i in range (5):
    a=input("enter values:")
    list1.append(a)
print(list1)
list2=[]
for i in range(5):
    list2.append(int(list1[i])+1000)
print(list2)
l1=[1,2,5,3,4]
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
print(len(l1))
print(max(l1))
print(min(l1))
# reference copy(if u change any value in list 2 automatically changes in l1)
l2=l1
print(l2)
print(l1)
l2.append(6)
print(l2)
print(l1)
#shallow copy(memory location will be different and if u change any value in list2 in list1 dose not change but in nested list will be  change because nested list memory location same
l2=l1.copy()
l2.append(6)
print(l2)
print(l1)
l2.append([5,6,4,7])
print(l2)
print(l1)
l2=l1
l3=[1,2,3,4,[5,6,4,7]]
import copy
l4=copy.copy(l3)
print(l3)
print(id(l3))
print(l4)
print(id(l4))
l4.append(5)
print(l4)
print(l3)
l5=list(l3)
print(l5)
print(id(l5))
print(l3)
print(id(l3))
l5[4].append(9)
print(l5)
print(l3)
print(id(4))
print(id(4))
#deepcopy(nested list memory location will be change in deep copy so if change in list l6 list l3 dost not change in nested list)
import copy
l6=copy.deepcopy(l3)
print(l6)
print(id(5))
print(l3)
print(id(l3))
print(id(l6[4]))
print(id(l3[4]))
l6[4].append(85)
print(l6)
print(l3)

print([i for i in range(5)])
print([i for i in range(20) if i%2==0])
print([(str(5)+"*"+str(i)+"="+str(5*i))  for i in range(11)])
l2=["teja",55,"152",55.5]
s=0
for i in l2:
    if type(i)==int:
        s=s+i
    elif type(i)==float:
        s=s+int(i)
    elif i.isdigit()==True:
        s=s+int(i)
print(s)
l1=[1,2,[2,3,[2,2,2],3,4,2],[3,4,6,[6,7,8],7,7],7,5,9]
l2=[]
for i in l1:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                for k in j:
                    l2.append(k)
            else:
                l2.append(j)
    else:
        l2.append(i)
print(l2)
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(5):
    a=input("enter name:")
    b=input("enter age: ")
    c=input("enter occupation:")
    d=input("enter salary:")
    l1.append(a)
    l2.append(b)
    l3.append(c)
    l4.append(d)
print(l1)
print(l2)
print(l3)
print(l4)
l5=[(l1[i],l2[i],l3[i],l4[i])   for i in range(5)]
print(l5)
l6=[i     for i in zip(l1,l2,l3,l4)]
print(l6)
l7=[[input("enter value:") for i in range(4)]  for j in range(3)]
print(l7)
for i in zip(l1,l2,l3,l4):
    print([i])
a="10,20,30,40"
list1=a.split(",")
print(a)
print(type(a))
print(type(list1))
b="".join(list1)# to convert list to string format
print(b)
print(type(b))
c="teja"
print(c)
print(type(c))
#list5=[10,20,30,40]      (in join function only one convertion when list is in the form of string it will convert to string other wise it will not convert)
#print(" ".join(list5))
#print(type(list5))
list2=["a","b","c"]
print(* list2)       #(*list will convert anydata type to string format whether the list in the form string or int or float or mixed with int and string it will convert to string )
print(type(list2))
list3=[10,20,30,40]
print(* list3)
print(type(list3))
list4=[10,"20",40,"30",7.5]
print(* list4)
print(type(list4))
l1=[[ i for i in range(5)]   for j in range(3)]
print(l1)
import itertools
z=itertools.chain(*l1)
print(list(z))
print(list(z))# when u enter like this it will give empty list cause in the first line we gave print(list(z)) so all the elements come under this code so no elements left in the z function so it give the empty string
z=list(itertools.chain(*l1))#(it will give print multiple time cause we assigning z to list part so it will give multiple times)
print(z)
print(z)
l2=[1,23,[23,34,34],4,5,[34,56,45],6,4,["teja","vinod"], "raju","chandu","cnu"]
print(l2)
#flatten
flatten=[]
for i in l2:
    if type(i)==list:
        for j in i:
            flatten.append(j)
    else:
        flatten.append(i)
print(flatten)
l3=[[1,23,[23,34,34],4,5,[34,55,66,[34,56,45]],6,4,["teja",["cnu","raju","chandu"],"vinod"], "raju","chandu","cnu"],[1,23,[23,34,34],4,5,[34,55,66,[34,56,45]],6,4,["teja",["cnu","raju","chandu"],"vinod"], "raju","chandu","cnu"],[1,23,[23,34,34],4,5,[34,55,66,[34,56,45]],6,4,["teja",["cnu","raju","chandu"],"vinod"], "raju","chandu","cnu"]]
print(l3)
#flatten
for x in range(3):
    l4=[]
    for i in l3:
        if type(i)==list:
            for j in i:
                l4.append(j)
        else:
            l4.append(i)
        l3=l4
print(l3)
print(list1)
print(list2)
list2.append("d")
print(list2)
z=zip(list1,list2)
print(z)# it will shows the location of z
print(list(z))
print(list(zip(list1,list2)))
z=list(zip(list1,list2))
print(z)
for i in z:
    print(i)
for i in zip(list1,list2):
    print(i)
list5=["90","80","70","60"]
z=list(zip(list1,list2,list5))
print(z)
for i in zip(list1,list2,list5):
    print(i)
print(list1+list2)
l5=[34,55,66,34,56,45]
l6=[1,23,23,34,34,4]
for i in range(6):
    print(l5[i]+l6[i])
for i,j in zip(l5,l6):
    print(i+j)
print(list3)
list3.extend([60,66])
print(list3)
for i in range(6):
    print(l5[i]+l6[i]+list3[i])
for i in zip(l5,l6,list3):
    print(i)
for i,j,k in zip(l5,l6,list3):
    print(i+j+k)
z=zip(l5,l6)
print(list(z))
z=list(zip(l5,l6))
x,n=zip(*z)
print(x)
print(n)
l5.pop()
print(l5)
z=list(zip(l5,l6))
print(z)
m,n=zip(*z)
print(m)
print(n)
print(l5)
print(l6)
z=zip(l5,l6)
print(list(z))
l7=["cnu","raju","chandu","vinod"]
l8=["vinod", "raju","chandu","cnu"]
print(sorted(l7))
z=list(zip(l7,l8))
print(z)
print(sorted(z))
from collections import deque # we have special features in deque we append values left side.we can delete left side values but we dont have that type feature in simple list
print(l7)
dql7=deque(l7)
print(dql7)
dql7.append("teja")
print(dql7)
dql7.pop()
print(dql7)
dql7.appendleft("teja")
print(dql7)
dql7.extend(["raju","teja"])
print(dql7)
dql7.extendleft(["teja","raju"])
print(dql7)
dql7.rotate(2)# if u give positive sign it will rotate from right side to left side it means last value assign to frist and remaining values moves side by side
print(dql7)
dql7.rotate(-1)# if u give negative value then left side value assign to right side and  the left side next value moves to left side forward direction
print(dql7)
