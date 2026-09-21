def Check_Palindrome(n: int, s: str) -> bool:
    left = 0
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            # Delete left character
            left_check = s[left + 1:right + 1]

            # Delete right character
            right_check = s[left:right]

            if left_check == left_check[::-1] or right_check == right_check[::-1]:
                return True
            else:
                return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))