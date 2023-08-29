import sys
import pygame
import time
import random
from random import choice
from turtle import *
from freegames import floor, vector

def rps():
    play_remaining=10
    assistant_wins=0
    user_wins=0


    print("\t \t \t  r  =  Rock  :   p  =  Paper  :  s =  Scissor (....Enter Q to stop)  \n")

    while (play_remaining>0):
        print(f"\n[ Number of plays remaining: {play_remaining} ]")
        play_remaining-=1
        user_input = input("Enter Your Choice.......  \n")
        user_input=user_input.lower()
        assistant_input = (random.choice(["s","p","k"]))

        if user_input=="q":
            print(".........GAME END......... \n \n \n")
            print("Wait a moment to return to Assistant")
            break
            

        elif user_input == assistant_input:
            print("Both are same !!!!!")

        elif user_input == 'r' and assistant_input == 'p':
            print("Assistant won.....You lose....!!")
            assistant_wins+=1

        elif user_input == 'p' and assistant_input == 'r':
            print("You Won !!")
            user_wins+=1

        elif user_input == 'r' and assistant_input == 's':
            print("You Won !!")
            user_wins+=1

        elif user_input == 's' and assistant_input == 'r':
            print("Assistant won.....You lose....!!")
            assistant_wins+=1

        elif user_input == 's' and assistant_input == 'p':
            print("You Won !!")
            user_wins+=1

        elif user_input == 'p' and assistant_input == 's':
            print("Assistant won.....You lose....!!")
            assistant_wins+=1

        else:
            print("You Entered Wrong input....try again")


    print(f"\nAssistant score: {assistant_wins}\n Your score: {user_wins}")
    print("\nWait a moment to return to Assistant")

def math_game():
    print("\nWelcome to the math game!\n")
    print("You will be given 2 integers and must enter the result of this calculation.")
    print("Try to answer correctly as much as possible!")
    print("If you want to quit and return to Assistant, type q\n")
    print("Start!!!")
    score = 0
    while True:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        op = random.choice(["+", "-", "*"])
        user_answer = "0"

        correct_answer = eval(f"{a} {op} {b}")
        user_answer = input(f"{a} {op} {b} = ")

        while a < b:
            a = random.randint(1, 100)
            b = random.randint(1, 100)

            if a > b:
                break

        if user_answer == "q":
            print("\nWait a moment to return to Assistant")
            break
        elif user_answer.isdigit():
             if int(user_answer) == correct_answer:
                score += 1
                print("Correct!")
        else:
            print(f"Incorrect! Your answer is {correct_answer}")
    print(f"You're answer correct {score} questions.")

def pacman():
    state = {'score': 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    aim = vector(5, 0)
    pacman = vector(-40, -80)
    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    # fmt: off
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]
    # fmt: on


    def square(x, y):
        """Draw square using path at (x, y)."""
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()


    def offset(point):
        """Return offset of point in tiles."""
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index


    def valid(point):
        """Return True if point is valid in tiles."""
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0


    def world():
        """Draw world using path."""
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')


    def move():
        """Move pacman and all ghosts."""
        writer.undo()
        writer.write(state['score'])

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, 'yellow')

        for point, course in ghosts:
            if valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        update()

        for point, course in ghosts:
            if abs(pacman - point) < 20:
                return

        ontimer(move, 100)


    def change(x, y):
        """Change pacman aim if valid."""
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 160)
    writer.color('white')
    writer.write(state['score'])
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
    move()
    done()

