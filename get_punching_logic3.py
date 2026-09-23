with open('fight day.html', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'canvas.addEventListener(\'mousedown\'' in line:
            print("Found mousedown logic around line", i)
            start = max(0, i - 10)
            end = min(len(lines), i + 50)
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip()}")
            break
