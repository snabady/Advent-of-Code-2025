import sys
puzzle = sys.stdin.read()
res1=0
res2=0
for line in puzzle.splitlines():
    vals = list(line)
    index_max = max(range(len(line)-1), key=line.__getitem__) 
    rest_line=line[index_max+1:]
    index_two = max(range(len(rest_line)),key=rest_line.__getitem__)
    jolt=f"{line[index_max]}{rest_line[index_two]}"
    res1+=int(jolt)
print(f"puzzle1: {res1}")
    
