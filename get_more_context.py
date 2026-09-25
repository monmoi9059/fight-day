import re

with open("fight day.html", "r") as f:
    content = f.read()

print("dodge logic in update():")
match = re.search(r"// Player Dodge state.*?\n.*?actions\.dodgeRight = false;", content, re.DOTALL)
if match:
    print(match.group(0))
