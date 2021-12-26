l = list()
print(l)
l.append([1, 2])
print(l)

priority_list_in_line=[[1, 9], [5, 6], [5, 10], [8, 6]]

def one():
    print("one")

def two():
    print("two")

if priority_list_in_line != []:
    for pair in priority_list_in_line:
    # for line, index in priority_list_in_line:
        print(priority_list_in_line.index(pair))
        while (len(priority_list_in_line)-1) > priority_list_in_line.index(pair):
            one()
        two()

    print(len(priority_list_in_line) - 1)

