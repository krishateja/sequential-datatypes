#dictionaries key value pair  and maping mechanisum
d1={"a":1,1:"apple","b":2,2:"bal"}#key should be unique and values may  be duplicate
# the first element is called  key and second element is called value and (key and value) both elements together is called item
print(d1)
print(type(d1))
d2={}# this is not set it is dictionary
print(d2)
print(type(d2))
d3=dict(a="apple",b=2,c="apple")#when we using assigning values  key values should be char
print(d3)
d4=dict([("a","apple"),("b","ball"),(3,"cat")])
print(d4)
d=dict([("a","apple"),("b","ball"),(3,"cat")],c="raju",d=1)
print(d)
#dd=dict(e="apple",f=4,[("a","apple"),("b","ball"),(3,"cat")])
#when we creating dictionary by using dict() we have to create first list with nested tuple follows assigning
#if u create assigning first and follows listwith nested tuple it will show error
#print(dd)#SyntaxError: positional argument follows keyword argument
print(d1)
# input order is not preserved so we dont have the indeses and slicing
# if we want read the values by using key's
print(d1["a"])
print(d1["b"])
print(d1[2])
#print(d1[3]) we dont have key 3 it shows error
d1[3]="teja"#updation of d1 by key element
print(d1)
d1[2]=222#replace value of key
print(d1)
print(d1.get(2))#by using get() we can read the data
#print(d1.get(c))#in d1 we dont have c so it will show error
print(d1.get("c","no such value"))#hear we dont have key like c so we get output like no such data
print(d1)#we dont get the key and value bcz its not setdefault
print(d1.get(3,"no such value"))#here we have the key so direclty it will show value
print(d1.setdefault(3))#by using setdefault we can read data
print(d1.setdefault("e","no such value"))
print(d1.setdefault("f","srinivas"))#directly it will add key and value to dictionary
print(d1)
print(d1.pop("e"))
print(d1)
print(d1.pop(2))
print(d1.popitem())
print(d1)
print(d1.items())
print(d1.keys())
print(d1.values())
print(d1.clear())
print(d1)
del d1
print(d3)
d3["d"]="ball"
d3["e"]="teja"
print(d3)
for i in d3:#by default it will take key values
    print(i)
for i in d3.keys():
    print(i)
for i in d3.values():
    print(i)
for i in d3.items():
    print(i)
for i,j in d3.items():
    print(i,end=":")
    print(j)
d5=dict([("name",[]),("id",[]),("marks",{})])
print(d5)
d5["name"].append("teja")
print(d5)
d5["name"].extend(["raju","srinivas"])
d5["name"].pop(1)
d5["name"].pop(1)
print(d5["name"])
print(d5["id"])
d5["id"].extend([111,222,333])
print(d5)
d5["id"].pop()
d5["id"].pop()
d5["marks"]["english"]=77
d5["marks"].setdefault("maths",99)
d5["marks"]["stats"]=88
print(d5)
d5["total"]=d5["marks"]["english"]+d5["marks"]["maths"]+d5["marks"]["stats"]
print(d5)
d5["avg"]=d5["total"]/3
print(d5)
d6=dict({("a",1),("b",2),(3,"teja")})
print(d6)
list1=["apple","banana","orange","mango"]
dd1={}
for i in range(len(list1)):
    dd1[i+1]=list1[i]
print(dd1)
d1={}
for i in range(len(list1)):
    d1[list1[i][0]]=list1[i]
print(d1)
d1={"name":"teja","id":1111,"course":"btech"}
d2=d1# reference copy  it will same the memory loction if u change in one dictionary both will be effected
print(d2)
print(d1)
print(id(d1))
print(id(d2))
d1["location"]="hyd"
print(d1)
print(d2)
d1={'name': 'teja', 'id': 1111, 'course': 'btech', 'location': 'hyd'}
d2=d1.copy()#in shallow copy id's different for both dictonaries  if u change in one dictionary the second dictionary will not effected but nested dictionaries have the same id's
print(d1)
print(d2)
print(id(d1))
print(id(d2))
d1["marks"]={}
print(d1)
print(d2)
d3=dict(d1)#second type of shallow copy
print(d3)
print(d1)
print(id(d1))
print(id(d3))
print(id(d1["marks"]))
print(id(d3["marks"]))
d1["marks"]=[("english",77),("maths",88),("stats",99)]
d1["college"]="bhavans"
print(d1)
print(d3)
import copy#third type of shallow copy
d4=copy.copy(d1)
print(d1)
print(d4)
print(id(d1))
print(id(d4))
print(id(d1["marks"]))
print(id(d1["marks"]))
d1["marks"].append(("hindi",66))
print(d1)
print(d2)
# fourth and fifth type of shallow copies d2={**d1},d2=dict(**d1)
#deep copy in that both dictionaries memory location different and nested dictionaries memory loction also different
import copy
d5=copy.deepcopy(d1)
print(d5)
print(d1)
print(id(d1))
print(id(d5))
print(id(d1["marks"]))
print(id(d5["marks"]))
d1["marks"].append(("science",89))
print(d1)
print(d5)
d1={"A":"apple","B":"bat","C":"car"}
d1.update(D="dog")
print(d1)
d2={1:"car",2:"apple",3:"bat"}
print(d2)
d1.update(d=dict(one=1,two=2,three=3))
print(d1)
d1.update([("r","raju"),("t","teja"),("V","vinod")])
print(d1)
d1.update((("c","chandu"),))
d1.update({("s","srinivas")})
print(d1)
d2.update(d1)
print(d2)
print(d1)
d1={"A":"apple","B":"bat","C":"car"}
d1.update(D="dog")
print(d1)
d2={1:"car",2:"apple",3:"bat"}
print(d2)
for i in d1:
    print(i)
for i in d1,d2:
    print(i)
d3={}
for i in d1,d2:
    d3.update(i)
print(d3)
print({**d1, **d2})
#print(dict(**d1,**d2))#TypeError: keywords must be strings
d3={"v":"teja","x":"krishna","z":"moturi"}
print(dict(**d1,**d3))
import itertools
z=itertools.chain(d1.items(),d2.items())
print(dict(z))
a=dict(itertools.chain(d1.items(),d2.items()))
print(a)
import collections
#b=dict(collections.chainmap(d1,d2)) doubt
#print(b)
list=[1,2,3,4]
x=1234
print(dict.fromkeys(list,x))