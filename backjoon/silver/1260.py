"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""

n,m,v = map(int, input().split())
edges = {}
for _ in range(m):
    s,e = map(int,input().split())
    edges[s] = edges.get(s,set()).union({e})
    edges[e] = edges.get(e,set()).union({s})

# dfs
visited = []
def dfs(v,edges):
    global visited
    visited.append(v)
    for i in sorted(edges.get(v,[])):
        if i not in visited:
            dfs(i,edges)
dfs(v,edges)
print(" ".join(map(str,visited)))

# bfs
visited = [v]
def bfs(v,edges):
    global visited
    cache = [v]
    while cache:
        tcache = []
        for v in cache:
            for i in sorted(edges.get(v,[])):
                if i not in visited:
                    tcache.append(i)
                    visited.append(i)
        cache = tcache

bfs(v,edges)
print(" ".join(map(str,visited)))


# 일단 실패 ??


## 정답
# Depth First Search



#########################################################
# 틀린거 찾기
#########################################################



def mysol(n,m,v,se):
    ret = []
    edges = {}
    for s,e in se:
        edges[s] = edges.get(s,set()).union({e})
        edges[e] = edges.get(e,set()).union({s})

    # dfs
    visited = []
    def dfs(v,edges):
        nonlocal visited
        visited.append(v)
        for i in sorted(edges.get(v,[])):
            if i not in visited:
                dfs(i,edges)
    dfs(v,edges)
    ret.append(" ".join(map(str,visited)))

    # bfs
    visited = [v]
    def bfs(v,edges):
        nonlocal visited
        cache = [v]
        while cache:
            tcache = []
            for v in cache:
                for i in sorted(edges.get(v,[])):
                    if i not in visited:
                        tcache.append(i)
                        visited.append(i)
            cache = tcache

    bfs(v,edges)
    ret.append(" ".join(map(str,visited)))

    return ret

def solution(n,m,v,se):
    def dfs(n):
        nonlocal answer,visited,graph
        answer += f"{n} "
        visited[n] = True
        for i in graph[n]:
            if not visited[i]:
                dfs(i)

    # Breadth First Search
    def bfs(n):
        nonlocal answer,visited,graph
        visited[n] = True
        queue = deque([n])
        while queue:
            v = queue.popleft()
            answer += f"{v} "
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    from collections import deque

    # node, branch, first node
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)

    # make adjacency list
    for a,b in se:
        graph[a].append(b)
        graph[b].append(a)
    # sort adjacency list
    for i in range(1, n+1):
        graph[i].sort()
    answer = ""
    ret = []
    dfs(v)
    ret.append(answer[:-1])
    # initialize check list
    visited = [False] * (n + 1)
    answer = ""
    bfs(v)
    ret.append(answer[:-1])
    return ret


import random
# for _ in range(100):
#     n,m = random.choice(range(1,10)),random.choice(range(1,10))
#     if n >1:
#         v = random.choice(range(1,n+1))
#     else:
#         v = 1

#     se = []
#     for _ in range(m):
#         se.append(random.choices(range(1,n+1),k=2))
#     mret = mysol(n,m,v,se)
#     sret = solution(n,m,v,se)
#     if mret!=sret:
#         print(n,m,v)
#         print(se)
#         print(mret,sret)
#         break
n = 6
m = 9
v = 2
se = [[3,6],[4,2],[4,1],[1,5],[6,1],[4,2],[6,2]]
mret = mysol(n,m,v,se)
sret = solution(n,m,v,se)

print(mret, sret)
print("done")