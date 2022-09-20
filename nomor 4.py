def isPalindrome(s):
    return s== s[::-1]

s = "malam"
ans = isPalindrome(s)

if ans:
    print("True")
else:
    print("False")