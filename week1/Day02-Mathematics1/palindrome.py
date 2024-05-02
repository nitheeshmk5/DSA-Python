def palindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        last_digit = temp % 10
        reverse = reverse * 10 + last_digit 
        temp = temp // 10     
    if n == reverse:
        print(f"{n} is palindrome number")
    else:
        print(f"{n} is !palindrome number")

palindrome(7557)
