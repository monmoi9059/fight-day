import re

with open('fight day.html', 'r') as f:
    content = f.read()

replacement = """        let build = {
            scaleX: 1, scaleY: 1, muscle: 1, belly: 0, jaw: 1,
            hair: ['bald', 'buzzcut', 'mohawk', 'afro', 'fade'][Math.floor(Math.random() * 5)],
            hairColor: ['#111', '#4a2511', '#e8b831', '#8b2e16'][Math.floor(Math.random() * 4)]
        };"""

content = content.replace("let build = { scaleX: 1, scaleY: 1, muscle: 1, belly: 0, jaw: 1 };", replacement)

# We also need to add hair to the default opponent object initialization at line 184
replacement2 = """        build: { scaleX: 1, scaleY: 1, muscle: 1, belly: 0, jaw: 1, hair: 'buzzcut', hairColor: '#111' },"""
content = content.replace("build: { scaleX: 1, scaleY: 1, muscle: 1, belly: 0, jaw: 1 },", replacement2)

with open('fight day.html', 'w') as f:
    f.write(content)
