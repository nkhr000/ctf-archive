# 1以上整数N以下の各桁の総和がA以上、B以下の総和

def calc_sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10

    return sum_digit

N, A, B = map(int, input().split())
result = 0
for n in range(1, N + 1):
    if A <= calc_sum_digit(n) <= B:
        result += n

print(result)
