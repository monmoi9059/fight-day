1. **Opponent Fighting Styles:**
   - Add a `fightingStyle` property to `opponent` which affects movement and punching.
   - The styles will be assigned based on the `buildClass` during `generateOpponent()` or randomly:
     - `brawler`: Aggressive, slow wide hooks, higher power multiplier, moves closer (shorter optimal dist).
     - `outboxer`: Defensive, faster straight punches, maintains range (longer optimal dist), retreats more often.
     - `swarmer`: Very aggressive, constant pressure, fast movement, low power multiplier.
     - `slugger`: Very slow, but extremely high power multiplier, moves slowly towards the player.
   - We will assign this in `generateOpponent()` and add it to `opponent.fightingStyle`.
   - Update `styleDesc` to include the fighting style explicitly.
   - Default opponent should have `fightingStyle: 'outboxer'`.

2. **Movement Style Integration:**
   - In `updateOpponent(dt)` logic:
     - Use `opponent.fightingStyle` to modify `optimalDist` and `oSpeed`.
     - `brawler` / `swarmer`: Shorter `optimalDist`.
     - `outboxer`: Longer `optimalDist`.
     - `swarmer`: Higher `oSpeed`.
     - `slugger`: Lower `oSpeed`.

3. **Punching Style Integration:**
   - In `updateOpponent(dt)` punch logic (`opponent.state === 'idle' -> 'windup'`):
     - `brawler` / `swarmer` / `slugger`: Increase aggro checks or alter windup times based on style.
     - `brawler`: Longer windup.
     - `swarmer`: Shorter windup.
   - In `drawOpponentProcedural()`:
     - Draw different windup arm angles based on style. For example, `brawler` and `slugger` have wider hooks (larger `lx` or `rx`), while `outboxer` has tighter, straighter punches.

4. **Verify Implementation:**
   - Read the changes in `fight day.html` to confirm opponent fighting style properties, movement adjustments, and rendering updates were correctly applied.

5. **Pre-commit Checks:**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
