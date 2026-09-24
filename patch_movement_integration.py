import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Update optimalDist and oSpeed
movement_vars_regex = r'(let oppMaxReach = 70 \+ \(opponent\.stats\.reach \* 5\.0\) \* opponent\.build\.scaleX;\s*let optimalDist = oppMaxReach - 15;\s*let oSpeed = \(90 - \(opponent\.build\.scaleX - 1\)\*40\) \* \(dt/1000\);)'
movement_vars_replace = r"""\1
        if (opponent.fightingStyle === 'outboxer') { optimalDist += 20; oSpeed *= 1.1; }
        else if (opponent.fightingStyle === 'brawler') { optimalDist -= 10; oSpeed *= 0.85; }
        else if (opponent.fightingStyle === 'swarmer') { optimalDist -= 20; oSpeed *= 1.25; }"""
content = re.sub(movement_vars_regex, movement_vars_replace, content)

# Update Aggro check
aggro_check_regex = r'(if \(Math\.random\(\) < opponent\.stats\.aggro && opponent\.sta > 20 && view\.dist <= oppMaxReach \+ 10\) \{)'
aggro_check_replace = r"""let aggroMod = opponent.fightingStyle === 'swarmer' ? 0.2 : (opponent.fightingStyle === 'outboxer' ? -0.1 : 0);
                if (Math.random() < opponent.stats.aggro + aggroMod && opponent.sta > 20 && view.dist <= oppMaxReach + 10) {"""
content = re.sub(aggro_check_regex, aggro_check_replace, content)


with open('fight day.html', 'w') as f:
    f.write(content)
