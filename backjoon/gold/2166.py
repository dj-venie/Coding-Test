"""
문제
2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

출력
첫째 줄에 면적을 출력한다. 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.
"""
n = int(input())

points = []
for _ in range(n):
    points.append(tuple(map(int,input().split())))

before = points[-1]
l = 0
r = 0
for p in points:
    l += before[0]*p[1]
    r += before[1]*p[0]
    before = p

print(round(abs(l-r)/2,2))

