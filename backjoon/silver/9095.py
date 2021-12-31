"""
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""

import sys
n = int(input())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i==1:
        print(1)
    elif i==2:
        print(2)
    elif i==3:
        print(4)
    else:
        c1 = {"111","12","21","3"}
        c2 = {"11","2"}
        c3 = {"1"}
        for _ in range(3,i):
            tcache = set()
            for c in c1:
                tcache.add("1"+c)
                tcache.add(c+"1")
            for c in c2:
                tcache.add("2"+c)
                tcache.add(c+"2")
            for c in c3:
                tcache.add("3"+c)
                tcache.add(c+"3")
            c1,c2,c3 = tcache,c1,c2
        print(len(c1))
        