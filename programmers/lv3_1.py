"""
문제 설명
N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.
스티커_hb1jty.jpg
원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.

제한 사항
sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.
원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

sticker	answer
[14, 6, 5, 11, 3, 9, 2, 10]	36
[1, 3, 2, 5, 4]	8
"""

def solution(sticker):
    answer = 0
    if len(sticker)<=3:
        return max(sticker)

    # start 0
    a3 = sticker[0]
    a2 = sticker[1]
    a1 = sticker[0]+sticker[2]
    for s in sticker[3:-1]:
        a1,a2,a3 = s+max(a2,a3), a1, a2
    
    # start 1
    b3 = sticker[1]
    b2 = sticker[2]
    b1 = sticker[1]+sticker[3]
    for s in sticker[4:]:
        b1,b2,b3 = s+max(b2,b3),b1,b2
    return max(a1,a2,a3,b1,b2,b3)


test_case = [[[14, 6, 5, 11, 3, 9, 2, 10],36],[[1, 3, 2, 5, 4],8]]

for a,b in test_case:
    print(solution(a),b)