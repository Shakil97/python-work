
#list
mylist = [4,2,7,6]
mylistTwo = ["x","y","z"]
item = mylist.pop()
mylist.reverse()
mylist.sort()
mylist.appand(["x","y","z"])
mylist.extand(mylistTwo)
print(mylist)
print(item)

#nasted list

mylist = [1,2 ["x","y","z"]]
print(mylist[2][1])

#list comprehansion

matrix = [[1,2,3],[4,6,7],[8,9,0]]
first_col = [row [0] for row in matrix]
print(first_col)