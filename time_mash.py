# newmatrix = []
# for n,i in enumerate(matrix[0]):# assuming the lists are in the same length
#
#     templist =[]
#     for l in matrix:
#
#         templist.append(l[n])
#     print "templist: ",n,"content: ",templist
#     newmatrix.append(templist)


list = [[1, 2, 3], [4, 4, 6], [7, 8, 9], [10, 11, 12]]


newmatrix = []
for n, i in enumerate(list[0]):# assuming the lists are in the same length

    templist =[]
    for l in list:

        templist.append(l[n])
    print("templist: ", n, "content: ", templist)
    newmatrix.append(templist)

for column in newmatrix:
    print(column)


print(list[2][1])
print(newmatrix[2][1])
print(newmatrix[1][2])


# list.reverse()
# print(list)
# print(list[1][1])
