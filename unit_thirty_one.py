count = 0
def find_heaviest_coin(coins):
    global count 
    count += 1
    if len(coins) == 1:
        return coins[0]
    else:
        mid = len(coins)//2
        left = coins[:mid]
        right = coins[mid:]
        left_weight = sum([coin.get('weight') for coin in left])
        right_weight = sum([coin.get('weight') for coin in right])
        
        if left_weight > right_weight:
            return find_heaviest_coin(left)
        elif left_weight < right_weight:
            return find_heaviest_coin(right)
        else:
            return find_heaviest_coin(coins[len(coins)//2:])
coins = [
    
        {'coins' : 1 , 'weight': 1},
        {'coins' : 2 , 'weight': 2},
        {'coins' : 3 , 'weight': 3},
        {'coins' : 4 , 'weight': 4},
        {'coins' : 5 , 'weight': 5},
        {'coins' : 6 , 'weight': 6},
        {'coins' : 7 , 'weight': 7},
        {'coins' : 8 , 'weight': 8},
        #{'coins' : 9 , 'weight': 9}
    
]
       
        

coin = find_heaviest_coin(coins)
print(coin, " ", count)
        