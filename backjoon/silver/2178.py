"""
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""
h,w = map(int, input().split())
mat = []
for _ in range(h):
    mat.append(list(map(int, input())))

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    cache = [(0,0)]
    count = 1
    while cache:
        tcache = []
        for x,y in cache:
            if (x,y)==(h-1,w-1):
                return count
            # check up
            if x-1>=0:
                if maps[x-1][y]:
                    tcache.append((x-1,y))
                    maps[x-1][y]=0
            # check down
            if x+1<h:
                if maps[x+1][y]:
                    tcache.append((x+1,y))
                    maps[x+1][y]=0

            # check left
            if y-1>=0:
                if maps[x][y-1]:
                    tcache.append((x,y-1))
                    maps[x][y-1]=0
            # check right
            if y+1<w:
                if maps[x][y+1]:
                    tcache.append((x,y+1))
                    maps[x][y+1]=0
        cache = tcache
        count += 1
    return -1

print(solution(mat))