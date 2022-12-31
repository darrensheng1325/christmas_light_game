from turtle import *
from read import *
import tkinter as tk
from threading import Thread

# These are global variables
turtle = None
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
map_data = []
block_data = None
availible_blocks = ["blank","lights_normal", "block", "turtle", "player"]
block_map = {0:"air",1:"light_normal",2:"block",3:"light_normal_45degrees"}
game_state = "main_menu"
level_num = 1
edit_block = 1

def reg_screen(name, shape):
    screen.register_shape(name=name, shape=shape)
    
def init_button(button, shape_name):
    button.shape(shape_name)
    button.penup()
    button.speed(100000)
    button.hideturtle()

def init_player():
    player_shape = Shape("image", tk.PhotoImage(file="char_main.png"))
    reg_screen("player", player_shape)
    player.shape("player")
    player.speed(100000)
    
def init_play_button():
    play_button_shape = Shape("image", tk.PhotoImage(file="play_button.png"))
    reg_screen("play_button", play_button_shape)
    play_button.shape("play_button")
    
def init_close_button():
    close_button_shape = Shape("image", tk.PhotoImage(file="close_button.png"))
    reg_screen("close_button", close_button_shape)
    close_button.shape("close_button")
    close_button.penup()

def init_back_button():    
    back_button_shape = Shape("image", tk.PhotoImage(file="back_button.png"))
    reg_screen("back_button", back_button_shape)
    init_button(back_button, "back_button")
    back_button.setpos(10000, -10000)
    
def init_main_menu_button():
    main_menu_button_shape = Shape("image", tk.PhotoImage(file="main_menu_button.png"))
    reg_screen("main_menu_button", main_menu_button_shape)
    init_button(main_menu_button, "main_menu_button")
    main_menu_button.setpos(10000, 10000)
    
def init_up_arrow():
    init_button(up_arrow, "arrow")
    up_arrow.left(90)
    
def init_down_arrow():
    init_button(down_arrow, "arrow")
    down_arrow.right(90)
    
def init_box():
    box_shape = Shape("image", tk.PhotoImage(file="box.png"))
    reg_screen("box", box_shape)
    box.shape("box")
    box.hideturtle()

def init_edit_button():
    edit_button_shape = Shape("image", tk.PhotoImage(file="edit_button.png"))
    reg_screen("edit_button", edit_button_shape)
    init_button(edit_button, "edit_button")
    
def init_variables():
    init_player()
    init_play_button()
    init_close_button()
    init_back_button()
    init_main_menu_button()
    init_up_arrow()
    init_down_arrow()
    init_box()
    init_edit_button()
    
    particles.hideturtle()
    
    turtle.speed(100000)
    
    lights_normal_shape = Shape("image", tk.PhotoImage(file="lights_normal.png"))
    reg_screen("lights_normal", lights_normal_shape)
    
    blank = Shape("image", tk.PhotoImage(file="blank.png"))
    reg_screen("blank", blank)
    
    block_visible_shape = Shape("image", tk.PhotoImage(file="block.png"))
    reg_screen("block", block_visible_shape)

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
    elif game_state == "level_select" or game_state == "edit":
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
    close_button.speed(100000)
    close_button.setpos(0, -60)
    
def close_game(x, y):
    global game_state
    game_state = "closed"
    screen.bye()
    
def debug():
    global game_state
    while True:
        try:
            command = input()
        except Exception:
            pass
        if command == "game_state":
            print(game_state)
        if command == "quit":
            close_game(0, 0)
            game_state = "closed"
            break
        if command == "level":
            try:
                for block in map_data:
                    print(block_map[block[2]])
            except Exception:
                pass
        if game_state == "closed":
            quit()
            
def game_loop():
    while True:
        if game_state == "play":
            up_arrow.hideturtle()
            down_arrow.hideturtle()
            box.hideturtle()
            play_button.hideturtle()
            edit_button.hideturtle()
        if game_state == "closed":
            quit()
            
def event_up_button_click(x, y):
    global level_num
    if not level_num == 1:
        level_num -= 1
    turtle.clear()
    turtle.write("Level " + str(level_num),font=("Comic Sans MS", 20, "normal"))
    
def event_down_button_click(x, y):
    global level_num
    level_num += 1
    turtle.clear()
    turtle.write("Level " + str(level_num),font=("Comic Sans MS", 20, "normal"))
    
def screen_click_event(x, y):
    global game_state
    global map_data
    global block_data
    if game_state == "edit":
        global avalible_blocks
        turtle.shape(availible_blocks[edit_block])
        turtle.showturtle()
        turtle.setpos(30*(x//30), 21*(y//21))
        turtle.stamp()
        block_data = []
        block_data.append(turtle.xcor())
        block_data.append(turtle.ycor())
        block_data.append(edit_block)
        map_data.append(block_data)
        
def edit(x, y):
    global game_state
    screen.bgpic("background.png")
    edit_button.hideturtle()
    box.hideturtle()
    turtle.clear()
    up_arrow.hideturtle()
    down_arrow.hideturtle()
    game_state = "edit"
    player.hideturtle()
    close_button.setpos(10000, 10000)
    
def make_event_fn(block_num):
    def event_fn():
        global edit_block
        edit_block = block_num
    return event_fn

init_variables()
init_game(0, 0)
back_button.onclick(init_game)
play_button.onclick(open_game)
close_button.onclick(close_game)
up_arrow.onclick(event_up_button_click)
down_arrow.onclick(event_down_button_click)
edit_button.onclick(edit)
for i in range(4):
    screen.onkey(make_event_fn(i), str(i))
screen.onclick(screen_click_event)

threads = [Thread(target=debug), Thread(target=game_loop)]
for thread in threads:
    thread.start()
screen.listen()
screen.mainloop()