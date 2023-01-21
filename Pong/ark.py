def hate_all_hedgehogs(list_orders: list[str]):

    list_n: list[int] = []

    print(list_orders)
    for line in list_orders:

        if "append" in line:
            # line = "append 1"
            list_n.append(line[1])
        elif "insert" in line:
            list_n.insert(line[1], line[2])
        elif "remove" in line:
            list_n.remove(line[1])
        elif "sort" in line:
            list_n.sort()
        elif "pop" in line:
            list_n.pop()
        elif "reverse" in line:
            list_n.reverse()
        elif "print" in line:
            print(list_n)


hate_all_hedgehogs(list(['insert 0 5',
           'insert 1 10',
           'insert 0 6',
           'print',
           'remove 6',
           'append 9',
           'append 1',
           'sort',
           'print',
           'pop',
           'reverse',
           'print'
           ]))
