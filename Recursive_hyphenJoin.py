# Write a recursive function to join items in a list using ','

def join_list(lst, i=0):
    if i == len(lst)-1:
        return lst[i]
    return lst[i] + "-" + join_list(lst, i+1)

print(join_list(["a", "b", "c", "d"]))

# OUTPUT:
# a,b,c,d