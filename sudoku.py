# 解数独的程序
# 有两个步骤，第一步用于推断出所有必然的数字，第二步用于猜测一个数字看是否得出结果
# 首先应该写一个判断数独是否完成的函数，如果第一步完成，则不需要执行第二步
# 第二步的猜测需要保留第一步的进度，直到解出数独

from copy import deepcopy

table_unfinished = [[0,1,0,0,6,0,0,9,0],[0,0,9,4,0,0,3,0,0],[5,0,0,0,7,0,0,0,2],[0,0,0,0,0,0,6,0,9],[1,0,6,0,0,0,0,0,0],[0,7,0,6,0,0,0,4,0],[0,0,4,5,0,0,8,0,0],[0,8,0,0,0,6,0,7,0],[2,0,0,0,0,8,0,0,1]]

#----------------------------------------------------
#输入输出

def print_table(table, pow = 9):
    print('-'*25)
    for i in range(pow):
        print('|', end=' ')
        for j in range(3):
            print(table[i][j*3],table[i][j*3+1],table[i][j*3+2],'|', end=' ')
        print()
        if i%3 == 2:
            print('-'*25)

def input_table(pow = 9):
    print('input the sudoku line by line, using 0 instead of the blank cell')
    print('for example: 029400600 enter:')
    table = []
    for i in range(pow):
        line_str = input()
        lint_int = [int(x) for x in line_str]
        table.append(lint_int)
    return table

#-----------------------------------------------------------
#检查是否正确

def check_row_finished(table, row_number, pow = 9):
    temp_row = sorted(table[row_number])
    if temp_row == list(range(1,pow+1)):
        return True
    return False

def check_col_finished(table, col_number, pow = 9):
    temp_col = sorted([table[i][col_number] for i in range(pow)])
    if temp_col == list(range(1,pow+1)):
        return True
    return False

def check_unit_finished(table, unit_index, pow = 9):
    [r,s] = unit_index
    temp_unit = sorted([table[r*3 + i][s*3 + j] for i in range(3) for j in range(3)])
    if temp_unit == list(range(1,pow+1)):
        return True
    return False

# 测试数独填充完成之后是否有错误
def check_table(table, pow = 9):
    for i in range(9):
        if not check_row_finished(table, i):
            return False
    for i in range(9):
        if not check_col_finished(table, i):
            return False
    for i in range(9):
        if not check_unit_finished(table, [i//3, i%3]):
            return False
    return True

#--------------------------------------------------------
#检查是否完成

def is_finish(table, pow = 9):
    for i in range(pow):
        for j in range(pow):
            if table[i][j] == 0:
                return False
    return True

#--------------------------------------------------------
#生成可能的数字

def in_row(table, n, row_number, pow = 9):
    return n in table[row_number]

def in_col(table, n, col_number, pow = 9):
    return n in [table[i][col_number] for i in range(pow)]

def in_unit(table, n, unit_index, pow = 9):
    [r,s] = unit_index
    return n in [table[r*3 + i][s*3 + j] for i in range(3) for j in range(3)]

def possible_numbers_of_cell(table, cell_index, pow = 9):
    [x,y] = cell_index
    cell = []
    if table[x][y] != 0:
        return cell
    for n in list(range(1,pow+1)):
        if in_row(table, n, x) or in_col(table, n, y) or in_unit(table, n, [x//3,y//3]):
            continue
        else:
            cell.append(n)
    return cell

def all_possible_numbers(table, pow = 9):
    possible_numbers_table = []
    for i in range(pow):
        possible_numbers_table.append([])
        for j in range(pow):
            cell = possible_numbers_of_cell(table, [i,j])
            possible_numbers_table[i].append(cell)
    return possible_numbers_table

#----------------------------------------------------------------
#推断一个cell中的数字
def number_of_cell(possible_numbers_table, cell_index, pow = 9):
    [x,y] = cell_index
    temp_list = possible_numbers_table[x][y]
    if len(temp_list) == 1:
        return temp_list[0]
    #by row
    for n in list(range(1,pow+1)):
        show_once = False
        show_twice = False
        for i in range(9):
            if n in possible_numbers_table[x][y]:
                if show_once:
                    show_twice = True
                show_once = True
        if show_once and (not show_twice):
            return n
    #by col
    for n in possible_numbers_table[x][y]:
        show_once = False
        show_twice = False
        for i in range(9):
            if n in possible_numbers_table[i][y]:
                if show_once:
                    show_twice = True
                show_once = True
        if show_once and (not show_twice):
            return n
    #by unit
    r = x // 3
    s = y // 3
    for n in possible_numbers_table[x][y]:
        show_once = False
        show_twice = False
        for i in range(3):
            for j in range(3):
                if n in possible_numbers_table[r*3+i][s*3+j]:
                    if show_once:
                        show_twice = True
                    show_once = True
        if show_once and (not show_twice):
            return n
    return 0

#-------------------------------------------------------
#生成尝试序列
def get_the_try_table(possible_numbers_table):
    cell_had_tyied = [[False]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if possible_numbers_table[i][j] == []:
                cell_had_tyied[i][j] = True
    return cell_had_tyied

#---------------------------------------------------------------
#寻找最小的可能序列
def min_list_of_possible_numbers(possible_numbers_table, cell_had_tyied, pow = 9):
    [x, y] = [0, 0]
    length = pow
    for i in range(pow):
        for j in range(pow):
            if cell_had_tyied[i][j]:
                continue
            temp_length = len(possible_numbers_table[i][j])
            if temp_length == 0:
                continue
            if temp_length < length:
                x = i
                y = j
                length = temp_length
    if length == pow:
        for i in range(pow):
            for j in range(pow):
                if cell_had_tyied[i][j]:
                    continue
                if len(possible_numbers_table[i][j]) != 0:
                    x = i
                    y = j
                    break
    cell_had_tyied[x][y] = True
    return[[x,y], length]

#---------------------------------------------------------------
#第一步，直推
def step_one(table, pow = 9):
    change_flag = False
    possible_numbers_table = all_possible_numbers(table)
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0:
                continue
            n = number_of_cell(possible_numbers_table, [i,j])
            if n == 0:
                continue
            else:
                table[i][j] = n
                change_flag = True
    return change_flag

#--------------------------------------------------------------
#第二步，猜测
def step_two(table, pow = 9):
    possible_numbers_table = all_possible_numbers(table)
    cell_had_tyied = get_the_try_table(possible_numbers_table)
    [guess_list_index, guess_list_length] = min_list_of_possible_numbers(possible_numbers_table, cell_had_tyied)
    [x,y] = guess_list_index
    temp_table = table
    flag_all_try = False
    for i in range(9):
        for j in range(9):
            flag_all_try = flag_all_try and cell_had_tyied[i][j]
    if flag_all_try:
        return table
    for n in possible_numbers_table[x][y]:
        temp_table = deepcopy(table)
        temp_table[x][y] = n
        while step_one(temp_table):
            pass
        if is_finish(temp_table):
            if check_table(temp_table):
                return temp_table
            else:
                continue
        else:
            temp_table = step_two(temp_table)
            if temp_table == None:
                continue
            return temp_table

# ---------------------------------------------------------------
#test

table = table_unfinished
table = input_table()
print_table(table)

while step_one(table):
    pass

if not is_finish(table):
    table = step_two(table)

print('the result is:')
print_table(table)
