def solution(numbers, hand):
    answer = ''
    keypad = {
        1:[0,0], 2:[1,0], 3:[2,0],
        4:[0,1], 5:[1,1], 6:[2,1],
        7:[0,2], 8:[1,2], 9:[2,2],
        '#':[0,3], 0:[1,3], '*':[2,3],
    }
    left_hand = keypad.get('#')
    right_hand = keypad.get('*')

    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            left_hand = keypad.get(n)
        elif n in [3,6,9]:
            answer += 'R'
            right_hand = keypad.get(n)
        else:
            x, y = keypad.get(n)
            # left_distance = x-left_hand[0] if x-left_hand[0]>=0 else left_hand[0]-x
            # left_distance += y-left_hand[1] if y-left_hand[1]>=0 else left_hand[1]-y
            # right_distance = x-right_hand[0] if x-right_hand[0]>=0 else right_hand[0]-x
            # right_distance += y-right_hand[1] if y-right_hand[1]>=0 else right_hand[1]-y
            left_distance = abs(x-left_hand[0]) + abs(y-left_hand[1])
            right_distance = abs(x-right_hand[0]) + abs(y-right_hand[1])
            if right_distance > left_distance:
                answer += 'L'
                left_hand = keypad.get(n)
            elif right_distance < left_distance:
                answer += 'R'
                right_hand = keypad.get(n)
            else:
                if hand == "left":
                    answer += 'L'
                    left_hand = keypad.get(n)
                else:
                    answer += 'R'
                    right_hand = keypad.get(n)
    return answer