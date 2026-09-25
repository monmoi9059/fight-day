1. **Remove Mouse Targeting**:
   - Modify `view.crossX` and `view.crossY` to map entirely to screen center (`512`, `384`) + player sway/lean + opponent tracking, ignoring `mouse.x` and `mouse.y`.
   - Remove `mousemove`, `mousedown`, `mouseup` listeners related to targeting.
   - Refactor `launchPunch` target generation: Rather than targeting a mouse crosshair, target the opponent's head or body directly based on punch type, factoring in player's accuracy.

2. **Q and E as Punch Modifiers**:
   - The user requested "add Q an E as modifiers for punches for more punching styles". Currently Q and E are used for dodging (`actions.dodgeLeft` / `actions.dodgeRight`). We need to move dodge to something else (maybe double tap A/D or just remove it in favor of lean, or map dodging to something else like Z and C, but let's just make Q/E modifiers). Wait, the prompt specifically asks to "add Q and E as modifiers for punches". We should unbind them from dodge, or map dodge to something else like Spacebar + A/D. Let's map dodge to Shift + A/D maybe? The lean is currently Shift + WASD. We can map Dodge to double-tap, or simply use `Z` and `C` for dodge, or `Space + A/D`. Let's just remove Dodge from Q/E and make Q/E modifiers in `handlePunchInput()`.
   - Add new punch types handling in `launchPunch` and `drawPlayerDetailed` to reflect these new styles. (e.g. `jab`, `cross`, `hook`, `body_hook`, `uppercut`, `bolo`, `overhand`, `shovel_hook`).

3. **Details and Realism in Movements**:
   - Add head bobbing/breathing animation in the update loop (sine waves to `player.worldY` or camera `screenY`).
   - Opponent realistic movement (add a subtle sway or bob to the opponent).
   - In `drawPlayerDetailed`, add more dynamic animations for the new punch types.
   - Make the `view.dist` effect on camera field of view more dramatic.

4. **Pre-commit checks**:
   - Ensure the new logic doesn't break the existing rendering and fight loop. Verify with test file.
