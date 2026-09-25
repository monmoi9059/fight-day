import re

with open("fight day.html", "r") as f:
    content = f.read()

match = re.search(r"const keys = \{.*?\};", content)
if match:
    print(match.group(0))
