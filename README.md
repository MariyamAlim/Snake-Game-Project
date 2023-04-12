# Snake-Game-Project

This project is a game called snake, written in Python and uses the Pygame library. Its unique from other versions as users can select to play in easy or hard mode and each mode has its own challenges. 

## Installation Instructions:

- Install pygame

- Clone the repository

- Run game.py in the terminal using python game.py or your choice of IDE

## How To Play the Game
When the game starts the first screen you will see is the rules of the game.You will have 30 secs to read them before the game moves on to the next screen. <br>

The next screen will give you the option to select easy or hard. <br>

### Easy Mode
To select easy mode press the e key
  - The snake (brown) in brown will start moving towards the right automatically
  - The prey (green) will also appear in a random spot
  - Use the WASD keys to change directions for the snake
    - W - moves the snake up
    - A - moves the snake left
    - S - moves the snake down
    - D - moves the snake right <br>

You must control the snake to get it to consume the prey (green) and when it does the snake will increase in size by 1 everytime and so will the score.

When the score is greater than 10, a new prey (red) will appear where if the snake consumes it then its speed will increase. If the snake keeps consuming the prey (red) then the speed will keep increasing until it hits a specific value.

If you let the snake hit the window boundaries or you end up running the snake into itself, it will be game over and the window will close. 

### Hard Mode
To select hard mode press the h key
  - The snake (brown) in brown will start moving towards the right automatically
  - A computer controlled snake (blue) will also automatically appear and move around the screen randomly
  - The prey (green) will also appear in a random spot
  - Use the WASD keys to change directions for the snake
    - W - moves the snake up
    - A - moves the snake left
    - S - moves the snake down
    - D - moves the snake right <br>

You must control the snake (brown) to get it to consume the prey (green) and when it does the snake (brown) will increase in size by 1 everytime and so will the score. If snake (blue) consumes prey(green) it will also grow in size.

When the score is greater than 10, a new prey (red) will appear where if the snake(brown) consumes it then its speed will increase. If the snake(brown) keeps consuming the prey (red) then the speed will keep increasing until it hits a specific value. If snake(blue) consumes the prey(red) its speed will also incease.


If you let the snake (brown) hit the window boundaries, or you end up running the snake into itself, or it hits snake(blue) it will be game over and the window will close.
