const fs = require('fs');
let html = fs.readFileSync('fight day.html', 'utf8');
let scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
    fs.writeFileSync('game.js', scriptMatch[1]);
    console.log("Extracted game.js");
} else {
    console.log("No script tag found.");
}
