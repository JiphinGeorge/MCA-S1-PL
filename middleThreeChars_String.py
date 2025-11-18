#3. Given a string of odd length > 7, return a string of the middle 3 characters.
def middle_three(s):
    if len(s) <= 7 or len(s) % 2 == 0:
        raise ValueError("String must be odd length and greater than 7")
    
    mid = len(s) // 2
    return s[mid-1 : mid+2]

# Accept string from user
user_input = input("Enter an odd-length string (>7 characters): ")

try:
    print("Middle three characters:", middle_three(user_input))
except ValueError as e:
    print("Error:", e)
