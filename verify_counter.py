with open('fight day.html', 'r') as f:
    content = f.read()

print("resolvePlayerHit excerpt:")
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'let dmg = (player.stats.power * 1.3) + (Math.random() * 5);' in line:
        for j in range(i, i+12):
            print(lines[j])
        break

print("\nMiss logic excerpt:")
for i, line in enumerate(lines):
    if 'spawnText("WHIFF!", 512, 200, "#95a5a6");' in line:
        for j in range(i-2, i+6):
            print(lines[j])
        break

print("\nSlip logic excerpt:")
for i, line in enumerate(lines):
    if 'spawnText("SLIP!", 512 + (player.dodgeState === \'left\' ? -100 : 100), 250, "#00a8ff");' in line:
        for j in range(i-2, i+4):
            print(lines[j])
        break
