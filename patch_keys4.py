import re

with open("fight day.html", "r") as f:
    content = f.read()

# Let's check where actions.dodgeLeft and dodgeRight are set
match = re.search(r"if \(k === 'q'.*?\n.*?\n", content, re.DOTALL)
if match:
    print(match.group(0))
