#List crud operations

#Create to add list

#APPEND:

lst = ["deva","25"]
print(lst)

#insert :
names = ["de","pr","te"]
names.insert(2,"te")
print(names)

#to count

names = ["de","pr","te"]
print(names.count("de"))

#UPDATE
#1.by using index:

names = ["de","pr","te"]
names[1] = "sa"
print(names)

#2.by uisng insert:
#3.by using aappend
#both are same as previous.

#4.by using extend:

names = ["de","pr","te"]
names1 = ["re","kl","jk"]
names.extend(names1)
print(names)
print(names1)

#To Delete

#1.remove

names = ["de","pr","te"]
names.remove("pr")
print(names)

#2.pop with index:

names = ["de","pr","te"]
names.pop(0)
print(names)

#3.pop without index:

names = ["de","pr","te"]
names.pop()
names.pop()
print(names)