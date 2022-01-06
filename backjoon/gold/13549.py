"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""

# n,k = map(int, input().split())
# def find(n,k):
#     cache = [n]
#     visited = [n]
#     count = 0
#     while 1:
#         tcache = []
#         for c in cache:
#             if c==k:
#                 return count
#             if c-1 not in visited:
#                 tcache.append(c-1)
#                 visited.append(c-1)
#             if c+1 not in visited:
#                 tcache.append(c+1)
#                 visited.append(c+1)
#             if c*2 not in visited:
#                 tcache.append(c*2)
#                 visited.append(c*2)
#         cache = tcache
#         count += 1
# print(find(n,k))

n,k = map(int, input().split())
def find(n,k):
    result = 0
    if n>=k:
        return n-k

    if n < (k//2):
        return k%2+find(n,k//2)
    else:
        if n-k//2 > k-n:
            return k-n
        else:
            return n-k//2 + k%2
print(find(n,k))
# 5 31 : 2

# n,k = map(int, input().split())
# def find(n,k):
#     if n>=k:
#         return n-k
#     cache = {n}
#     count = 0
#     while 1:
#         new_cache = set()
#         for c in cache:
#             if c==0:
#                 new_cache.add(c)
#                 continue
#             while c<=100000:
#                 new_cache.add(c)
#                 c*=2
#         tcache = set()
#         for c in new_cache:
#             if c==k:
#                 return count
#             if c>1:
#                 tcache.add(c-1)
#             tcache.add(c+1)
#         cache = tcache
#         count += 1  

# print(find(n,k))
# 시간 초과
n,k = map(int, input().split())
def find(n,k):
    if n>=k:
        return n-k
    
    cache = [k]
    visited = {k}
    count = 0
    while 1:
        for c in cache:
            if c%2:
                pass
            elif c>1:
                cache.append(c//2)
        new_cache = set()
        for c in cache:
            if c == n:
                return count
            if (c>0) and (c-1 not in visited):
                new_cache.add(c-1)
                visited.add(c-1)
            if (c<100000) and (c+1 not in visited):
                new_cache.add(c+1)
                visited.add(c+1)
        cache = list(new_cache)
        count += 1

print(find(n,k))

# n,k = map(int, input().split())
# def find(n,k):
#     if n>=k:
#         return n-k
    
#     cache = [k]
#     visited = [k]
#     count = 0
#     while 1:
#         for c in cache:
#             if c%2:
#                 pass
#             elif c>1:
#                 cache.append(c//2)
#         new_cache = set()
#         for c in cache:
#             if c == n:
#                 return count
#             if (c>0) and (c-1 not in visited):
#                 new_cache.add(c-1)
#                 visited.append(c-1)
#             if (c<100000) and (c+1 not in visited):
#                 new_cache.add(c+1)
#                 visited.append(c+1)
#         cache = list(new_cache)
#         count += 1

# print(find(n,k))
# list check 속도 느림
