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
    
    for i in range(len(tableData[0])):          # 1 à 4
        for j in range(len(tableData)):         # 1 à 3            # padding += table_width[j]
            print(tableData[j][i].rjust(table_width[j] + 2), end='')
        print()


print_table(tableData)
