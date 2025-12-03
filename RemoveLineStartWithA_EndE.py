# Remove lines with words starting with 'a' and ending with 'e'

fname = input("Enter filename: ")
new_lines = []

with open(fname) as f:
    for line in f:
        words = line.split()
        if not any(w.startswith('a') and w.endswith('e') for w in words):
            new_lines.append(line)

with open(fname, "w") as f:
    f.writelines(new_lines)

print("Filtered successfully.")
