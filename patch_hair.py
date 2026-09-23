import re

with open('fight day.html', 'r') as f:
    content = f.read()

# Update generateOpponent to include hair and hairColor
build_replacement = """        let build = {
            scaleX: 0.85 + (Math.random() * 0.4), scaleY: 0.9 + (Math.random() * 0.3),
            muscle: 0.5 + Math.random() * 1.5, belly: Math.random() > 0.7 ? Math.random() : 0,
            jaw: 0.8 + (Math.random() * 0.5),
            hair: ['bald', 'buzzcut', 'mohawk', 'afro', 'fade'][Math.floor(Math.random() * 5)],
            hairColor: ['#111', '#4a2511', '#e8b831', '#8b2e16'][Math.floor(Math.random() * 4)]
        };"""

content = re.sub(r'let build = \{[\s\S]*?jaw: 0.8 \+ \(Math.random\(\) \* 0\.5\)\s*\};', build_replacement, content)

# Update drawOpponentProcedural to draw the hair
head_draw_regex = r'(ctx\.bezierCurveTo\(-hw \+ 5, 25, -hw - 5, -10, -hw, -hh\); ctx\.fill\(\);)'
hair_draw = r"""\1

        // Draw Hair
        ctx.fillStyle = b.hairColor || '#111';
        if (b.hair === 'buzzcut') {
            ctx.beginPath(); ctx.ellipse(0, -hh - 12, hw + 2, 8, 0, 0, Math.PI*2); ctx.fill();
        } else if (b.hair === 'mohawk') {
            ctx.beginPath(); ctx.moveTo(-15, -hh - 10); ctx.lineTo(-10, -hh - 40); ctx.lineTo(0, -hh - 50); ctx.lineTo(10, -hh - 40); ctx.lineTo(15, -hh - 10); ctx.fill();
        } else if (b.hair === 'afro') {
            ctx.beginPath(); ctx.arc(-20, -hh - 15, 20, 0, Math.PI*2); ctx.arc(0, -hh - 25, 25, 0, Math.PI*2); ctx.arc(20, -hh - 15, 20, 0, Math.PI*2); ctx.fill();
        } else if (b.hair === 'fade') {
            ctx.beginPath(); ctx.ellipse(0, -hh - 15, hw - 5, 12, 0, 0, Math.PI*2); ctx.fill();
            ctx.fillRect(-hw, -hh, hw*2, 15);
        }
"""

content = re.sub(head_draw_regex, hair_draw, content)

with open('fight day.html', 'w') as f:
    f.write(content)
