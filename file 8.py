import pygame as pg
import random
pg.init()
win = pg.display.set_mode((800,800))
W = 800
H = 800
def load_image(name):
   img = pg.image.load(name)
   img = img.convert()
   colorkey = img.get_at((0,0))
   img.set_colorkey(colorkey)
   return img
all_sprites = pg.sprite.Group()

class Inginirium(pg.sprite.Sprite):

   def __init__(self, *group):
      super().__init__(*group)
      self.image = load_image("JOE.jpg")
      self.image = pg.transform.scale(self.image,(100,100))
      self.rect = self.image.get_rect()
      self.rect.x = random.randrange(W)
      self.rect.y = random.randrange(H)
   
   def update(self):
      self.rect = self.rect.move(random.randrange(3) - 1,
                                 random.randrange(3)-1)
   
   all_sprites = pg.sprite.Group()

for i in range(50):
   Inginirium(all_sprites)

while True:
   for i in pg.event.get():
      if i.type == pg.QUIT:
         exit()
   all_sprites.update()

   win.fill((255,255,255))
   all_sprites.draw(win)
   pg.display.update()
   
