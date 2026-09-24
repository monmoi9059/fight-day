with open('fight day.html', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'function update(' in line:
            print("Found update logic around line", i)
            start = max(0, i - 10)
            end = min(len(lines), i + 200)
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip()}")
            break
