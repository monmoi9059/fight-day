import re

with open("fight day.html", "r") as f:
    content = f.read()

# Let's check where Q and E are used currently
match = re.search(r"if \(k === 'q'.*?\n.*?\n", content, re.DOTALL)
if match:
    print("Q/E usage:")
    print(match.group(0))
