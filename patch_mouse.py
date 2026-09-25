import re

with open("fight day.html", "r") as f:
    content = f.read()

# I need to change:
# 1. Remove mouse crosshair calculations (or fix crossX/crossY to center)
# 2. Modify handlePunchInput to add Q and E as modifiers for punches for more punching styles (as requested: "add Q an E as modifiers for punches for more punching styles")
# 3. Add more details and realism in the movements. Currently, lean is mapped to keys.shift + WASD. We can add more subtle head bobbing or body sway to the opponent and player.
# 4. Remove mouse targeting: view.crossX and view.crossY should just point to center + opponent offset.
