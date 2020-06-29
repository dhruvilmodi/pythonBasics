# print hello world
print("Hello World")

# if else condition
if 5 > 2:
    print("5 is greater than 2")
else:
    print("2 is greater than 5")

# variables
x = 5
y = "Good"
print(x)
print(y)

# multiple variables
a, b, c = "Dhruvil", "Ashokkumar", "Modi"
print(a)
print(b)
print(c)

# defining same value if variables
d = e = f = "Iron Man"
print(d)
print(e)
print(f)

# concatinating variable
g = "Games"
print("Dhruvil love " + g)

# function
def myFunc():
    print(d + " " + g)
myFunc()

# global variable
def globalVar():
    global h
    h = "happy"
globalVar()
print("I am " + h)

# set
thisset = {"Apple","Mango","Pineapple"}

# for loop
for j in thisset:
    print(j)

# add() into set
thisset.add("Orange")
print(thisset)

# remove() from set
thisset.remove("Apple")
print(thisset)

# discard() from set
thisset.discard("Orange")
print(thisset)

# pop() will remove the last item
l = thisset.pop()
print(l)
print(thisset)

# clear() will empty set
thisset.clear()
print(thisset)

# del will delete set
del thisset

# union() will join two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update() will add items
set1.update(set2)
print(set1)