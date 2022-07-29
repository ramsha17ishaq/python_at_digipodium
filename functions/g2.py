import pgzrun

HEIGHT = 500
WIDTH = 500

box = Rect(50,50,100,100)
box2 = Rect(350,50,100,50)
box3 = Rect((400,400), (50,50))
b4 = Rect((200,450),(100,100))

def draw():
    screen.fill('white')
    screen.draw.rect(box,'red')
    screen.draw.filled_rect(box2,'pink')
    screen.draw.filled_rect(box3,'green')
    screen.draw.filled_rect(b4,'violet')
    screen.draw.text('These are rectangles',(150,250),color = 'blue')

pgzrun.go()