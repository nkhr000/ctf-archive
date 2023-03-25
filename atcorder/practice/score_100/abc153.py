# モンスターの体力H, 攻撃力A,が与えられた時、何回攻撃すればモンスターを倒せるか

h, a = map(int, input().split())

sho = h // a
print(sho if h % a == 0 else sho + 1) 
