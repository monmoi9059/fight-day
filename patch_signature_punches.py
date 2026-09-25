import re

with open("fight day.html", "r") as f:
    content = f.read()

# Add a few popular boxer signature punches.
# We can change some of the modShift punches or add modQ && modE punches, or replace some of the generic ones with specific signature ones.

# Let's say:
# Shift + Left = "Smash" (Donovan Ruddock's signature)
# Shift + Right = "Gazelle Punch" (Floyd Patterson/Rocky Marciano)
# Shift + Down = "Bolo Punch" (Kid Gavilan / Sugar Ray Leonard) (Already there)
# Q + Right = "Philly Shell Counter / Pull Counter" (Floyd Mayweather) -> 'pull_counter'
# E + Left = "Liver Shot" (Micky Ward / Bas Rutten) -> 'liver_shot'

handle_pattern = r"function handlePunchInput\(\) \{.*?\n\s*\}"
new_handle = """function handlePunchInput() {
        if (keys.arrowleft && keys.arrowright) { player.isBlocking = true; }
        else {
            player.isBlocking = false;
            if (player.exhausted || player.dodgeState !== 'none') return;

            let modShift = keys.shift;
            let modQ = keys.q;
            let modE = keys.e;

            if (keys.arrowup && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'gazelle_punch'); // Signature
                else if (modQ) launchPunch('right', 'flicker_jab'); // Thomas Hearns
                else if (modE) launchPunch('right', 'overhand');
                else launchPunch('right', 'overhead');
            }
            else if (keys.arrowdown && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'bolo'); // Sugar Ray Leonard / Kid Gavilan
                else if (modQ) launchPunch('left', 'lead_uppercut');
                else if (modE) launchPunch('right', 'shovel_hook');
                else launchPunch('right', 'uppercut');
            }
            else if (keys.arrowleft && player.arms.left.state === 'idle') {
                if (modShift) launchPunch('left', 'smash'); // Donovan Ruddock
                else if (modQ) launchPunch('left', 'jab');
                else if (modE) launchPunch('left', 'liver_shot'); // Micky Ward
                else launchPunch('left', 'straight');
            }
            else if (keys.arrowright && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'haymaker');
                else if (modQ) launchPunch('right', 'pull_counter'); // Floyd Mayweather
                else if (modE) launchPunch('right', 'body_hook');
                else launchPunch('right', 'cross');
            }
        }
    }"""

content = re.sub(handle_pattern, new_handle, content, count=1, flags=re.DOTALL)


# Now update launchPunch to know if it's head or body
launch_pattern = r"let bodyPunches = \['body_hook', 'shovel_hook', 'uppercut', 'bolo'\];"
new_launch = "let bodyPunches = ['body_hook', 'shovel_hook', 'uppercut', 'bolo', 'liver_shot'];"
content = re.sub(launch_pattern, new_launch, content)

# Now add animations for signature punches
anim_pattern = r"(// Apply different animations based on punch type\n.*?let radius = 120 - \(ease \* 65\);)"

new_anim = """// Apply different animations based on punch type
            if (arm.punchType === 'overhead' || arm.punchType === 'heavy_overhead' || arm.punchType === 'overhand') {
                cy -= Math.sin(arm.progress * Math.PI) * (arm.punchType === 'heavy_overhead' ? 220 : 180);
                if (arm.punchType === 'heavy_overhead' || arm.punchType === 'overhand') cx += (side === 'left' ? 1 : -1) * Math.sin(arm.progress * Math.PI) * 50;
            } else if (arm.punchType === 'uppercut' || arm.punchType === 'bolo' || arm.punchType === 'lead_uppercut') {
                cy += Math.sin(arm.progress * Math.PI) * (arm.punchType === 'bolo' ? 200 : 150);
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * (arm.punchType === 'bolo' ? 120 : 80);
            } else if (arm.punchType === 'haymaker') {
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * 200; // Super wide hook/haymaker
                cy -= Math.sin(arm.progress * Math.PI) * 30;
            } else if (arm.punchType === 'body_hook' || arm.punchType === 'shovel_hook' || arm.punchType === 'liver_shot') {
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * (arm.punchType === 'liver_shot' ? 160 : 120);
                cy += Math.sin(arm.progress * Math.PI) * (arm.punchType === 'liver_shot' ? 140 : 100);
            } else if (arm.punchType === 'jab' || arm.punchType === 'cross' || arm.punchType === 'straight') {
                // straight line with slight torque
                cx += (side === 'left' ? 1 : -1) * Math.sin(arm.progress * Math.PI) * 20;
                cy -= Math.sin(arm.progress * Math.PI) * 10;
            } else if (arm.punchType === 'flicker_jab') {
                cy += Math.sin(arm.progress * Math.PI) * 80;
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * 40;
            } else if (arm.punchType === 'smash') {
                // Ruddock's Smash - hybrid hook/uppercut
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * 140;
                cy += Math.sin(arm.progress * Math.PI) * 100;
            } else if (arm.punchType === 'gazelle_punch') {
                // Gazelle Punch - leaping hook
                cy -= Math.sin(arm.progress * Math.PI) * 50;
                cx += (side === 'left' ? -1 : 1) * Math.sin(arm.progress * Math.PI) * 100;
            } else if (arm.punchType === 'pull_counter') {
                // Pull counter - leans back slightly then strikes straight
                if (arm.progress < 0.3) {
                    cy += 20; cx += (side === 'left' ? -1 : 1) * 30;
                } else {
                    cx += (side === 'left' ? 1 : -1) * Math.sin(arm.progress * Math.PI) * 20;
                    cy -= Math.sin(arm.progress * Math.PI) * 10;
                }
            }

            let radius = 120 - (ease * 65);"""

content = re.sub(anim_pattern, new_anim, content, flags=re.DOTALL)

# Adjust power/cost of signature punches
cost_pattern = r"if \(punchType === 'haymaker' \|\| punchType === 'heavy_overhead' \|\| punchType === 'bolo'\) cost \*= 1\.5;"
new_cost = "if (['haymaker', 'heavy_overhead', 'bolo', 'smash', 'gazelle_punch', 'liver_shot'].includes(punchType)) cost *= 1.5;"
content = re.sub(cost_pattern, new_cost, content)

dmg_pattern = r"if \(\['haymaker','heavy_overhead','bolo'\].includes\(player\.arms\.left\.punchType\)\) \|\|"
# I'll just change the line entirely

dmg_search = """if ((player.arms.left.state === 'retracting' && ['haymaker','heavy_overhead','bolo'].includes(player.arms.left.punchType)) ||
                    (player.arms.right.state === 'retracting' && ['haymaker','heavy_overhead','bolo'].includes(player.arms.right.punchType))) {"""
dmg_replace = """let heavyPunches = ['haymaker', 'heavy_overhead', 'bolo', 'smash', 'gazelle_punch', 'liver_shot', 'pull_counter'];
                if ((player.arms.left.state === 'retracting' && heavyPunches.includes(player.arms.left.punchType)) ||
                    (player.arms.right.state === 'retracting' && heavyPunches.includes(player.arms.right.punchType))) {"""
content = content.replace(dmg_search, dmg_replace)


with open("fight day.html", "w") as f:
    f.write(content)
