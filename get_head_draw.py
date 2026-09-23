with open('fight day.html', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'let headGrd =' in line:
            print("Found head drawing logic around line", i)
            start = max(0, i - 10)
            end = min(len(lines), i + 40)
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip()}")
            break
