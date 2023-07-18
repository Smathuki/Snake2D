import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 640
screen_height = 480
cell_size = 20
grid_width = screen_width // cell_size
grid_height = screen_height // cell_size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(grid_width // 2, grid_height // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % grid_width, (head_y + dy) % grid_height)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail_x, tail_y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((tail_x - dx) % grid_width, (tail_y - dy) % grid_height)
        self.body.append(new_tail)

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def check_collision(self):
        return len(set(self.body)) != len(self.body)

    def draw(self, surface):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(surface, green, (x * cell_size, y * cell_size, cell_size, cell_size))

# Food class
class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        return random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, red, (x * cell_size, y * cell_size, cell_size, cell_size))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.position = self.generate_obstacle_position()

    def generate_obstacle_position(self):
        return random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, white, (x * cell_size, y * cell_size, cell_size, cell_size))

# Game class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.obstacles = []
        self.current_level = 1
        self.points = 0
        self.is_running = False
        self.is_paused = False

    def generate_obstacles(self):
        num_obstacles = min(self.current_level + 2, 15)  # Maximum 15 obstacles
        self.obstacles = [Obstacle() for _ in range(num_obstacles)]

    def start(self):
        self.is_running = True
        self.current_level = 1
        self.points = 0
        self.generate_obstacles()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if self.is_running:
                    self.handle_game_input(event.key)
                else:
                    self.handle_start_menu_input(event.key)

    def handle_game_input(self, key):
        dx, dy = self.snake.direction
        if key == pygame.K_UP and dy != 1:
            self.snake.change_direction(0, -1)
        elif key == pygame.K_DOWN and dy != -1:
            self.snake.change_direction(0, 1)
        elif key == pygame.K_LEFT and dx != 1:
            self.snake.change_direction(-1, 0)
        elif key == pygame.K_RIGHT and dx != -1:
            self.snake.change_direction(1, 0)
        elif key == pygame.K_p:
            self.is_paused = not self.is_paused  # Toggle pause state
        elif key == pygame.K_e:
            self.is_running = False  # Exit the game

    def handle_start_menu_input(self, key):
        if key == pygame.K_s:
            self.start()
            while self.is_running:
                self.handle_input()
                self.update()
                self.draw()
                self.clock.tick(10)  # Control snake's speed here
        elif key == pygame.K_e:
            pygame.quit()
            exit()

    def update(self):
        if self.is_running and not self.is_paused:
            self.snake.move()

            # Check if snake eats the food
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.position = self.food.generate_food_position()
                self.points += 1

                # Check if the player should level up
                if self.points % 10 == 0:
                    self.current_level += 1
                    self.generate_obstacles()

            # Check for collision with obstacles
            for obstacle in self.obstacles:
                if self.snake.body[0] == obstacle.position:
                    self.is_running = False

            # Check for self-collision
            for segment in self.snake.body[1:]:  # Start from the second segment (not the head)
                if self.snake.body[0] == segment:
                    self.is_running = False

            # Check for collision with the walls
            head_x, head_y = self.snake.body[0]
            if head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height:
                self.is_running = False

            if not self.is_running:
                self.reset()  # Reset the game after failure

    def draw(self):
        self.screen.fill(black)

        # Draw the obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Draw point counter
        font = pygame.font.Font(None, 30)
        points_text = font.render(f"Points: {self.points}", True, white)
        self.screen.blit(points_text, (10, 10))

        # Draw level indicator
        level_text = font.render(f"Level: {self.current_level}", True, white)
        self.screen.blit(level_text, (screen_width - level_text.get_width() - 10, 10))

        pygame.display.flip()

    def reset(self):
        self.snake = Snake()  # Reset the snake's length
        self.food = Food()
        self.obstacles = []
        self.current_level = 1
        self.points = 0
        self.generate_obstacles()

    def start_menu(self):
        is_menu_running = True
        font = pygame.font.Font(None, 36)

        while is_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]:
                self.start()
                while self.is_running:
                    self.handle_input()
                    self.update()
                    self.draw()
                    self.clock.tick(10)  # Control snake's speed here

            if keys[pygame.K_e]:
                pygame.quit()
                exit()

            # Clear the screen and draw the start menu
            self.screen.fill(black)
            start_text = font.render("Press 'S' to start or 'E' to exit", True, white)
            self.screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))
            pygame.display.flip()

    def run(self):
        self.start_menu()

# Create an instance of the Game class
game = Game()

# Start the game loop
game.run()
