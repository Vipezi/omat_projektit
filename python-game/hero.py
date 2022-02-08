import pygame
from pygame import Surface
import settings
from drawable import Drawable

class Hero(Drawable):
  ####################################################################
  # Task 5.1: Add the following attributes in the constructor
  #  * controls: Controls object
  #  * speed: 4 (Quantity of pixels per frame)
  #  * index_animation = 0 (Starts in static position)
  #  * direction = "down"  (Starts looking down)
  # Task 5.2: Call the __init__ function of the Parent Class (Drawable)  -> DONE in Line 23
  #####################################################################

  def __init__(self, screen, controls, scale=2, hero_name="hero"):
    ############      Write your code here      ############
    self.controls = None
    self.speed = None
    self.index_animation = None
    self.direction = None
    ########################################################
    super().__init__(screen, hero_name, 0, 0, category="sprites", scale=scale,transparent=True)
    self.rect.centerx = self.screen.window.get_rect().centerx
    self.rect.centery = self.screen.window.get_rect().centery
    self.init_images(scale)

  def init_images(self, scale):
    self.images = {}
    for direction in ["up","down","right","left"]:
      images = []
      for index in range(settings.frames_animation_characters):
        resource_folder = settings.resource_folder
        path = resource_folder + "/sprites/" + self.name + "/" + direction + str(index) + ".bmp"
        image, rect =  self.create_image(path, scale, transparent=True)
        images.append(image)
      self.images[direction] = images

  def is_moving(self):
    return self.moving_left or \
          self.moving_right or \
          self.moving_up or \
          self.moving_down

  # Overriding Method to avoid unexpected behaviors
  def update_position(self):
    pass


  def update_animation(self):
    freq = settings.speed_animation_walk
    if self.is_moving():
      self.index_animation += freq
      if self.index_animation >= settings.frames_animation_characters:
        self.index_animation = 0
      index = int(self.index_animation)
      self.image = self.images[self.direction][index]
    else:
      self.image = self.images[self.direction][0]

  def update(self):
    self.update_movement()
    self.update_direction()
    self.update_animation()
    self.block_movement()
    self.move()
    self.draw()
  
  ##############################################
  # Task 6: Add movement with arrows and WASD  #
  ##############################################
  def update_movement(self):
    keys = self.controls.keys
    #######     Write your code here     #######
    self.moving_up    = keys["up"] or keys["w"]
    self.moving_down  = False
    self.moving_left  = False
    self.moving_right = False
    ############################################

  #############################################
  # Task 7: Update the attribute direction    #
  #         depending on the values of:       #
  #  self.moving_up, self.moving_down         #
  #  self.moving_left, self.moving_right      #
  #############################################
  def update_direction(self):
    #######     Write your code here     #######
    if self.moving_up:
      self.direction = "down"
    elif self.moving_down:
      self.direction = "down"
    elif self.moving_right:
      self.direction = "down"
    elif self.moving_left:
      self.direction = "down"
    ############################################

  def move(self):
    dx , dy = 0 , 0
    speed = self.speed
    if self.moving_left:
      dx = -speed
    if self.moving_right:
      dx = +speed
    if self.moving_up:
      dy = -speed
    if self.moving_down:
      dy = +speed
    self.screen.move(dx,dy)

  ###########################################
  # Task 8: Detect obstacle in the sides
  # Detection Points:
  # * Left:  (x0,y) (x0,y1)
  # * Right: (x1,y) (x1,y1) 
  # * Up:    (x,y0)
  # * Down:  (x,ybottom)
  ###########################################
  def block_movement(self):
    scr = self.screen
    x,y = self.screen.get_center_coordinates()
    ###########        Write your code Here       ############
    x0 = None
    x1 = x + self.width / 2 + self.speed
    y0 = None
    y1 = None
    ybottom = None

    # Hint: 
    #   scr.is_collision(xa,ya) or scr.is_collision(xb,yb)
    obstacle_in_left = False or False
    obstacle_in_right = False or False
    obstacle_in_up = False or False
    obstacle_in_down = False or False
    ##########################################################

    if obstacle_in_left:
      self.moving_left = False
    if obstacle_in_right:
      self.moving_right = False
    if obstacle_in_up:
      self.moving_up = False
    if obstacle_in_down:
      self.moving_down = False
