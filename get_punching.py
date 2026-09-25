import re

with open("fight day.html", "r") as f:
    content = f.read()

match = re.search(r"function handlePunchInput\(\) \{.*?\n\s*\}\n\s*\}", content, re.DOTALL)
if match:
    print(match.group(0))
