import pygame as pg
pg.init()
sc = pg.display.set_mode((800,800))
y = 0
x = 0
img = pg.image.load('JOE.png')
while 1:
   for i in pg.event.get():
      if i.type == pg.QUIT:
         exit()
   keys = pg.key.get_pressed()
   if keys[pg.K_LEFT]:
      x -= 50
   if keys[pg.K_RIGHT]:
      x += 50
   if keys[pg.K_DOWN]:
      y += 50
   if keys[pg.K_UP]:
      y -= 50  
   
   sc.fill((0,0,0))
   sc.blit(img, (x,y))
   pg.display.update()
   pg.time.delay(30)