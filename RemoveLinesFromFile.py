# Remove lines from a file with words starting with 'a' and ending with 'e'
lines = []
with open("sample.txt") as f:
    for line in f:
        w = line.strip()
        if not (w.startswith("a") and w.endswith("e")):
            lines.append(w)

with open("sample.txt", "w") as f:
    for l in lines:
        f.write(l + "\n")

# OUTPUT:
# (File updated – no words starting with 'a' and ending with 'e')