# Aircraft Adventure Game

A simple 2D aircraft flying game built with Pygame where players control an aircraft, shoot enemies, and try to achieve the highest score possible.

![Aircraft Adventure Game](screenshots/gameplay.png)

## Features

- Player-controlled aircraft that moves across the screen
- Enemy aircraft that spawn randomly from the top
- Shooting mechanics to destroy enemy aircraft
- Score tracking system
- Game over condition when colliding with enemies
- Simple and intuitive controls
- Clean visual design with sky-themed background

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/aircraft-adventure.git
cd aircraft-adventure
```

2. Install the required dependencies:
```bash
# Using pip
pip install pygame

# Or using apt on Debian/Ubuntu
sudo apt-get install python3-pygame
```

## How to Play

Run the game:
```bash
python3 aircraft_game.py
```

### Controls

- **Arrow keys** or **WASD**: Move the aircraft
  - Left/Right: Move horizontally
  - Up/Down: Limited vertical movement
- **Spacebar**: Fire bullets
- **R**: Restart the game after Game Over

### Gameplay

- Control your blue aircraft at the bottom of the screen
- Shoot the red enemy aircraft coming from the top
- Each destroyed enemy gives you 10 points
- Avoid colliding with enemy aircraft
- Try to achieve the highest score possible!

## Game Structure

The game is built using Pygame and consists of the following components:

- **Game Window**: 800x600 pixels with a sky-themed background
- **Player Aircraft**: Blue triangle controlled by the player
- **Enemy Aircraft**: Red triangles that move downward
- **Bullets**: Red rectangles that travel upward
- **Score System**: Tracks and displays the player's score
- **Game Over**: Displays when the player collides with an enemy

## Code Structure

- `aircraft_game.py`: Main game file containing all the game logic
  - Initialization and setup
  - Game loop
  - Input handling
  - Collision detection
  - Drawing functions
  - Game state management

## Customization

You can customize various aspects of the game by modifying the constants at the beginning of the script:

- Screen dimensions
- Colors
- Player and enemy sizes
- Movement speeds
- Spawn rates
- And more!

## Future Improvements

- Add sound effects for shooting and explosions
- Implement different enemy types
- Add power-ups and special abilities
- Create levels with increasing difficulty
- Add a high score system
- Implement better graphics and animations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Created as a simple demonstration of game development with Python
