from pygame import *
score = 0
inc = 1
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.player_h = player_h
        self.player_w = player_w
        self.image = transform.scale(image.load(player_image), (player_w, player_h))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    pass
class Button(GameSprite):
    pass  


window = display.set_mode((700, 500))

hero = Player('g.jpg', 250, 150, 150, 200, 200)

magaz = Button('x2.png', 650, 0, 150, 50, 50)
magaz2 = Button('x3.png', 650, 50, 200, 50, 50)
magaz3 = Button('x5.png', 650, 100, 250, 50, 50)
magaz4 = Button('x50.jpg', 650, 150, 300, 50, 50)
magaz5 = Button('100.jpg', 650, 200, 350, 50, 50)
magaz6 = Button('saturn.png', 650, 250, 400, 50, 50)
magaz7 = Button('x500.webp', 650, 300, 450, 50 ,50)


background = transform.scale(image.load('c.jpg'), (700, 500))
font.init()
font2 = font.Font(None, 70)
font3 = font.Font(None,70)
font4 = font.Font(None, 70)
font5 = font.Font(None, 70)
font6 = font.Font(None,70)
font7 = font.Font(None,70)
font8 = font.Font(None, 60)
font9 = font.Font(None, 60)

game = True
while game:
    text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
    text2 = font3.render('20', 1, (255, 255, 255))
    text3 = font4.render('30', 1, (255, 255, 255))
    text4 = font5.render('50', 1, (255, 255, 255))
    text5 = font6.render('500', 1, (255, 255, 255))
    text6 = font7.render('1000', 1, (255, 255, 255))
    text7 = font8.render('1000000', 1, (255, 255, 255))
    text8 = font9.render('10000000', 1, (255, 255, 255))
    window.blit(background, (0, 0))
    hero.reset()
    magaz.reset()
    magaz2.reset()
    magaz3.reset()
    magaz4.reset()
    magaz5.reset()
    magaz6.reset()
    magaz7.reset()
    window.blit(text, (10, 20))
    window.blit(text2, (580, 0))
    window.blit(text3, (580, 50))
    window.blit(text4, (580, 100))
    window.blit(text5, (560, 150))
    window.blit(text6, (540, 200))
    window.blit(text7, (520, 200))
    window.blit(text8, (450, 300))
for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if e.pos[0] >= 290 and e.pos[0] <= 410: 
                    if e.pos[1] >= 190 and e.pos[1] <= 310:
                        score += inc
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 0 and e.pos[1] <= 50:
                        if score - 20 >= 0:
                            score -= 20
                            inc+=1
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 50 and e.pos[1] <= 100:
                        if score - 30 >= 0:
                            score -= 30
                            inc+=2
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 100 and e.pos[1] <= 150:
                        if score - 50 >= 0:
                            score -= 50
                            inc+=5
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 150 and e.pos[1] <= 200:
                        if score - 500 >= 0:
                            score -= 500
                            inc+=50
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 200 and e.pos[1] <= 250:
                        if score - 1000 >= 0:
                            score -= 10000
                            inc+=100
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 250 and e.pos[1] <= 300:
                        if score - 1000000 >= 0:
                            score -= 10000000
                            inc+=1000
                            hero.image = transform.scale(image.load('st.jpg'), (hero.player_w, hero.player_h))
                if e.pos[0] >= 650 and e.pos[0] <= 700:
                    if e.pos[1] >= 300 and e.pos[1] <= 350:
                        if score - 500000000  >= 0:
                            score -= 500000000
                            inc+=500


    display.update()
