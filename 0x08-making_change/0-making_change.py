#!/usr/bin/python3
'''0-making_change'''


def makeChange(coins, total):
    '''This function determines the fewest
    number of coins needed to meet a
    given amount total. Given a pile
    of coins of different values'''
    if total <= 0:
        return 0
    '''Use a greedy algo. Start by sorting the coins'''
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        make_change_times = total // coin
        change += make_change_times
        total -= (make_change_times * coin)
    if total != 0:
        return -1
    return change