def tetris():
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    GRID_SIZE = 25

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    COLORS = [RED, BLUE, GREEN]

    # Tetromino shapes
    SHAPES = [
        [
            ['.....',
            '.....',
            '.....',
            'OOOO.',
            '.....'],
            ['.....',
            '..O..',
            '..O..',
            '..O..',
            '..O..']
        ],
        [
            ['.....',
            '.....',
            '..O..',
            '.OOO.',
            '.....'],
            ['.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....'],
            ['.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'],
            ['.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....']
        ],
        [
            [
            '.....',
            '.....',
            '..OO.',
            '.OO..',
            '.....'],
            ['.....',
            '.....',
            '.OO..',
            '..OO.',
            '.....'],
            ['.....',
            '.O...',
            '.OO..',
            '..O..',
            '.....'],
            ['.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....']
        ],
        [
            ['.....',
            '..O..',
            '..O.',
            '..OO.',
            '.....'],
            ['.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'],
            ['.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....'],
            ['.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....']
        ],
    ]


    class Tetromino:
        def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = random.choice(COLORS) # You can choose different colors for each shape
            self.rotation = 0


    class Tetris:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.grid = [[0 for _ in range(width)] for _ in range(height)]
            self.current_piece = self.new_piece()
            self.game_over = False
            self.score = 0  # Add score attribute

        def new_piece(self):
            # Choose a random shape
            shape = random.choice(SHAPES)
            # Return a new Tetromino object
            return Tetromino(self.width // 2, 0, shape)

        def valid_move(self, piece, x, y, rotation):
            """Check if the piece can move to the given position"""
            for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
                for j, cell in enumerate(row):
                    try:
                        if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
                            return False
                    except IndexError:
                        return False
            return True

        def clear_lines(self):
            """Clear the lines that are full and return the number of cleared lines"""
            lines_cleared = 0
            for i, row in enumerate(self.grid[:-1]):
                if all(cell != 0 for cell in row):
                    lines_cleared += 1
                    del self.grid[i]
                    self.grid.insert(0, [0 for _ in range(self.width)])
            return lines_cleared

        def lock_piece(self, piece):
            """Lock the piece in place and create a new piece"""
            for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        self.grid[piece.y + i][piece.x + j] = piece.color
            # Clear the lines and update the score
            lines_cleared = self.clear_lines()
            self.score += lines_cleared * 100  # Update the score based on the number of cleared lines
            # Create a new piece
            self.current_piece = self.new_piece()
            # Check if the game is over
            if not self.valid_move(self.current_piece, 0, 0, 0):
                self.game_over = True
            return lines_cleared

        def update(self):
            """Move the tetromino down one cell"""
            if not self.game_over:
                if self.valid_move(self.current_piece, 0, 1, 0):
                    self.current_piece.y += 1
                else:
                    self.lock_piece(self.current_piece)

        def draw(self, screen):
            """Draw the grid and the current piece"""
            for y, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

            if self.current_piece:
                for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                    for j, cell in enumerate(row):
                        if cell == 'O':
                            pygame.draw.rect(screen, self.current_piece.color, ((self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))


    def draw_score(screen, score, x, y):
        """Draw the score on the screen"""
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (x, y))
        
        
    def draw_game_over(screen, x, y):
        """Draw the game over text on the screen"""
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (x, y))


    def main():
        # Initialize pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tetris Game (Made by Thai Minh Nguyen)')
        # Create a clock object
        clock = pygame.time.Clock()
        # Create a Tetris object
        game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
        fall_time = 0
        fall_speed = 50  # You can adjust this value to change the falling speed, it's in milliseconds
        while True:
            # Fill the screen with black
            screen.fill(BLACK) 
            for event in pygame.event.get():
                # Check for the QUIT event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Check for the KEYDOWN event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if game.valid_move(game.current_piece, -1, 0, 0):
                            game.current_piece.x -= 1 # Move the piece to the left
                    if event.key == pygame.K_RIGHT:
                        if game.valid_move(game.current_piece, 1, 0, 0):
                            game.current_piece.x += 1 # Move the piece to the right
                    if event.key == pygame.K_DOWN:
                        if game.valid_move(game.current_piece, 0, 1, 0):
                            game.current_piece.y += 1 # Move the piece down
                    if event.key == pygame.K_UP:
                        if game.valid_move(game.current_piece, 0, 0, 1):
                            game.current_piece.rotation += 1 # Rotate the piece
                    if event.key == pygame.K_SPACE:
                        while game.valid_move(game.current_piece, 0, 1, 0):
                            game.current_piece.y += 1 # Move the piece down until it hits the bottom
                        game.lock_piece(game.current_piece) # Lock the piece in place
            # Get the number of milliseconds since the last frame
            delta_time = clock.get_rawtime() 
            # Add the delta time to the fall time
            fall_time += delta_time 
            if fall_time >= fall_speed:
                # Move the piece down
                game.update()
                # Reset the fall time
                fall_time = 0
            # Draw the score on the screen
            draw_score(screen, game.score, 10, 10)
            # Draw the grid and the current piece
            game.draw(screen)
            if game.game_over:
                # Draw the "Game Over" message
                draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message
                # You can add a "Press any key to restart" message here
                # Check for the KEYDOWN event
                if event.type == pygame.KEYDOWN:
                    # Create a new Tetris object
                    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
            # Update the display
            pygame.display.flip()
            # Set the framerate
            clock.tick(60)


    if __name__ == "__main__":
        main()

def snake():
    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake (Made by Thai Minh Nguyen)')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):

        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)
        
        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)
        
        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()
        
        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():

        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)
        
        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        
        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (window_x/2, window_y/4)
        
        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the program
        time.sleep(2)
        
        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()


    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)