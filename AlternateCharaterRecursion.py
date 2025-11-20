# Display alternate characters using recursion

def alt_chars(s, i=0):
    if i >= len(s):
        return ""
    return s[i] + alt_chars(s, i+2)

text = input("Enter a string: ")
print("Alternate characters:", alt_chars(text))
