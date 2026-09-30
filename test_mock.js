const fs = require('fs');

const mockHtml = `<html><body><canvas id="gameCanvas"></canvas><div id="menu-hub"></div><div id="playerColor"></div><div id="playerStance"></div><div id="playerCombatStyle"></div><div id="playerBlockStyle"></div><div id="playerName"></div></body></html>`;

const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(mockHtml);

global.document = dom.window.document;
global.window = dom.window;

try {
    require('./game.js');
    console.log("No runtime errors in JS!");
} catch (e) {
    console.error("Error executing JS:", e);
}
