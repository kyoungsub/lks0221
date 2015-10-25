from pico2d import *

import random

# Game object class here
class Map:
    def __init__(self):
        self.bkimage1 = load_image('map/1st_map_block.png')
        self.bkimage2 = load_image('map/2nd_map_block.png')
        self.block1 = load_image('map/1st_map.png')
        self.block2 = load_image('map/2nd_map.png')

    def draw(self,n, battle):
        if n==1:
            self.bkimage1.draw(360,215)
            if battle == 1:
                self.block1.draw(360,215)
        elif n==2:
            self.bkimage2.draw(360,215)
            if battle == 1:
                self.block2.draw(360,215)

class Character:
    def __init__(self):
        self.hero = load_image('charcter/hero_sprites.png')
        self.heroin = load_image('charcter/heroin_sprites.png')
        self.archer = load_image('charcter/archer.png')

        self.x = 645
        self.y = 63
        self.movecount=0
        self.frame = 0
        self.charevent = 7

    def update(self):
        if self.charevent >= 0 and self.charevent<=4:
            self.frame = (self.frame+1)%7
        elif self.charevent >4:
            self.frame = (self.frame+1)%8

    def move_left(self, tilemoved):
        self.charevent = 8
        self.x -=2
        self.y -=1
        self.movecount+=1
        if self.movecount >= 16 * tilemoved:
            #y값 17로 보정
            self.y -= 1*tilemoved
            self.movecount=0

    def move_right(self, tilemoved):
        self.charevent = 5
        self.x +=2
        self.y +=1
        self.movecount+=1
        if self.movecount >= 16*tilemoved:
            #y값 17로 보정
            self.y += 1*tilemoved
            self.movecount =0

    def move_up(self,tilemoved):
        self.charevent = 6
        self.x -=2
        self.y +=1
        self.movecount+=1
        if self.movecount >= 16 * tilemoved:
            #y값 17로 보정
            self.y += 1*tilemoved
            self.movecount=0

    def move_down(self,tilemoved):
        self.charevent = 7
        self.x +=2
        self.y -=1
        self.movecount+=1
        if self.movecount >= 16 * tilemoved:
            #y값 17로 보정
            self.y -= 1*tilemoved
            self.movecount=0

    def draw(self, n):
        if n==1:
            self.hero.clip_draw(self.frame*60,self.charevent*60,60,60,self.x,self.y)
        elif n == 2:
            self.heroin.clip_draw(self.frame*60,self.charevent*60,60,60,self.x+ 32, self.y+ 17)
        elif n == 3:
            self.archer.clip_draw(self.frame*60,self.charevent*60,60,60,self.x -32, self.y - 17)


#define function
def mapselection(n, tile_xpos, tile_ypos):
    global enable_tile
    global selected_tile

    enable_tile = load_image('ui/move_tiles.png')
    selected_tile = load_image('ui/selected_tiles.png')

    if n==1:
        enable_tile.draw(tile_xpos,tile_ypos)
    if n==2:
        selected_tile.draw(tile_xpos,tile_ypos)

def move(turn, tile1,tile2):
    if turn ==1:
        if tile1 > 0:
            mainboy.move_right(tile1)
        elif tile1 < 0:
            mainboy.move_left(-tile1)

        if tile2 > 0:
            mainboy.move_up(tile2)
        elif tile2 < 0:
            mainboy.move_down(-tile2)

    if turn ==2:
        if tile1 > 0:
            maingirl.move_right(tile1)
        elif tile1 < 0:
            maingirl.move_left(-tile1)

        if tile2 > 0:
            maingirl.move_up(tile2)
        elif tile2 < 0:
            maingirl.move_down(-tile2)

    if turn ==3:
        if tile1 > 0:
            subboy.move_right(tile1)
        elif tile1 < 0:
            subboy.move_left(-tile1)

        if tile2 > 0:
            subboy.move_up(tile2)
        elif tile2 < 0:
            subboy.move_down(-tile2)

def turncounter():
    global who_turn
    global movement

    if movement == 0:
        who_turn += 1
        who_turn %= 3
        movement = 7

def draw():
    clear_canvas()
    map.draw(mapswitch,1)

    if who_turn ==1:
        mapselection(1,mainboy.x,mainboy.y- tilesizey/2)
    elif who_turn ==2:
        mapselection(1,maingirl.x + tilesizex/2,maingirl.y)
    elif who_turn ==3:
        mapselection(1,subboy.x - tilesizex/2,subboy.y- tilesizey)
    mainboy.draw(1)
    maingirl.draw(2)
    subboy.draw(3)
    update_canvas()

def animation():
    move(who_turn,tilecount1, tilecount2)

    mainboy.update()
    maingirl.update()
    subboy.update()

def handle_events():
    global mapswitch
    global who_turn
    global keyinput
    global tilecount1,tilecount2

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == SDLK_RIGHT:
                keyinput = KEY_RIGHT
                tilecount1 += 1
            if event.key == SDLK_LEFT:
                keyinput = KEY_LEFT
                tilecount1 -= 1
            if event.key == SDLK_UP:
                keyinput = KEY_UP
                tilecount2 += 1
            if event.key == SDLK_DOWN:
                keyinput = KEY_DOWN
                tilecount2 -= 1

            if event.key == SDLK_1:
                mapswitch=1
            if event.key ==SDLK_2:
                mapswitch=2
            if event.key == SDLK_4:
                who_turn =1
            if event.key == SDLK_5:
                who_turn =2
            if event.key == SDLK_6:
                who_turn =3

# initialization code
open_canvas(720,430)

KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN = 1, 2, 3, 4
tilesizex = 64
tilesizey = 34

tilecount1,tilecount2 = 0, 0
who_turn = 1
movement = 7
keyinput = 0

mapswitch = 1

map = Map()
mainboy = Character()
maingirl = Character()
subboy = Character()


running = True;


# game main loop code
while running:
    turncounter()

    handle_events()
    animation()
    draw()

    delay(0.05)
# finalization code
close_canvas()
