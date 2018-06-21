# A program that takes a list of strings and displays it in
# a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.


def table_printer(collection):
    width = max(len(tableData[i][j]) for i in range(len(tableData)) for j in range(len(tableData[0])))

    for i in range(len(tableData[0])):
        for column in tableData:
            print(f"{column[i]:>{width}}", end="")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

table_printer(tableData)
