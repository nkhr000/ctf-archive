# N枚のカードを配りAice, Bobが交互に１枚とる。最適な戦略の場合、AliceはBobより合計難点高いか

N = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)

result = 0
for i in range(N):
    if i % 2 == 0:
        result += cards[i]
    else:
        result -= cards[i]

print(result)