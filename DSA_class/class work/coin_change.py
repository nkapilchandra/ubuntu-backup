def C(coins_list,value):
    min_coins = value
    if value in coins_list:
        return 1
    else:
        for i in [c for c in coins_list if c<= value]:
            num_coins = 1 + C(coins_list,value-i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def C_eff(coins_list,value,known_result):
    min_coins = value
    if value in coins_list:
        known_result[value] = 1
        return 1
    elif known_result[value]>0:
        return known_result[value]
    else:
        for i in [c for c in coins_list if c <=value]:
            num_coins = 1 + C_eff(coins_list,value-i,known_result)
            if min_coins >= num_coins:
                min_coins = num_coins
                known_result[value] = min_coins
    return min_coins

print(C_eff([1,5,10,25],63,[0]*64))
print(C([1,5,10,25],63))
