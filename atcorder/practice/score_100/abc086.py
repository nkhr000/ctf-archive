# 整数a,bの積が偶数か奇数かを答える

a, b = map(int, input().split())
if (a*b) % 2 == 0: 
    print("Even")
else:
    print("Odd")

# 三項演算子による記載
print("Even" if a * b % 2 == 0 else "Odd")