from math import ceil


def sol(n):
    
    lines = [0, 0, 0]
    curr = 0
    while curr < n:
        print(curr, lines)
        if lines[0] == min(lines):
            if lines[0] == lines[1] and lines[0] == lines[2]:
                curr += lines[2] + lines[1]
                curr += (lines[0] // 2 )
            elif lines[0] + 1 == lines[1] and lines[0] + 1 == lines[2]:
                curr += lines[2] + lines[1]
                curr += ceil(lines[1] / 2)
            else:
                curr += lines[2] + lines[1]
                curr += (max(lines) // 2)
            lines[0] += 1
        elif lines[1] == min(lines):
            if lines[0] == lines[1] and lines[0] == lines[2]:
                curr += lines[0] + lines[2]
                curr += (lines[0] // 2)
            elif lines[1] + 1 == lines[0] and lines[1] + 1 == lines[2]:
                curr += lines[0] + lines[2]
                curr += ceil(lines[0] / 2) 
            else:
                curr += lines[0] + lines[2]
                curr += (max(lines) // 2)
            lines[1] += 1
        elif lines[2] == min(lines):
            if lines[0] == lines[1] and lines[0] == lines[2]:
                curr += lines[0] + lines[1]
                curr += (lines[0] // 2)
            elif lines[2] + 1 == lines[0] and lines[2] + 1 == lines[1]:
                curr += lines[0] + lines[1]
                curr += ceil(lines[0] / 2) 
            else:
                curr += lines[0] + lines[1]
                curr += (max(lines) // 2)
            lines[2] += 1
    return sum(lines)
            
    
    return 
    
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))
    