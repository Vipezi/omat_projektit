import pygame
import settings

##########################################################################
# Task 4:    Implement the constructor
# Objective:  Assign the parameters as attributes
#
# Add the following attributes to the Class
#  * screen: Object Screen to paint the drawable
#  * name:   Name of the sprite
#  * x:      Position in x
#  * y:      Position in y
#  * obstacle: True if the object is an obstacle
#
# The other parameters are not part of the class
#  * transparent: Creates transparency with color in (0,0) as background
#  * scale: Resizes the image
#  * category: Obtains the image from the folder of the category
##########################################################################
class Drawable():
  def __init__(self, screen, name, x, y, obstacle=False ,transparent=False, scale=2, category="blocks"):
    ##############  Write your code here  ##############
    self.name = name
    #####################################################
    self.scale = scale
    resource_folder = settings.resource_folder
    path = resource_folder + "/" + category + "/" + name + ".bmp"
    image, rect = self.create_image(path, scale, transparent)
    self.set_image(image)
    self.rect = rect

  def set_image(self,image):
    self.width = image.get_width()
    self.height = image.get_height()
    self.image = image

  def create_image(self, path, scale=1, transparent=False):
    image = pygame.image.load(path)
    width = image.get_width() * scale
    height = image.get_height() * scale
    dims = (width, height)
    image = pygame.transform.scale(image,dims)
    if transparent:
      first_pixel = image.get_at((0,0))
      image.set_colorkey(first_pixel)
    rect = image.get_rect()
    return image, rect

  def update_position(self):
    relative_x, relative_y = self.screen.get_relative_coordinates()
    self.rect.centerx = self.x - relative_x
    self.rect.centery = self.y - relative_y

  def update(self):
    self.update_position()
    self.draw()

  def draw(self):
    self.screen.window.blit(self.image, self.rect)

  ############################################################
  # Optional Task X: Return True if the given point in (x,y) #
  #         collides with the image of the drawable          #
  ############################################################
  def collide_point(self,x,y):
    ##########    Write your code here    #############
    x0 = self.x - self.width // 2
    x1 = self.x + self.width // 2
    y0 = self.y - self.height // 2
    y1 = self.y + self.height // 2
    return x in range(x0,x1) and y in range(y0,y1)
    ###################################################

  def __str__(self):
    print(self.rect)
    return self.name