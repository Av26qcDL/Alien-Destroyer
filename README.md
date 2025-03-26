---

# Alien Destroyer

Alien Destroyer is a fun and action-packed 2D shooter game developed using Python and Pygame. Players take on the role of an earth-defending hero taking down alien invaders while dodging obstacles. Test your reflexes and aim in this thrilling arcade-style game!

## Features
- **Jump and shoot mechanics**: Players can jump to avoid obstacles and fire bullets at alien enemies.
- **Variety of enemies**: Battle challenging blue one-eyed and yellow five-eyed aliens.
- **Scoring System**: Gain points by successfully taking down aliens.
- **Explosions**: Visual feedback of alien destruction through explosion effects.
- **Engaging Graphics and Audio**: Enjoy custom background images, character assets, and sound effects for gunfire and explosions.

---

## Gameplay Instructions
1. **Starting the Game**: 
   - Launch the game. The start screen shows the game name and helpful instructions.
   - Press the `SPACE` key to begin.
   
2. **Controls**:
   - **Jump**: Press the `SPACE` key to jump over incoming obstacles. 
   - **Shoot**: Press the `F` key to fire bullets at aliens.
   
3. **Objective**: 
   - Avoid collisions with aliens and obstacles.
   - Shoot aliens to score points and achieve a high score.

4. **Game Over**:
   - The game ends if your character collides with an alien.
   - View your score and restart the game by pressing `SPACE`.

---

## Installation and Setup
1. **Prerequisites**:
   - Python 3.10+ installed on your system.
   - Git installed on your system
   - Install the Pygame library:
```shell script
pip install pygame
```

2. **Clone or Download This Repository**:
   - Clone this repository or download the ZIP file and extract it:
```shell script
git clone <https://github.com/Av26qcDL/Alien-Destroyer>
```

3. **Run the Game**:
   - Navigate to the project directory and execute the game file:
```shell script
python main.py
```

---

## Assets

The game uses the following assets located in the `assets` folder:
- **Graphics**:
  - Background (sky, ground)
  - Player character
  - Aliens (blue with one eye, yellow with five eyes)
  - Bullet sprite
  - Explosion sprite
  - UFO stand image
- **Sounds**:
  - Gunfire sound (`gun_fire.wav`)
  - Explosion sound (`explosion.wav`)
- **Font**:
  - The custom font `Momo.ttf` is used to render game text at various points.

---

## How It Works
- **Game Loop**: Manages events, updates states (player, obstacles, bullets), and renders the game.
- **Collision Detection**:
  - Clashes with aliens result in a game over.
  - Bullet collisions with aliens destroy both the bullet and the alien, incrementing the score and triggering an explosion effect.
- **Obstacle Movement**: Aliens move through the screen at a fixed speed. Players can jump over or destroy them.
- **Custom Scoring**: The score is displayed on-screen and increases when an alien is successfully destroyed.

---

## Planned Enhancements (Future Updates)
- Add new alien types with unique behaviors.
- Introduce power-ups or special weapons.
- Implement difficulty levels to challenge advanced players.

---

## Dependencies
The following Python library is required:
- **Pygame** [Installation](https://www.pygame.org/wiki/GettingStarted)

Install it using:
```shell script
pip install pygame
```

---

## Contributions
Contributions, bug reports, and feature requests are welcome! Simply open an issue or submit a pull request.

---

## License

This project is for educational and personal use. Feel free to modify and share it. For more information, refer to the `LICENSE` file.

---

Enjoy playing **Alien Destroyer**, and let us know your high scores!

---

Feel free to customize this further based on your preferences or specific details you'd like to include!
