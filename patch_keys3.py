import re

with open("fight day.html", "r") as f:
    content = f.read()

# Let's check drawCrosshair and handlePunchInput and launchPunch and view.crossX.

# In handlePunchInput:
new_handlePunchInput = """function handlePunchInput() {
        if (keys.arrowleft && keys.arrowright) { player.isBlocking = true; }
        else {
            player.isBlocking = false;
            if (player.exhausted || player.dodgeState !== 'none') return;

            let modShift = keys.shift;
            let modQ = keys.q;
            let modE = keys.e;

            // Define custom styles with Q and E
            // Normal: overhead, uppercut, straight, straight
            // Shift: heavy_overhead, bolo, haymaker, haymaker
            // Q (Lead/Technical): jab, check hook, flicker jab, lead uppercut
            // E (Power/Inside): cross, body hook, shovel hook, overhand right

            // We can map these up for right/left depending on what makes sense.
            // Let's use simple string concatenation or logic:

            if (keys.arrowup && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'heavy_overhead');
                else if (modQ) launchPunch('right', 'flicker_jab');
                else if (modE) launchPunch('right', 'overhand');
                else launchPunch('right', 'overhead');
            }
            else if (keys.arrowdown && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'bolo');
                else if (modQ) launchPunch('left', 'lead_uppercut'); // wait, arrowdown was right uppercut
                else if (modE) launchPunch('right', 'shovel_hook');
                else launchPunch('right', 'uppercut');
            }
            else if (keys.arrowleft && player.arms.left.state === 'idle') {
                if (modShift) launchPunch('left', 'haymaker');
                else if (modQ) launchPunch('left', 'jab');
                else if (modE) launchPunch('left', 'body_hook');
                else launchPunch('left', 'straight'); // Left straight / hook
            }
            else if (keys.arrowright && player.arms.right.state === 'idle') {
                if (modShift) launchPunch('right', 'haymaker');
                else if (modQ) launchPunch('right', 'cross');
                else if (modE) launchPunch('right', 'body_hook');
                else launchPunch('right', 'straight');
            }
        }
    }"""
print(new_handlePunchInput)
