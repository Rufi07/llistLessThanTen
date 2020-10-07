# create a program that will filter out items of a list that are less than 5 and print them out.
# afterwards print them out in an ordered list.
# add an element to accept an input that becomes the filter point

a = [2, 1, 4, 3, 5, 8, 13, 21, 35, 45]
b =[]

num = int(input("What number should be the upper limit for our list?"))
for element in a:
    while element < num:
        b.append(element)
        b.sort()
        break

print(b)

#sort() to sort into order later?