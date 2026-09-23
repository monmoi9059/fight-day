import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Add counterWindow to player
content = content.replace("worldX: 0, worldZ: 0, dodgeState: 'none', dodgeTimer: 0, dodgeOffset: 0, tilt: 0,",
                          "worldX: 0, worldZ: 0, dodgeState: 'none', dodgeTimer: 0, dodgeOffset: 0, tilt: 0, counterWindow: 0,")

# Update opponent punch logic for misses -> counter punch window
miss_logic_regex = r'(} else \{\s*spawnText\("WHIFF!", 512, 200, "#95a5a6"\);\s*\})'
miss_logic_replace = r"""} else {
                        spawnText("WHIFF!", 512, 200, "#95a5a6");
                        if (player.dodgeState !== 'none' || Math.abs(player.leanX) > 100 || player.leanY > 80) {
                            player.counterWindow = 600;
                        }
                    }"""
content = re.sub(miss_logic_regex, miss_logic_replace, content)

# But wait, what if player dodge successfully in range?
slip_logic_regex = r'(spawnText\("SLIP!", 512 \+ \(player\.dodgeState === \'left\' \? -100 : 100\), 250, "#00a8ff"\);)'
slip_logic_replace = r"""\1
                            player.counterWindow = 600;"""
content = re.sub(slip_logic_regex, slip_logic_replace, content)


# Update resolvePlayerHit for damage and visual effects
hit_logic_regex = r'(let dmg = \(player\.stats\.power \* 1\.3\) \+ \(Math\.random\(\) \* 5\);)'
hit_logic_replace = r"""\1
                let isCounter = player.counterWindow > 0 && opponent.state !== 'blocking';
                if (isCounter) {
                    dmg *= 2.5;
                    spawnText("COUNTER PUNCH!", targetX, targetY - 40, "#fbc531");
                }
"""
content = re.sub(hit_logic_regex, hit_logic_replace, content)

head_hit_regex = r'(dmg \*= 1\.5; spawnParticles\(targetX, targetY, \'blood\'\); hitStopFrames = 4; setCamShake\(15, 0\.05\);)'
head_hit_replace = r"""\1
                        if (isCounter) { spawnParticles(targetX, targetY, 'blood'); spawnParticles(targetX, targetY, 'blood'); hitStopFrames = 8; setCamShake(30, 0.1); }
"""
content = re.sub(head_hit_regex, head_hit_replace, content)

body_hit_regex = r'(spawnParticles\(targetX, targetY, \'sweat\'\); hitStopFrames = 2; setCamShake\(8, 0\.02\);)'
body_hit_replace = r"""\1
                        if (isCounter) { hitStopFrames = 5; setCamShake(20, 0.05); }
"""
content = re.sub(body_hit_regex, body_hit_replace, content)


# Decrease counterWindow in update loop
update_tick_regex = r'(if \(hitStopFrames > 0\) \{ hitStopFrames--; return; \})'
update_tick_replace = r"""\1
    if (player.counterWindow > 0) { player.counterWindow -= dt; }
"""
content = re.sub(update_tick_regex, update_tick_replace, content)

with open('fight day.html', 'w') as f:
    f.write(content)
