with open('fight day.html', 'r') as f:
    content = f.read()

print("UI excerpt:")
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'WASD:' in line:
        for j in range(i, i+5):
            print(lines[j])
        break

print("\nMovement logic excerpt:")
for i, line in enumerate(lines):
    if 'let moveSpeed =' in line:
        for j in range(i-2, i+18):
            print(lines[j])
        break

print("\nSlip logic excerpt:")
for i, line in enumerate(lines):
    if 'spawnText("SLIP!"' in line:
        for j in range(i-2, i+6):
            print(lines[j])
        break
