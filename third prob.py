def is_stepping_number(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if abs(int(num_str[i]) - int(num_str[i - 1])) != 1:
            return False
    return True

n, m = map(int, input().split())
for i in range(n, m + 1):
    if is_stepping_number(i):
        print(i,end=' ')
