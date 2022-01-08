"""
문제
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

출력
각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.
"""

# def calc(start, end):
#     count = 0
#     cache = [[1,start]]
#     while cache:
#         print(cache)
#         new_cache = []
#         for k,now in cache:
#             if now == end:
#                 return count
#             max_speed = end-now
#             if k<=max_speed-(k+1):
#                 new_cache.append([k+1,now+k])
#             if (k-1)<=(max_speed-k):
#                 new_cache.append([k,now+k])
#             if k-1>0:
#                 new_cache.append([k-1,now+k])
#         cache = new_cache
#         count += 1

def calc(start, end):
    count = 1
    cache = [[1, start+1]]
    while cache:
        # print(cache)
        new_cache = []
        for k, now in cache:
            if now == end:
                return count

            # speed up
            left = end - now
            if left >= ((k+1)*(k+2)/2):
                new_cache.append([k+1,now+k+1])
                continue

            # speed same
            if left >= (k*(k+1)/2):
                new_cache.append([k,now+k])
                continue

            # speed down
            if k>1:
                new_cache.append([k-1, now+k-1])

        cache = new_cache
        count += 1


t = int(input())
for _ in range(t):
    start, end = map(int,input().split())
    print(calc(start, end))
