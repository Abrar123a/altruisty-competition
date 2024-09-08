def mini(price, k):
    stack=[]
    turns=k
    for digit in price:
        while stack and turns > 0 and stack[-1] > digit:
            stack.pop()
            turns-=1
        stack.append(digit)
    while turns > 0:
        stack.pop()
        turns-=1
    result=''.join(stack).lstrip('0')

    if not result:
        result='0'
    return int(result)

price=input()
k=int(input())
print(mini(price, k))
