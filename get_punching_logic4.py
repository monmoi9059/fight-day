import re

with open("fight day.html", "r") as f:
    content = f.read()

# Let's check handlePunchInput block
match = re.search(r'function handlePunchInput\(\) \{.*?\n    \}', content, re.DOTALL)
if match:
    print(match.group(0))
