import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Default fighting style in opponent
content = content.replace("desc: \"\",", "desc: \"\", fightingStyle: 'outboxer',")

# generateOpponent style generation logic
gen_regex = r'(if \(buildClass < 0\.3\) \{[\s\S]*?\} else \{[\s\S]*?styleDesc = "Athletic Contender - Shredded, balanced fighter\.";\s*\})'
gen_replace = r"""let fightingStyle = 'outboxer';
        if (buildClass < 0.3) {
            build.scaleX = 1.15 + Math.random()*0.2; build.scaleY = 1.0 + Math.random()*0.15;
            build.belly = 0.4 + Math.random()*0.5; build.muscle = 0.7 + Math.random()*0.3; build.jaw = 1.2 + Math.random()*0.2;
            fightingStyle = 'brawler';
            styleDesc = "Brawler - Wide, tough, heavy hitter.";
            base += 2;
        } else if (buildClass < 0.6) {
            build.scaleX = 0.8 + Math.random()*0.15; build.scaleY = 0.85 + Math.random()*0.15;
            build.belly = 0; build.muscle = 0.8 + Math.random()*0.4; build.jaw = 0.8 + Math.random()*0.2;
            fightingStyle = Math.random() > 0.5 ? 'swarmer' : 'outboxer';
            styleDesc = fightingStyle === 'swarmer' ? "Swarmer - Fast, aggressive, constant pressure." : "Outboxer - Fast, evasive, fights outside.";
        } else {
            build.scaleX = 0.95 + Math.random()*0.15; build.scaleY = 1.0 + Math.random()*0.1;
            build.belly = 0.0; build.muscle = 1.3 + Math.random()*0.5; build.jaw = 1.0 + Math.random()*0.1;
            fightingStyle = Math.random() > 0.5 ? 'swarmer' : 'outboxer';
            styleDesc = fightingStyle === 'swarmer' ? "Athletic Swarmer - Shredded, relentless." : "Athletic Outboxer - Balanced, tactical.";
        }"""
content = re.sub(gen_regex, gen_replace, content)

# Inject fightingStyle into the opponent object initialization inside generateOpponent
content = content.replace("rank: targetRank, color: `hsl(${Math.random()*360}, 80%, 30%)`, desc: styleDesc,",
                          "rank: targetRank, color: `hsl(${Math.random()*360}, 80%, 30%)`, desc: styleDesc, fightingStyle: fightingStyle,")

with open('fight day.html', 'w') as f:
    f.write(content)
