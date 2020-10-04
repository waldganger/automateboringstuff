#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    table_width = []
    for c in tableData:
        max = 0
        for el in c:
            if len(el) > max:
                max = len(el)
        table_width.append(max)
    
    # return table_width

print(print_table(tableData))
