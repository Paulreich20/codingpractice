def Power(original):
    if len(original) == 0:
        powerSet = []
        powerSet.append(original)
        return powerSet
    else:
        item = original.pop()
        powerSet = Power(original)
        bigboi = powerSet.copy()
        for set in bigboi:
            copy = set.copy()
            copy.add(item)
            powerSet.append(copy)
        return powerSet
print(len(Power({1,2,3,9,'p','t',4})))
