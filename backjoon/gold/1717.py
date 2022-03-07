"""문제
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

출력
1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)"""

# class Node:
#     def __init__(self, n):
#         self.set = {n}
# i = Node(1)

# n,m = map(int, input().split())

# set_dict = {i:Node(i) for i in range(n+1)}

# for _ in range(m):
#     c,a,b = map(int, input().split())
#     if c:
#         if a in set_dict[b].set:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         union = set_dict[a].set.union(set_dict[b].set)
#         set_dict[a].set = union
#         set_dict[b].set = union
# 메모리 부족

# n,m = map(int, input().split())

# s_list = [i for i in range(n+1)]
# for _ in range(m):
#     c,a,b = map(int, input().split())
#     if c:
#         if s_list[a] == s_list[b]:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         if s_list[a]==s_list[b]:
#             pass
#         else:
#             A = s_list[a]
#             B = s_list[b]
#             for idx,s in enumerate(s_list):
#                 if s==B:
#                     s_list[idx]=A
# 시간 초과

# import sys
# n,m = map(int, sys.stdin.readline().split())

# s_list = [i for i in range(n+1)]

# def find(n):
#     if s_list[n]==n:
#         return n
#     else:
#         return find(s_list[n])

# for _ in range(m):
#     c,a,b = map(int, sys.stdin.readline().split())
#     if c:
#         if find(a)==find(b):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         fa = find(a)
#         fb = find(b)
#         if fa!=fb:
#             s_list[fb] = fa
# 재귀 에러


# import sys
# n,m = map(int, sys.stdin.readline().split())

# s_list = [i for i in range(n+1)]

# def find(n):
#     while s_list[n]!=n:
#         n = s_list[n]
#     return n

# for _ in range(m):
#     c,a,b = map(int, sys.stdin.readline().split())
#     if c:
#         if a==b:
#             print('YES')
#         elif find(a)==find(b):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         if a==b:
#             continue
#         fa = find(a)
#         fb = find(b)
#         if fa!=fb:
#             s_list[fb] = fa
# 시간초과

# import sys
# n,m = map(int, sys.stdin.readline().split())

# s_list = [i for i in range(n+1)]

# def find(a,b):
#     while s_list[a]!=a:
#         a = s_list[a]
#         if a==b:
#             return True

#     while s_list[b]!=b:
#         b = s_list[b]
#     if a==b:
#         return True
#     return a,b

# for _ in range(m):
#     c,a,b = map(int, sys.stdin.readline().split())
#     if c:
#         if a==b:
#             print('YES')
#         elif find(a,b)==True:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         if a==b:
#             continue
#         ret = find(a,b)
#         if ret!=True:
#             s_list[ret[0]] = ret[1]


import sys
n,m = map(int, sys.stdin.readline().split())

s_list = [i for i in range(n+1)]

def find(n):
    if s_list[n]==n:
        return n
    ret = find(s_list[n])
    s_list[n] = ret
    return ret

for _ in range(m):
    c,a,b = map(int, sys.stdin.readline().split())
    if c:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
    else:
        fa = find(a)
        fb = find(b)
        if fa!=fb:
            s_list[fb] = fa
