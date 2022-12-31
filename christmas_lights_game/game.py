from turtle import *
from read import *
import tkinter as tk
from threading import Thread
turtle = Turtle()
player = Turtle()
screen = Screen()
play_button = Turtle()
close_button = Turtle()
particles = Turtle()
back_button = Turtle()
main_menu_button = Turtle()
up_arrow = Turtle()
down_arrow = Turtle()
box = Turtle()
edit_button = Turtle()
mapdata = []
blockdata = None
availible_blocks = ["blank","lights_normal", "block", "turtle", "player"]
blockmap = {0:"air",1:"light_normal",2:"block",3:"light_normal_45degrees"}
game_state = "main_menu"
level_num = 1
edit_block = 1
player_shape = Shape('image', tk.PhotoImage(file='char_main.png'))
screen.register_shape(name='player', shape=player_shape)
player.shape("player")
play_button_shape = Shape('image', tk.PhotoImage(file='play_button.png'))
screen.register_shape(name='play_button', shape=play_button_shape)
play_button.shape("play_button")
close_button_shape = Shape('image', tk.PhotoImage(file='close_button.png'))
screen.register_shape(name='close_button', shape=close_button_shape)
close_button.shape("close_button")
close_button.penup()
close_button.setpos(0, -60)
back_button_shape = Shape('image', tk.PhotoImage(file='back_button.png'))
screen.register_shape(name='back_button', shape=back_button_shape)
back_button.shape("back_button")
back_button.speed(100000)
back_button.hideturtle()
back_button.penup()
back_button.setpos(10000, -10000)
main_menu_button_shape = Shape('image', tk.PhotoImage(file='main_menu_button.png'))
screen.register_shape(name='main_menu_button', shape=main_menu_button_shape)
main_menu_button.shape("main_menu_button")
main_menu_button.hideturtle()
main_menu_button.penup()
main_menu_button.speed(100000)
main_menu_button.setpos(10000, 10000)
up_arrow.shape("arrow")
up_arrow.penup()
up_arrow.speed(100000)
up_arrow.left(90)
up_arrow.hideturtle()
down_arrow.penup()
down_arrow.speed(100000)
down_arrow.shape("arrow")
down_arrow.right(90)
down_arrow.hideturtle()
particles.hideturtle()
box_shape = Shape('image', tk.PhotoImage(file='box.png'))
screen.register_shape(name='box', shape=box_shape)
box.shape("box")
box.hideturtle()
turtle.speed(100000)
lights_normal_shape = Shape('image', tk.PhotoImage(file='lights_normal.png'))
screen.register_shape(name='lights_normal', shape=lights_normal_shape)
edit_button_shape = Shape('image', tk.PhotoImage(file='edit_button.png'))
screen.register_shape(name='edit_button', shape=edit_button_shape)
edit_button.shape("edit_button")
edit_button.hideturtle()
edit_button.speed(100000)
edit_button.penup()
blank = Shape('image', tk.PhotoImage(file='blank.png'))
screen.register_shape(name='blank', shape=blank)
block_visible_shape = Shape('image', tk.PhotoImage(file='block.png'))
screen.register_shape(name='block', shape=block_visible_shape)

def open_game(x, y):
    global game_state
    if game_state == "main_menu":
        game_state = "level_select"
        play_button.penup()
        play_button.setpos(155, 300)
        close_button.hideturtle()
        back_button.penup()
        back_button.setpos(-393, 380)
        back_button.showturtle()
        up_arrow.setpos(0, 380)
        down_arrow.setpos(0, -380)
        up_arrow.showturtle()
        down_arrow.showturtle()
        box.showturtle()
        edit_button.setpos(-390, 0)
        edit_button.showturtle()
        turtle.setpos(-35, -15)
        turtle.write("Level" + " " + str(level_num),font=("Comic Sans MS", 20, "normal"))
        player.showturtle()
    elif game_state == "level_select":
        game_state = "play"
        screen.bgpic("background.png")
        player.showturtle()
def init_game(x, y):
    global game_state
    game_state = "main_menu"
    screen.title("")
    turtle.penup()
    player.penup()
    turtle.hideturtle()
    screen.bgcolor("cyan")
    player.setpos(-393,-120)
    screen.bgpic("title_screen.png")
    player.shape("player")
    play_button.shape("play_button")
    play_button.showturtle()
    close_button.shape("close_button")
    back_button.shape("back_button")
    main_menu_button.shape("main_menu_button")
    back_button.hideturtle()
    back_button.setpos(10000, 10000)
    main_menu_button.hideturtle()
    main_menu_button.setpos(10000, 10000)
    play_button.showturtle()
    play_button.speed(100000)
    play_button.setpos(0, 0)
    close_button.showturtle()
    up_arrow.hideturtle()
    down_arrow.hideturtle()
    box.hideturtle()
    turtle.clear()
    edit_button.hideturtle()
    player.showturtle()
def closegame(x, y):
    game_state = "closed"
    screen.bye()
def debug():
    global game_state
    while True:
        command = input()
        if command == "game_state":
            print(game_state)
        if command == "quit":
            closegame(0, 0)
            game_state = "closed"
            break
        if command == "level":
            try:
                for block in mapdata:
                    print(blockmap[block[2]])
            except Exception:
                pass
        if game_state == "closed":
            quit()
def gameloop():
    while True:
        if game_state == "play":
            up_arrow.hideturtle()
            down_arrow.hideturtle()
            box.hideturtle()
            play_button.hideturtle()
            turtle.clear()
            edit_button.hideturtle()
        if game_state == "closed":
            quit()
def event_up_button_click(x, y):
    global level_num
    if not level_num == 1:
        level_num -= 1
    turtle.clear()
    turtle.write("Level" + " " + str(level_num),font=("Comic Sans MS", 20, "normal"))
def event_down_button_click(x, y):
    global level_num
    level_num += 1
    turtle.clear()
    turtle.write("Level" + " " + str(level_num),font=("Comic Sans MS", 20, "normal"))
def screen_click_event(x, y):
    global game_state
    global mapdata
    global blockdata
    if game_state == "edit":
        global avalible_blocks
        turtle.shape(availible_blocks[edit_block])
        turtle.showturtle()
        turtle.setpos(30*(x//30), 21*(y//21))
        turtle.stamp()
        blockdata = []
        blockdata.append(turtle.xcor())
        blockdata.append(turtle.ycor())
        blockdata.append(edit_block)
        mapdata.append(blockdata)
def edit(x, y):
    global game_state
    screen.bgpic("background.png")
    edit_button.hideturtle()
    play_button.hideturtle()
    box.hideturtle()
    turtle.clear()
    up_arrow.hideturtle()
    down_arrow.hideturtle()
    game_state = "edit"
    player.hideturtle()
def event_1():
    global edit_block
    edit_block = 1
def event_2():
    global edit_block
    edit_block = 2
def event_0():
    global edit_block
    edit_block = 0
def event_3():
    global edit_block
    edit_block = 3
def event_4():
    global edit_block
    edit_block = 4

init_game(0, 0)
back_button.onclick(init_game)
play_button.onclick(open_game)
close_button.onclick(closegame)
up_arrow.onclick(event_up_button_click)
down_arrow.onclick(event_down_button_click)
edit_button.onclick(edit)
screen.onkey(event_1, "1")
screen.onkey(event_2, "2")
screen.onkey(event_0, "0")
screen.onkey(event_3, "3")
screen.onkey(event_4, "4")
screen.onclick(screen_click_event)

threads = [Thread(target=debug), Thread(target=gameloop)]
for thread in threads:
    thread.start()
screen.listen()
screen.mainloop()