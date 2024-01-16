#!/usr/bin/python3
'''the function returns fewest number
of steps'''


def minOperations(n):
    '''This function returns the fewest number
    of steps to achieve characters equal to n'''
    character_list = ['H']
    count = 0
    character_list = [float('inf')] * (n + 1)
    character_list[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                character_list[i] = min(character_list[i], character_list[j] + i // j)
    if character_list[n] != float('inf'):
        return character_list[n]
    else:
        return 0
