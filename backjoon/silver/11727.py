"""
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

n = int(input())
if n==1:
    print(1)
elif n==2:
    print(3)
else:
    b1 = 3
    b2 = 1
    for _ in range(2,n):
        b1,b2 = b2*2+b1, b1

    print(b1%10007) 