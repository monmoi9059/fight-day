with open('fight day.html', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'let lx, ly, rx, ry;' in line:
            for j in range(max(0, i-2), i+15):
                print(lines[j].strip())
            break
