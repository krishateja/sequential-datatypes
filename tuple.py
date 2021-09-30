#tuple is nothing but list but immutable and holds hetrogenious values and
#   tuple is immutable so we can't do all operations
#we can't delete single value from tuple is not possible but we can delete total tuule is possible

a=100
print(a)
print(type(a))
a=100,# if u put , in variable declataion it will convert tuple in this we can use single values  or more then one values
print(a)
print(type(a))#this  is one type of creation of tuple
a=100,200,300
print(a)
print(type(a))# this is second type of creation of tuple
a=(100,200,3000)
print(a)
print(type(a))# this is third type of creation of tuple
a=("orange",100,10.5)# tuple can hold hetro genious values
print(a)
print(type(a))
a="orange"
b=100
c=10.5
#print(tuple(a,b,c)) tuple takes atmost one value
print(tuple([a,b,c]))
t=a,b,c
print(t)
print(type(t))
#() can't required for creation of tuple we given multiple exmaples below
list=[100]
print(list)
print(type(list))
a=100
print(a)
print(type(a))
b="string"
print(b)
print(type(b))
c=100,# if u give any datatype no problem but if u put , by its side it will convert to tuple
d="string",#here we can't use() symbol
e=10.5,
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
# in tuple input order is preserved so we can do slicing method and indexing method for reading data
#and we can forloop also for reading data from tuple
tpl=(100,"teja",100,100.5,100)#in this tuple given different datatypes(hetrogenious)
print(tpl)#and duplication allowed
print(tpl[2])#we use indexing method
print(tpl[1:3])#we use slicing method
t3=(100,200,300,400,"teja","chandu",10.5)
for i in t3:
    print(i)
# we have few specification function because tuple is immutable
print(tpl.index(100))
print(tpl.count(100))
# we use generic funtions
print(len(tpl))
t1=100,200,300,400
print(max(t1))
print(min(t1))
print(sum(t1))
print(all(t1))# all funtion will check whether the given datatype is true or not if all true gives true if any one false in the tuple gives false
print(any(t1))# any function will check if any one datatype is true in tuple then it gives true it gives false when all the values will be false
t2=("teja",100,10.5,"")
print(t2)
print(all(t2))#in t2 we have empty string so it will give false
print(any(t2))
a=100
b=200
c=300
print(a)
print(id(a))
print(c)
print(id(c))
print(b)
print(id(b))
t4=(a,b,c)
print(t4)
print(id(t4))
x,y,z=t4
print(x)
print(y)
print(z)
str="we r going to new room"
e=tuple(str)
print(e)
t4=(10,20,30,40,50)
a,*b=t4# * will give u list
print(a)
print(b)
print(b[3])
*a,b=t4
print(a)
print(a[2])
print(b)
a,*b,c=t4
print(a)
print(b)
print(c)
#*a=t4we can't give single variable we give atleast two variables
#if u want give single variable we can use like this
[*b]=t4
print(b)
*b,=t4
print(b)
# we can.t append in tuple if u want append u can convert tuple to list and again convert to list to tuple
t4=(10,20,30,40,50)
lt=list(t4)
print(lt)
lt.append(60)
print(lt)
t4=tuple(lt)
print(t4)
t5=(100,200,300,400,500)
print(t4+t5)
l1=[]
for i in range (5):
    l1.append(t4[i]+t5[i])
print(l1)
t6=tuple(l1)
print(t6)
t7=("teja","raju",[10,20,30],50,(66,77,"chandu"),88,("cnu","vinod",12.2))
print(t7)
print(t7[2])
print(t7[2].append(60))
print(t7)
l2=[]
for i in t7:
    if type(i)==list or type(i)==tuple:
        for j in i:
            l2.append(j)
    else:
        l2.append(i)
print(l2)
t7=tuple(l2)
print(t7)


