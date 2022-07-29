import pgzrun

HEIGHT = 500
WIDTH = 500

p = Rect((40,40),(50,50))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(p,'blue')

def update():
    control_player()



def control_player():
    if keyboard.RIGHT:
        if p.right < WIDTH:
            p.x += 2
        else:
            sounds.punch.play()
    if keyboard.LEFT:
        if p.left > 0:
            p.x += -2
        else:
            sounds.punch.play()

    if keyboard.UP:
        p.y += -2
    if keyboard.DOWN:
        p.y += 2
    
pgzrun.go()