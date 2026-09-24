import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Add leanX and leanY to player
content = content.replace("worldX: 0, worldZ: 0, dodgeState: 'none', dodgeTimer: 0, dodgeOffset: 0, tilt: 0, counterWindow: 0,",
                          "worldX: 0, worldZ: 0, dodgeState: 'none', dodgeTimer: 0, dodgeOffset: 0, tilt: 0, counterWindow: 0, leanX: 0, leanY: 0,")

# Add shift to keys
content = content.replace("const keys = { w: false, a: false, s: false, d: false, q: false, e: false };",
                          "const keys = { w: false, a: false, s: false, d: false, q: false, e: false, shift: false };")

# Add shift event listener
key_down_regex = r'(if \(k === \'w\'\) keys\.w = true; if \(k === \'s\'\) keys\.s = true; if \(k === \'a\'\) keys\.a = true; if \(k === \'d\'\) keys\.d = true;)'
key_down_replace = r"""if (k === 'shift') keys.shift = true;
        \1"""
content = re.sub(key_down_regex, key_down_replace, content)

key_up_regex = r'(if \(k === \'w\'\) keys\.w = false; if \(k === \'s\'\) keys\.s = false; if \(k === \'a\'\) keys\.a = false; if \(k === \'d\'\) keys\.d = false;)'
key_up_replace = r"""if (k === 'shift') keys.shift = false;
        \1"""
content = re.sub(key_up_regex, key_up_replace, content)


# Update UI
ui_regex = r'(<p><strong>WASD:</strong> Move &nbsp;\|&nbsp; <strong>Q / E:</strong> Dodge Left / Right</p>)'
ui_replace = r"""\1
            <p><strong>Shift + WASD:</strong> Body Lean (Slip Punches)</p>"""
content = re.sub(ui_regex, ui_replace, content)

# Update Movement Logic in update loop
movement_regex = r'(// Player Movement\s*let moveSpeed = 160 \* \(dt/1000\);\s*if \(keys\.w\) player\.worldZ \+= moveSpeed;\s*if \(keys\.s\) player\.worldZ -= moveSpeed;\s*if \(keys\.a\) player\.worldX -= moveSpeed;\s*if \(keys\.d\) player\.worldX \+= moveSpeed;)'

movement_replace = r"""// Player Movement and Body Leaning
        let moveSpeed = 160 * (dt/1000);
        let targetLeanX = 0;
        let targetLeanY = 0;

        if (keys.shift) {
            if (keys.w) targetLeanY = -120; // Lean forward
            if (keys.s) targetLeanY = 120;  // Lean back
            if (keys.a) targetLeanX = -150; // Lean left
            if (keys.d) targetLeanX = 150;  // Lean right
        } else {
            if (keys.w) player.worldZ += moveSpeed;
            if (keys.s) player.worldZ -= moveSpeed;
            if (keys.a) player.worldX -= moveSpeed;
            if (keys.d) player.worldX += moveSpeed;
        }

        player.leanX += (targetLeanX - player.leanX) * 0.15;
        player.leanY += (targetLeanY - player.leanY) * 0.15;
"""

content = re.sub(movement_regex, movement_replace, content)

# Update screen calculation to use leanX and leanY
screenX_regex = r'(view\.screenX = 512 \+ \(\(opponent\.worldX - player\.worldX\) \* 2\.5 \* view\.scale\) - \(\(mouse\.x - 512\)\*0\.1\) \+ player\.dodgeOffset;)'
screenX_replace = r"""\1
        view.screenX -= player.leanX;
"""
content = re.sub(screenX_regex, screenX_replace, content)

screenY_regex = r'(view\.screenY = 384 \+ \(\(view\.dist - 130\) \* 0\.9\) - \(\(mouse\.y - 384\)\*0\.1\);)'
screenY_replace = r"""\1
        view.screenY += player.leanY;
"""
content = re.sub(screenY_regex, screenY_replace, content)


# Update slip logic to include lean in range
punch_hit_regex = r'(if \(player\.dodgeState !== \'none\'\) \{\s*spawnText\("SLIP!", 512 \+ \(player\.dodgeState === \'left\' \? -100 : 100\), 250, "#00a8ff"\);\s*player\.counterWindow = 600;\s*\})'
punch_hit_replace = r"""if (player.dodgeState !== 'none' || Math.abs(player.leanX) > 100 || player.leanY > 80) {
                        spawnText("SLIP!", 512 + (player.leanX < 0 || player.dodgeState === 'left' ? -100 : 100), 250, "#00a8ff");
                        player.counterWindow = 600;
                    }"""
content = re.sub(punch_hit_regex, punch_hit_replace, content)


with open('fight day.html', 'w') as f:
    f.write(content)
