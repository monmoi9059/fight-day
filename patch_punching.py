import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Update windup timer
timer_regex = r'(opponent\.stateTimer = Math\.max\(200, 650 - \(opponent\.stats\.speed \* 15\)\) \+ \(opponent\.build\.scaleX\*50\);)'
timer_replace = r"""\1
                    if (opponent.fightingStyle === 'brawler') opponent.stateTimer *= 1.3;
                    else if (opponent.fightingStyle === 'swarmer') opponent.stateTimer *= 0.8;"""
content = re.sub(timer_regex, timer_replace, content)


# Update arm rendering logic
arm_regex = r'(if \(opponent\.currentAttack === \'left\'\) \{\s*lx = ox - 60 \+ \(ease\*70\); ly = oy \+ 40 \+ \(ease\*180\); rx = ox \+ 45\*b\.scaleX; ry = oy \+ 60;\s*\} else \{\s*lx = ox - 45\*b\.scaleX; ly = oy \+ 60; rx = ox \+ 60 - \(ease\*70\); ry = oy \+ 40 \+ \(ease\*180\);\s*\})'
arm_replace = r"""let hookWide = 60; let hookTravel = 70; let hookDrop = 180;
                if (opponent.fightingStyle === 'brawler') { hookWide = 90; hookTravel = 100; hookDrop = 200; }
                else if (opponent.fightingStyle === 'outboxer') { hookWide = 40; hookTravel = 45; hookDrop = 140; }

                if (opponent.currentAttack === 'left') {
                    lx = ox - hookWide + (ease*hookTravel); ly = oy + 40 + (ease*hookDrop); rx = ox + 45*b.scaleX; ry = oy + 60;
                } else {
                    lx = ox - 45*b.scaleX; ly = oy + 60; rx = ox + hookWide - (ease*hookTravel); ry = oy + 40 + (ease*hookDrop);
                }"""
content = re.sub(arm_regex, arm_replace, content)

with open('fight day.html', 'w') as f:
    f.write(content)
