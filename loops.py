#for loops
seq = [1,2,3,4,6,7,8,9]
for item in seq:
	print(item)



#for in dic

d = {"sam":1,"frank":2,"dan":3}

for k in d:
     print(k)
     print(d[k])


#tupels
mypairs = [(1,2),(3,4),(6,7)]

for item in mypairs:
       print(item)     

for tup1,tup2 in mypairs:
      print(tup2)
      print(tup1)     


      #while loops

 i=1
 while i<6:
        print("i is: {}".format(i))
        i=i+1 


 #range
 for item in range(10):

 print(item)

 #list comprehansion

 x= [1,2,3,4]

 out = [num**2 for num in x]
 print(out)           
