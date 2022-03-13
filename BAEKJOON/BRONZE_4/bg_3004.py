N = int(input())

# 가로 세로를 번갈아가면서 자를 때, 최대 조각이 나옵니다.
if(N % 2 == 0):  # 짝수이면 자르는 횟수가 정확히 반으로 나누어집니다.
    S, M = (N // 2, N // 2)
else:  # 홀수이면 자르는 횟수가 1만큼 남기 때문에, 가로나 세로 중에 하나 1을 더해줍니다.
    S, M = (N // 2, N // 2 + 1)

# 가로, 세로 각각 자른 수의 +1만큼 칸이 생깁니다.
print((S+1) * (M+1))