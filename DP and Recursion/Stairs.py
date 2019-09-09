list = [1,2,4]


def Stairs(n):
    if n > len(list):
        list.append(Stairs(n-1)+Stairs(n-2)+Stairs(n-3))
    return list[n-1]

print(Stairs(223))
