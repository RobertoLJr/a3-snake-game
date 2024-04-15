from board import Board
from food import Food
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
import time


FONT = ("Courier", 18, "normal")

# Setup window screen configuration
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")

# Setup Turtle configuration for menu writing
menu_pen = Turtle(visible=False)
menu_pen.speed(0)
menu_pen.color("lime")
menu_pen.penup()


def show_rules():
    """Write the rules of the game on the screen"""

    screen.clear()
    screen.bgcolor("black")

    menu_pen.goto(0, 200)
    menu_pen.write("Regras", align="center", font=("Courier", 24, "normal"))
    menu_pen.goto(screen.window_width() * -0.4, 100)
    menu_pen.write("1. Controle a cobra com as setas do teclado", align="left", font=FONT)
    menu_pen.goto(screen.window_width() * -0.4, 50)
    menu_pen.write("2. Leve a cobra até o ponto vermelho na tela", align="left", font=FONT)
    menu_pen.goto(screen.window_width() * -0.4, 0)
    menu_pen.write("3. Evite colidir com as paredes e consigo mesmo(a)", align="left", font=FONT)
    menu_pen.goto(screen.window_width() * -0.4, -50)
    menu_pen.write("4. Seus pontos serão vistos no topo da tela", align="left", font=FONT)
    menu_pen.goto(screen.window_width() * -0.4, -100)
    menu_pen.write("5. Tente passar a pontuação máxima!", align="left", font=FONT)

    menu_pen.goto(screen.window_width() * -0.4, -200)
    menu_pen.write("Pressione 'Enter' para retornar ao menu principal", align="left", font=FONT)
    screen.onkeypress(main_menu, "Return")


def start_game():
    """Start a new game"""

    screen.clear()
    screen.bgcolor("black")

    board = Board(screen.window_width(), screen.window_height())
    snake = Snake()
    food = Food(screen.window_width(), screen.window_height())
    scoreboard = Scoreboard(screen.window_height())

    screen.tracer(10)  # Allow for more rapid keyboard response for snake's character

    # Setup keyboard binding for snake controls
    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")

    # Allow for screen updates and character movement
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # TODO: Implement collision detection with food
        # TODO: Implement collision detection with walls
        # TODO: Implement collision detection with self


def quit_game():
    """End the game by closing the screen."""

    screen.clear()
    screen.bgcolor("black")
    menu_pen.goto(0, 0)
    menu_pen.write("ATÉ LOGO!", align="center", font=FONT)
    time.sleep(1.5)
    screen.bye()


def main_menu():
    screen.clear()
    screen.bgcolor("black")

    menu_pen.goto(0, 200)
    menu_pen.write("Snake Game", align="center", font=("Courier", 24, "normal"))
    menu_pen.goto(0, 100)
    menu_pen.write("Pressione 'R' para ler as regras", align="center", font=FONT)
    menu_pen.goto(0, 50)
    menu_pen.write("Pressione 'Enter' para começar o jogo", align="center", font=FONT)
    menu_pen.goto(0, 0)
    menu_pen.write("Pressione 'Esc' para sair", align="center", font=FONT)

    # Bind keyboard keys for menu
    screen.listen()
    screen.onkeypress(show_rules, "r")
    screen.onkeypress(start_game, "Return")
    screen.onkeypress(quit_game, "Escape")


if __name__ == "__main__":
    main_menu()
    screen.exitonclick()
