# lks0221

from pico2d import *

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

def draw():
    clear_canvas()
    map.draw(1,1)

    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

# initialization code
open_canvas(720,430)
map = Map()


running = True;
# game main loop code
while running:
    handle_events()
    draw()

    delay(0.05)
# finalization code
close_canvas()
