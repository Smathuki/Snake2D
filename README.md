# Snake2D
# Snake Game using Pygame

This is a simple Snake game implemented using the Pygame library. The player controls a snake that moves around the grid, eating food to grow and avoiding collisions with obstacles and itself.

## How to Play

1. Install Python and Pygame.
2. Run the `Snake2d.py` script.
3. The game starts with a menu where you can press 'S' to start the game or 'E' to exit.
4. During the game, use the arrow keys to change the direction of the snake: UP, DOWN, LEFT, and RIGHT.
5. Press 'P' to pause the game, and press it again to resume.
6. If the snake collides with obstacles or itself, the game will end, and you'll have the option to start again from the menu.

## Game Components

### Snake

- The Snake class defines the behavior of the snake, including its movement, growth, and collision detection.

### Food

- The Food class generates random positions for food on the grid.

### Obstacle

- The Obstacle class generates random positions for obstacles on the grid.

### Game

- The Game class manages the game loop, handles user input, and updates the game state.

## Screen Settings

- The game screen is set to a width of 640 pixels and a height of 480 pixels.
- The grid is divided into cells of size 20x20 pixels.
- The game starts with one level, and the player earns points by eating food. Every 10 points, the player advances to the next level, increasing the difficulty with more obstacles.

## Colors

- Black: (0, 0, 0)
- White: (255, 255, 255)
- Red: (255, 0, 0)
- Green: (0, 255, 0)

## Controls

- Arrow keys: Change the direction of the snake.
- 'P': Pause the game during gameplay.
- 'S': Start the game from the menu.
- 'E': Exit the game from the menu or end the game.

## Requirements

- Python 3.x
- Pygame library

## How to Run

1. Clone this repository.
2. Install Python and Pygame.
3. Open a terminal or command prompt and navigate to the repository folder.
4. Run the command: `python Snake2d.py`.

Have fun playing the Snake game!
