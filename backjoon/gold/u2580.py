# -*- coding: utf-8 -*-

"""
문제
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.



나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.



또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.



이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.



게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
"""
# sudoku = []
# for _ in range(9):
#     sudoku.append(list(map(int,input().split())))

# zeros = {}
# for i in range(9):
#     for j in range(9):
#         if sudoku[i][j]==0:
#             zeros[(i,j)] = set(range(1,10))
# while zeros:

#     # vertical check
#     for j in range(9):
#         numbers = set(range(1,10))
#         t_zero = []
#         for i in range(9):
#             now = sudoku[i][j]
#             if now:
#                 numbers.remove(now)
#             else:
#                 t_zero.append((i,j))
#         for zero in t_zero:
#             zeros[zero].intersection_update(numbers)

#     # horizontal check
#     for i in range(9):
#         numbers = set(range(1,10))
#         t_zero = []
#         for j in range(9):
#             now = sudoku[i][j]
#             if now:
#                 numbers.remove(now)
#             else:
#                 t_zero.append((i,j))
#         for zero in t_zero:
#             zeros[zero].intersection_update(numbers)

#     # box check
#     for i in range(9):
#         numbers = set(range(1,10))
#         t_zero = []

#         box_y = (i//3)*3
#         box_x = (i%3)*3
#         for j in range(9):

#             now_y = (j//3)
#             now_x = (j%3)
            
#             y,x = box_y+now_y, box_x+now_x
#             now = sudoku[y][x]
#             if now:
#                 numbers.remove(now)
#             else:
#                 t_zero.append((y,x))

#         for zero in t_zero:
#             zeros[zero].intersection_update(numbers)
#     new_zeros = {}
#     for zero, cand in zeros.items():
#         if len(cand)==1:
#             y,x = zero
#             sudoku[y][x] = cand.pop()

#         else:
#             new_zeros[zero] = cand
#     zeros = new_zeros

# for line in sudoku:
#     print(" ".join(map(str,line)))
# 전부 빈칸인 경우 해결x

# sudoku = []
# for _ in range(9):
#     sudoku.append(list(map(int,input().split())))

# def find(sudoku, x,y):
#     while y<9:
#         if sudoku[y][x]:
#             x,y = (x+1)%9, y+(x+1)//9
#         else:
#             break

#     if y==9:
#         return sudoku
#     nx,ny = (x+1)%9, y+(x+1)//9
#     sudoku = [s.copy() for s in sudoku]
#     cand = set(range(1,10))

#     # check horizontal
#     cand -= set(sudoku[y])

#     # check vertical
#     v = set()
#     for i in range(9):
#         v.add(sudoku[i][x])
#     cand -= v

#     # check box
#     b = set()
#     box_x = (x//3)*3
#     box_y = (y//3)*3

#     for i in range(3):
#         for j in range(3):
#             b.add(sudoku[box_y+j][box_x+i])
#     cand -= b
#     for c in cand:
#         sudoku[y][x] = c
#         ret = find(sudoku, nx, ny)
#         if ret:
#             return ret

#     return False

# sudoku = find(sudoku, 0,0)

# for line in sudoku:
#     print(" ".join(map(str,line)))

# # 시간 초과?

import sys
input = sys.stdin.readline
sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

#check
h_list = []
v_list = []
box_list = []
temp = set(i for i in range(1,10))
for i in range(9):
    # v check
    v_list.append(temp - set(sudoku[i]))

    # h check
    htemp = set()
    for j in range(9):
        htemp.add(sudoku[j][i])
    h_list.append(temp - htemp)

    # box check
    btemp = set()
    bx,by = i%3, i//3
    for j in range(9):
        bxx,byy = j%3, j//3
        btemp.add(sudoku[3*by+byy][3*bx+bxx])
    box_list.append(temp-btemp)

cand = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            v = v_list[i]
            h = h_list[j]
            b = box_list[(j//3)*3 + (i//3)]

            now = v.intersection(h).intersection(b)
            if len(now)==1:
                n = now.pop()
                v.remove(n)
                h.remove(n)
                b.remove(n)
                sudoku[i][j] = n
print(sudoku)