"""
문제
홍윤이는 구간을 좋아한다. 홍윤이는 비트연산자도 좋아한다. 그래서 구간과 비트연산자를 합친 문제를 만들었다.

크기 $N$의 배열 $A$에서 연속한 구간을 잡아 내부의 값들을 전부 bitwise or 했을 때, 값이 정확히 $K$가 되는 구간을 구하시오. 만약 가능한 구간이 여러 개 있을 경우 그들 중 아무거나 선택해도 좋다.

입력
첫째 줄에 $N$과 $K$이 주어진다. ($1 \leq N \leq 200,000$, $1 \leq K \leq 2^{30}-1$)

둘째 줄에 길이 $N$의 배열 $A$이 주어진다. ($1 \leq A_i \leq 2^{30}-1$)

출력
왼쪽에서 $s$번째부터 $e$번째 수까지의 구간이 조건을 만족한다면, 한 줄에 $s$와 $e$를 공백으로 구분하여 출력한다. 만약 그러한 구간이 존재하지 않으면 대신 -1을 출력한다.
"""

n,k = map(int, input().split())
a = list(map(int, input().split()))

answer = 0                             
start = 0
idx = 0
flag = 0
now = 0
while idx<len(a):
    now|=a[idx]
    if k==now:
        answer = [start+1, idx+1]
        break
    elif k|now==k:
        idx += 1
    else:
        now = 0
        idx += 1
        start = idx

if answer:
    print(answer[0], answer[1])
else:
    print(-1)
