with open('fight day.html', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'menu-main' in line:
            print("Found menu-main around line", i)
            start = max(0, i - 1)
            end = min(len(lines), i + 10)
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip()}")
            break
