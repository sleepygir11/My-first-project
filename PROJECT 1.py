import pygame as pg
import random
import sys
pg.init()
W = 800
H = 800
g = random.randrange(0,600)
q = random.randrange(0,600)
win = pg.display.set_mode((W,H))
G = random.choices(range(0,256), k = 3)
img = pg.image.load("JOE.jpg")
count = 0
x = 0
y = 0
while True:
   for i in pg.event.get():
      if i.type == pg.QUIT:
         print("CONGRATULATIONS!!! YOUR SCORE IS", count)
         exit()
      keys = pg.key.get_pressed()
      if keys[pg.K_LEFT]:
         x -= 50
      elif keys[pg.K_RIGHT]:
         x += 50
      elif keys[pg.K_UP]:
         y -= 50
      elif keys[pg.K_DOWN]:
         y += 50
   win.fill((G))
   pg.display.set_caption('JOE PANCAKES')
# Параметры круга
   def get_random_position(circle_radius):
      x = random.randint(circle_radius, W - circle_radius)
      y = random.randint(circle_radius, H - circle_radius)
      return(x,y)

   circle_pos = get_random_position(50)
   circle_radius = 50
   circle_visible = True
# Параметры объекта (например, прямоугольник)
   img_pos = img.get_rect()
   img_size = img.get_size()
   count = 0
   pg.draw.circle(win,(0,0,0), circle_pos, circle_radius)
   if circle_visible:
      img_center = (img_pos[0] + img_size[0] // 2, img_pos[1] + img_size[1] // 2)
      distance = ((circle_pos[0] - img_center[0]) ** 2 + (circle_pos[1] - img_center[1]) ** 2) ** 0.5

   if distance < circle_radius + (img_size[0] // 2) and circle_visible:
      circle_visible = False
      count += 1

   elif circle_visible:
      pg.draw.circle(win,(0,0,0), circle_pos, circle_radius)


   win.blit(img,(x,y))
   pg.display.update()
   pg.time.delay(100)
   # if distance_squared < (my_circle.radius ** 2) and my_circle.visible:
   #    my_circle.visible = False 


