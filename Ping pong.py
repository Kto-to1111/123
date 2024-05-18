from pygame import  *

window = display.set_mode((900, 600))
display.set_caption('Ping_pong')



class GameSprite(sprite.Sprite):

    def __init__(self, player_image,player_x, player_y,player_speed,width,height):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(width , height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image,self.rect)



class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
                self.rect.y += self.speed

bask = (200,255,255)
win_widght = 600
win_height = 500
window = display.set_mode((win_widght,win_height))
window.fill(bask)

game = True
finish = False
clock = time.Clock()
FPS = 60

rasket1 = Player('nagess.jpeg',30,200,4,100,150)
rasket2 = Player('catnagess.jpg',520,200,4,100,150)
ball = GameSprite('ball (1).png',200,200,4,50,50)


font.init()
font = font.Font(None,35)
lose1 = font.render("Player 1 LOSE!!!!",True,(180,0,0))
lose2 = font.render("Player 2 LOSE!!!!",True,(180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(bask)
        rasket1.update_l()
        rasket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rasket1,ball) or sprite.collide_rect(rasket2 , ball):
            speed_x *= -1

        if ball.rect.y > 450 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))


        if ball.rect.x > 550:
            finish = True
            window.blit(lose2,(200,200))



        rasket1.reset()
        rasket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)







