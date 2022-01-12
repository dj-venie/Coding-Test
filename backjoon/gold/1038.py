"""
문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.
"""

n = int(input())
def find(n):
    if n<10:
        return n
    n -= 9
    cache = {i:[str(i)] for i in range(10)}
    while cache[9]:
        new_cache = {i:[] for i in range(10)}
        for i in range(10):
            for j in range(i):
                for c in cache[j]:
                    now_str = str(i)+c
                    new_cache[i].append(now_str)
                    n -= 1
                    if n==0:
                        return now_str
        cache = new_cache
        # print(cache)
    return -1
print(find(n))


