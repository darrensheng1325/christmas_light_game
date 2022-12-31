from turtle import *
from read import *
import tkinter as tk
from threading import Thread

# These are global variables
turtle = Turtle()
player = Turtle()
screen = Screen()
box = Turtle()
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
    
def init_play_button(play_button):
    play_button_shape = Shape("image", tk.PhotoImage(file="play_button.png"))
    reg_screen("play_button", play_button_shape)
    play_button.shape("play_button")
    
def init_close_button(close_button):
    close_button_shape = Shape("image", tk.PhotoImage(file="close_button.png"))
    reg_screen("close_button", close_button_shape)
    close_button.shape("close_button")
    close_button.penup()

def init_back_button(back_button):    
    back_button_shape = Shape("image", tk.PhotoImage(file="back_button.png"))
    reg_screen("back_button", back_button_shape)
    init_button(back_button, "back_button")
    back_button.setpos(10000, -10000)
    
def init_up_arrow(up_arrow):
    init_button(up_arrow, "arrow")
    up_arrow.left(90)
    
def init_down_arrow(down_arrow):
    init_button(down_arrow, "arrow")
    down_arrow.right(90)
    
def init_box():
    box_shape = Shape("image", tk.PhotoImage(file="box.png"))
    reg_screen("box", box_shape)
    box.shape("box")
    box.hideturtle()

def init_edit_button(edit_button):
    edit_button_shape = Shape("image", tk.PhotoImage(file="edit_button.png"))
    reg_screen("edit_button", edit_button_shape)
    init_button(edit_button, "edit_button")
    
def init_buttons():
    buttons = Buttons()
    init_play_button(buttons.play)
    buttons.play.onclick(make_open_game_fn(buttons))
    
    init_close_button(buttons.close)
    buttons.close.onclick(close_game)
    
    init_edit_button(buttons.edit)
    buttons.edit.onclick(make_edit(buttons))
    
    init_back_button(buttons.back)
    buttons.back.onclick(make_init_game_fn(buttons))
    
    init_up_arrow(buttons.up_arrow)
    buttons.up_arrow.onclick(event_up_button_click)
    
    init_down_arrow(buttons.down_arrow)
    buttons.down_arrow.onclick(event_down_button_click)
    
    return buttons
    
def init_variables():
    init_player()
    init_box()
    
    turtle.speed(100000)
    
    lights_normal_shape = Shape("image", tk.PhotoImage(file="lights_normal.png"))
    reg_screen("lights_normal", lights_normal_shape)
    
    blank = Shape("image", tk.PhotoImage(file="blank.png"))
    reg_screen("blank", blank)
    
    block_visible_shape = Shape("image", tk.PhotoImage(file="block.png"))
    reg_screen("block", block_visible_shape)

def make_open_game_fn(buttons):
    def open_game(x, y):
        global game_state
        if game_state == "main_menu":
            game_state = "level_select"
            buttons.play.penup()
            buttons.play.setpos(155, 300)
            buttons.close.hideturtle()
            buttons.back.penup()
            buttons.back.setpos(-393, 380)
            buttons.back.showturtle()
            buttons.up_arrow.setpos(0, 380)
            buttons.down_arrow.setpos(0, -380)
            buttons.up_arrow.showturtle()
            buttons.down_arrow.showturtle()
            box.showturtle()
            buttons.edit.setpos(-390, 0)
            buttons.edit.showturtle()
            turtle.setpos(-35, -15)
            turtle.write("Level " + str(level_num),font=("Comic Sans MS", 20, "normal"))
            player.showturtle()
        elif game_state == "level_select" or game_state == "edit":
            game_state = "play"
            screen.bgpic("background.png")
            player.showturtle()
    return open_game

def make_init_game_fn(buttons):
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
        buttons.play.shape("play_button")
        buttons.play.showturtle()
        buttons.close.shape("close_button")
        buttons.back.shape("back_button")
        buttons.back.hideturtle()
        buttons.back.setpos(10000, 10000)
        buttons.play.showturtle()
        buttons.play.speed(100000)
        buttons.play.setpos(0, 0)
        buttons.close.showturtle()
        buttons.up_arrow.hideturtle()
        buttons.down_arrow.hideturtle()
        box.hideturtle()
        turtle.clear()
        buttons.edit.hideturtle()
        player.showturtle()
        buttons.close.speed(100000)
        buttons.close.setpos(0, -60)
    return init_game
    
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
def make_game_loop(buttons):            
    def game_loop():
        while True:
            if game_state == "play":
                buttons.up_arrow.hideturtle()
                buttons.down_arrow.hideturtle()
                box.hideturtle()
                buttons.play.hideturtle()
                buttons.edit.hideturtle()
            if game_state == "closed":
                quit()
    return game_loop
            
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

def make_edit(buttons):        
    def edit(x, y):
        global game_state
        screen.bgpic("background.png")
        buttons.edit.hideturtle()
        box.hideturtle()
        turtle.clear()
        buttons.up_arrow.hideturtle()
        buttons.down_arrow.hideturtle()
        game_state = "edit"
        player.hideturtle()
        buttons.close.setpos(10000, 10000)
    return edit
        
def make_event_fn(block_num):
    def event_fn():
        global edit_block
        edit_block = block_num
    return event_fn

class Buttons(object):
    def __init__(self):
        self.edit = Turtle()
        self.close = Turtle()
        self.play = Turtle()
        self.back = Turtle()
        self.up_arrow = Turtle()
        self.down_arrow = Turtle()

def main():
    buttons = init_buttons()
    init_variables()
    make_init_game_fn(buttons)(0, 0)
    for i in range(4):
        screen.onkey(make_event_fn(i), str(i))
    screen.onclick(screen_click_event)
    threads = [Thread(target=debug), Thread(target=make_game_loop(buttons))]
    for thread in threads:
        thread.start()
    screen.listen()

    
main()
screen.mainloop()