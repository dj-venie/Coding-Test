# -*- coding: utf-8 -*-

"""문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 \(M\)으로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\), \(K\)와 \(M\)이 주어진다. (1 ≤ \(N\) ≤ 1018, 0 ≤ \(K\) ≤ \(N\), 2 ≤ \(M\) ≤ 2,000, M은 소수)

출력
 
\(\binom{N}{K}\)를 \(M\)으로 나눈 나머지를 출력한다."""

n,k,m = map(int, input().split())

k = min(k, n-k)

up = 1
down = 1
for i in range(k):
    up *= (n-i)
    down *= (i+1)

print(up, down, up/down)
print((up/down)%m)