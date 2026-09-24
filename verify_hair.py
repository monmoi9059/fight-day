with open('fight day.html', 'r') as f:
    content = f.read()
    if 'hair:' in content and 'hairColor:' in content:
        print("hair generation added.")
    if 'b.hair ===' in content:
        print("hair drawing added.")

    print("Generation excerpt:")
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'let build = {' in line:
            for j in range(i, i+8):
                print(lines[j])
            break

    print("\nDrawing excerpt:")
    for i, line in enumerate(lines):
        if 'ctx.bezierCurveTo(-hw + 5, 25, -hw - 5, -10, -hw, -hh); ctx.fill();' in line:
            for j in range(i, i+15):
                print(lines[j])
            break
