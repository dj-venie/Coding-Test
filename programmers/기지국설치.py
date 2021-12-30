"""
N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 
기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 
그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.
예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다. 
(전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)"""

# N	stations	W	answer
# 11	[4, 11]	1	3
# 16	[9]	2	3
test_case = [[11,[4, 11],1,3],[16,[15],2,3],[11,[],5,1],[1,[],1,1],[6,[],2,2]]

# def solution(N, stations, W):
#     cover_block = 2*W + 1
#     if stations==[]:
#         return N//cover_block + 1

#     result = 0
#     no_zone = 0

#     next_stations = stations.pop(0)
#     for i in range(1,N+1):
        
#         if i == next_stations:
#             no_zone -= W
#             result += no_zone//cover_block + bool(no_zone%cover_block)
#             if stations:
#                 next_stations = stations.pop(0)
#                 no_zone = -W
#             else:
#                 if i + W < N:
#                     result += (N-i-W)//cover_block + bool((N-i-W)%cover_block)
#                 return result
#         else:
#             no_zone += 1
#     return result

def solution(N, stations, W):
    cover_block = 2*W + 1
    result = 0
    before = 1
    while stations:
        now = stations.pop(0)
        gap = now - before - W
        if gap > 0:
            result += gap//cover_block + bool(gap%cover_block)
        before = now + W + 1

    if before <= N:
        gap = N-before+1
        result += gap//cover_block + bool(gap%cover_block)

    return result



for tc in test_case:
    N,stations,W,answer = tc
    result = solution(N,stations,W) 
    print(result, answer, result==answer)
