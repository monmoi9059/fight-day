1. **Hairstyles:**
   - Add a `hair` property to `opponent.build` (type: 'bald', 'buzzcut', 'mohawk', 'afro', 'fade').
   - Add a `hairColor` property to `opponent.build`.
   - Update `drawOpponentProcedural()` to draw the hair based on the type on top of the head.

2. **Counter Punches:**
   - Add a `counterWindow` to the `player` object.
   - When the player successfully slips/dodges an opponent's punch, set `player.counterWindow = 1000` (1 second).
   - In `resolvePlayerHit`, if `player.counterWindow > 0`, multiply damage by 2.5, add a "COUNTER PUNCH!" text, increase camera shake and hit stop, and spawn more particles.
   - Decrease `player.counterWindow` by `dt` in the `update` loop.

3. **Body Movement Control:**
   - Update `keys` to track `shift`.
   - Update the UI to explain `Shift + WASD` for body movement.
   - In the `update` loop, if `keys.shift` is held, WASD modifies `player.targetLeanX` and `player.targetLeanY` instead of moving the player in the ring.
   - Smoothly interpolate `player.dodgeOffset` to `player.targetLeanX` and `player.leanYOffset` to `player.targetLeanY`.
   - Adjust `view.screenY` and `view.scale` using `player.leanYOffset`.
   - Update opponent punch logic so that if the player is leaning sufficiently (X or Y), the punch misses, triggering the `SLIP!` text and the counter window.
