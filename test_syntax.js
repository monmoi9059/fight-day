const fs = require('fs');
let html = fs.readFileSync('fight day.html', 'utf8');
let snippet = html.substring(html.indexOf("} else if (arm.punchType === 'pull_counter') {"), html.indexOf("let radius = 120 - (ease * 65);") + 50);
console.log(snippet);
