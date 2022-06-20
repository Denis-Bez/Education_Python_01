# Task_1
# Let's define a rotate array as a sorted array where the numbers have all been rotated to the right some number of places,
# with nimbers wrapping around when they reach the end of the list.
# [1, 2, 3, 4, 5] rotated 3 times is [3, 4, 5, 1, 2]
# Given a rotated array, find the number of times it was rotated

# [3, 4, 5, 1, 2] -> 3
# [2, 3, 4, 5, 1] -> 4
# [6, 8, 12, 1, 3] -> 3
# [1, 2, 3, 4, 5] -> 0

# Bianry serch method
def get_rotate_number(ls):
    left_ls = 0
    right_ls = len(ls) - 1
    
    while left_ls < right_ls:
        current = ((right_ls + left_ls) // 2)
        
        if ls[current] > ls[left_ls]:
            left_ls = current
        elif ls[current] < ls[left_ls]:
           right_ls = current
        else:
            return right_ls


# Task_2
# Given a string s, find the length of the longest substring without repeating characters
# 
# In the string "abcabcbb", the longest substring without repeating characters is "abc", so the leight is 3


def leight_string(s: str) -> int:
    chars = [0] * 128
    length = 0
    left = 0

    for right in range(len(s)):
        chars[ord(s[right])] += 1
        
        while chars[ord(s[right])] > 1:
            chars[ord(s[left])] -= 1
            left += 1
    
        length = max(length, right - left + 1)
    
    return length





if __name__ == "__main__":
    print(leight_string('hello'))
