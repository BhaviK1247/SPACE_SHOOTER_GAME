# SPACE_SHOOTER_GAME
This is a simple space shooter game made in python.I used pygame library to code the game

Setting Up the Game World

The game opens in a space-themed window that’s about the size of your average browser. There’s a background that sets the mood, a UFO representing the player, an enemy floating across the top, and a bullet that you can fire. Everything moves in response to your keyboard, creating that familiar arcade game feel.

Controlling the UFO

As the player, you control a UFO near the bottom of the screen. You can move it left and right using the arrow keys. The movement is designed to be smooth, so it feels responsive. It’s a simple setup, but that’s part of what makes it fun. You’re focused entirely on aiming and reacting.

The Enemy Movement

There’s just one enemy on the screen at a time, but it’s not standing still. It glides left and right across the top of the screen. Each time it hits the edge, it drops slightly lower, slowly moving toward the player. This adds a layer of tension — you can’t wait too long to take the shot, or the enemy might get too close.

Shooting and Hitting the Target

Pressing the spacebar fires a bullet straight upward. Only one bullet can be active at a time, so you need to time your shots well. If the bullet hits the enemy, the enemy disappears and reappears at a new random position. This keeps things fresh and slightly unpredictable, which is great for replayability.

Keeping Score

Each time you land a hit, your score goes up. It’s displayed at the top corner of the screen, giving you a sense of progression. It’s a simple feedback loop — shoot, score, repeat — but it’s surprisingly satisfying.
