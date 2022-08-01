import pgzrun

WIDTH = 600
HEIGHT = 600

player = Actor("alien")
enemy = Actor("enemy", pos=(300,300))

music.play('house_lo')

def draw():
    screen.clear()
    screen.blit('background',(0,0))
    player.draw()
    enemy.draw()
    screen.draw.text("My game", (250,0), color='red')

# player movement
def player_control():
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

# limit check
def player_limit():
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

def enemy_chase_logic():
    if enemy.x < player.x:
        enemy.x += 1
    if enemy.x > player.x:
        enemy.x -= 1
    if enemy.y < player.y:
        enemy.y += 1
    if enemy.y > player.y:
        enemy.y -= 1
    if enemy.colliderect(player):
        sounds.secosmic_lo.play()
        player.image = 'splat'
    
def player_control():
    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

def update():
    player_limit()
    enemy_chase_logic()
    player_control()

pgzrun.go()