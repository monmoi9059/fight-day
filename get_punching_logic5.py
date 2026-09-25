import re

with open("fight day.html", "r") as f:
    content = f.read()

# I want to check how the mouse targeting works and remove it.
# Instead of targeting crossX based on mouse, we should target fixed positions on the opponent (like their head or body)
# depending on the punch type, or just target the center screen + lean logic.
# Wait, let's look at `view.crossX` update
match = re.search(r'view\.crossX.*?sway;.*?\n.*?\n', content, re.DOTALL)
if match:
    print(match.group(0))
