1. **Modify HTML UI**:
   - Add dropdown for `Stance (Handedness)`: Orthodox (Righty), Southpaw (Lefty).
   - Add dropdown for `Combat Style`: Outboxer, Inside Puncher, Peek-A-Boo, Showboat, Mayweather Money Style.
   - Add dropdown for `Blocking Style`: Normal, Philly Shell.
   - Update CSS to support `select` elements in `.form-group`.

2. **Update Game State (`player` object)**:
   - Add `handedness`, `combatStyle`, `blockStyle` to the `player` object with default values.

3. **Apply Stats Effects on Career Start**:
   - In `startCareer()`, read values from the dropdowns and set them on `player`.
   - Apply base stats modifiers based on the chosen combat style and block style.

4. **Visual Updates (`drawPlayerDetailed`)**:
   - Adjust `leftShoulderY/X` and `rightShoulderY/X` based on `player.handedness` to show the weak side shoulder forward (closer/more prominent).
   - Adjust idle hand positions (`baseX`, `baseY`) based on `player.combatStyle` (e.g., high for Peek-A-Boo, low for Showboat, asymmetric for Mayweather).
   - Adjust blocking visual positions based on `player.blockStyle` (Philly Shell vs Normal).

5. **Verify Changes**:
   - Start a python server, verify the UI displays correctly.
   - Verify styles affect stats.
   - Verify visuals adjust when stances and styles are changed.

6. **Pre-commit Steps**: Ensure tests/verifications/reviews pass using `pre_commit_instructions`.

7. **Submit Code**: Once verified, submit.
