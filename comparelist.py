#8. Compare two lists entered by user.
list1 = input("Enter first list (comma separated): ").split(',')
list2 = input("Enter second list (comma separated): ").split(',')

print("Lists are equal" if list1 == list2 else "Lists are NOT equal")
