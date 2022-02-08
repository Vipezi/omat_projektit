import random
from drawable import Drawable

class NPC(Drawable):
  def __init_screen__():
    pass

  def __init__(self, screen, name, x_0, y_0, scale=2, transparent=True):
    self.speed = 2
    super().__init__(screen,name,x_0,y_0,scale,transparent, category="sprites")
    
  def update(self):
    self.update_position()
    self.update_movement()
    self.move()
    self.draw()

  # Task X: Program the movement
  def update_movement(self):
    self.moving_up    = random.random() > 0.95
    self.moving_down  = random.random() > 0.95
    self.moving_left  = random.random() > 0.95
    self.moving_right = random.random() > 0.95

  # Task X: Add run
  def move(self):
    speed = self.speed
    if self.moving_left:
      self.rect.centerx -= speed
    if self.moving_right:
      self.rect.centerx += speed
    if self.moving_up:
      self.rect.centery -= speed
    if self.moving_down:
      self.rect.centery += speed
      
