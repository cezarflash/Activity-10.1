__author__ = 'Ayla'


#Create a list m = [2, 4, 6, 8].
#1. Print the second element in the list.
m = [2,4,6,8]
print (m[1])
#2 Create a new list fivem that has the elements 10, 20, 30, 40. Multiply m by 5 for this using a for loop,
# do NOT just create the list using fivem = [10, 20, 30, 40].
for i in range (len(m)):
    m[i]=m[i]*5
print(m)
#3. Add 10 to the list m and print m.
m=[2,4,6,8]
m.append(10)
print(m)
#4. What happens if you add 6 to the list m? Do you get two 6’s or just one?
m=[2,4,6,8]
m.append(6)
print(m)
#5. Print the position of 8 in m.
m=[2,4,6,8]
print(m[3])
#6. Delete 8 from m and print the new list.
m=[2,4,6,8]
x=m.pop(3)
print(m)