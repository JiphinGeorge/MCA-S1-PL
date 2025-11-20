# Retrieve lines where a word starts with 's' and ends with 'e'

fname = input("Enter filename: ")

with open(fname) as f:
    for line in f:
        words = line.strip().split()
        for w in words:
            if w.startswith('s') and w.endswith('e'):
                print("Matched line:", line.strip())
                break
