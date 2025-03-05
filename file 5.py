import pygame as pg
import random
pg.init()
W = 500
H = 500
def load_img(name):
   img = pg.image.load(name)
   img = img.convert()
   colorkey = img.get_at((0,0))
   img.set_colorkey(colorkey)
   return img
   
img = load_img("JOE.png")
img = pg.transform.scale(img,(100,100))
all_sprites = pg.sprite.Group()
win = pg.display.set_mode((500,500))
for i in range(100):
   sprite = pg.sprite.Sprite(all_sprites)
   sprite.image = img
   sprite.rect = sprite.image.get_rect()

   sprite.rect.x = random.randrange(W)
   sprite.rect.y = random.randrange(H)
while 1:
   for i in pg.event.get():
      if i.type == pg.QUIT:
         exit()
win.fill(255,255,255)
all_sprites.draw(win)
pg.display.update()
