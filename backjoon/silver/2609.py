"""
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""



# cd = 0
# n = min(a,b)
# if n==1:
#     print(1)
#     print(max(a,b))
# else:
#     for i in range(1,n+1):
#         if a%i or b%i:
#             pass
#         else:
#             cd = i
#     print(cd)
#     cm = cd
#     while 1:
#         if cm%a or cm%b:
#             pass
#         else:
#             break
#         cm += cd
#     print(cm)
# 시간 초ㅏ
import sys
a,b = map(int, sys.stdin.readline().split())
a_dict = {1:1}
b_dict = {1:1}
div = 2
while a>1:
    if a%div:
        div += 1
    else:
        a = a//div
        a_dict[div] = a_dict.get(div, 0) + 1
div = 2
while b>1:
    if b%div:
        div += 1
    else:
        b = b//div
        b_dict[div] = b_dict.get(div, 0) + 1
cd = 1
cm = 1
for k in set(a_dict.keys()).union(set(b_dict.keys())):
    ak = a_dict.get(k,0)
    bk = b_dict.get(k,0)
    cd *= k**min(ak,bk)
    cm *= k**max(ak,bk)

print(cd, cm,sep='\n')
