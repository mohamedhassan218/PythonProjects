import random
import curses

# Create screan object.
myScrean = curses.initscr()

# Change the state of the cursor to be 0 (invisible)
curses.curs_set(0)

# Get maximum high and maximum width of the screan.
screanHight, screanWidth = myScrean.getmaxyx()

# Create new window with screanHight and screanWidth.
screan = curses.newwin(screanHight, screanWidth, 0, 0)

# Allow the screan to take input from the keyboard.
screan.keypad(1)

# Set delay for updating the screan.
screan.timeout(90)

# Set x, y coordinates of the initial position of the snake.
snakeX = screanWidth // 3
snakeY = screanHight // 3

# Define intial position of the body of the snake.
snake = [
    [snakeY, snakeX],
    [snakeY, snakeX - 1],
    [snakeY, snakeX - 2]
]

# Create the food in the middle of the window.
food = [screanHight // 2, screanWidth // 2]

# Add the food as a block in the origin of the screan.
screan.addch(food[0], food[1], curses.ACS_BLOCK)

# Set the initial movement direction to right.
key = curses.KEY_RIGHT

# Create infinite loop.
while True:
    nextKey = screan.getch()
    
    """
    If user doens't input anything, key remains same. Else, key
        will be set to the new key.
    Note the ternary operator in Python.
    """
    key = key if nextKey == -1 else nextKey


    """
    Check if the snake collided with itself or with the walls.
    Note the list slicing in snake list.
    endwin() to close the window.
    quit() to exit the program.
    """
    if snake[0][0] in [0, screanHight] or snake[0][1] in [0, screanWidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit() 
    
    # Set the new position of the snake based on the direction taken from user.
    newHead = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        newHead[0] += 1 
    elif key == curses.KEY_UP:
        newHead[0] -= 1
    elif key == curses.KEY_RIGHT:
        newHead[1] += 1
    elif key == curses.KEY_LEFT:
        newHead[1] -= 1
    
    snake.insert(0, newHead)

    # Check if the snake ate the food.
    if snake[0] == food:
        food = None
        while food is None:
            newFood = [
                random.randint(1, screanHight - 1),
                random.randint(1, screanWidth - 1)
            ]
            # Ensure that the food isn't on the body of the snake.
            food = newFood if newFood not in snake else None 
        
        screan.addch(food[0], food[1], curses.ACS_BLOCK)
    else:
        snakeTail = snake.pop()
        screan.addch(snakeTail[0], snakeTail[1], ' ')
        
        screan.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND)
