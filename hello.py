
s = "Hello 10:49"

print(s)
output_file = "output.txt"
with open(output_file, "w") as f:
    f.write(s)
