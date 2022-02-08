import pygame
import settings
import resources.levels as lvl
from level import Level

#######################################################
# Task 2: Implement the constructor
# Objective: Assign the parameters as attributes
#
# Add the following attributes to the Class
#  * x,y: Initial position of the elements in the screen
#  * width: Screen width IN settings.py
#  * height: Screen height IN settings.py
#  * background_color: Color of empty screen IN settings.py
#
##########################################################################
class Screen:
  def __init__(self, x=0, y=0):
    ##############  Write your code here  ##############
    self.x = x
    self.y = y
    self.width = settings.screen_width
    self.height = settings.screen_height
    self.background_color = settings.background_color
    ####################################################
    self.window = pygame.display.set_mode((self.width, self.height))
    self.current_level = None
    pygame.display.set_caption(settings.title)

  def change_level(self,level_name, x=None, y=None):
    self.fade_screen()
    if x == None:
      x = lvl.levels[level_name]["x0"]
    if y == None:
      y = lvl.levels[level_name]["y0"]
    self.move_center(x,y)
    self.current_level = Level(level_name, self)

  def get_current_level_name(self):
    return self.current_level.name

  def fade_screen(self):
    fade = pygame.Surface((self.width, self.height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
      fade.set_alpha(alpha)
      self.update()
      self.window.blit(fade, (0,0))
      pygame.display.update()
      pygame.time.delay(1)

  def move(self,dx,dy):
    self.x += dx
    self.y += dy
  
  def move_center(self, x, y):
    self.x = x - self.width / 2
    self.y = y - self.height / 2

  def get_relative_coordinates(self):
    r_x = self.x
    r_y = self.y
    return r_x, r_y

  def get_center_coordinates(self):
    x = self.x + self.width / 2
    y = self.y + self.height / 2
    return x,y

  def get_block(self,x,y):
    block = self.current_level.get_block(x,y)
    return block

  def is_collision(self,x,y):
    block = self.get_block(x,y)
    elem = self.current_level.get_element_in(x,y)
    return block.obstacle or (elem != None and elem.obstacle)

  def update(self):
    self.window.fill(self.background_color)
    if self.current_level != None:
      self.current_level.update()