"""수 찾기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	122446	36563	24180	30.086%
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

# n = int(input())
# nn = list(map(int,input().split()))
# m = int(input())
# mm = map(int, input().split())

# for m in mm:
#     if nn.count(m):
#         print(1)
#     else:
#         print(0)
# 시간초과

n = int(input())
a = set(map(int, input().split()))
m = int(input())
mm = list(map(int, input().split()))

result = set(mm).intersection(a)
for m in mm:
    if m in result:
        print(1)
    else:
        print(0)

