
# fill here
from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

mode_1 = True
mode_2 = False

x = 0
y = 90
gak = 0
d = 0.001

while (True):
    if mode_1 == True:
        if y == 90 and x <800:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 2
            delay(d)
        elif y<600 and x==800:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 2
            delay(d)
        elif y==600 and x>0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 2
            delay(d)
        elif x==0 and y>90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 2
            delay(d)
            if x==0 and y ==90:
                mode_1 = False
                mode_2 = True
    elif mode_2 == True:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        gak = gak + 10
        radian = math.radians(gak)
        x = 400 + 250 * math.cos(radian) 
        y = 300 - 250 * math.sin(radian) 
        delay(0.1)
        if gak > 360:
            x = 0
            y = 90
            mode_1 = True
            mode_2 = False

    #update_canvas()

close_canvas()

