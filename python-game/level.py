import resources.blocks as blk
import resources.levels as lvl
from drawable import Drawable
import settings

##########################################################################
# Task 3:    Implement the constructor
# Objective:  Assign the parameters as attributes
#
# Add the following attributes to the Class
#  * scale:  scale of images IN settings.py
#  * name:   Level Name
#  * screen: Object Screen to paint the map
#  * size_blocks: Size of the blocks IN settings.py
#  * map: List of lists defined IN resources/levels.py
#
##########################################################################
class Level:
  def __init__(self, level_name, screen):
    ##########   Write your code here   ###########
    self.scale = None
    self.name = None
    self.screen = None
    self.size_blocks = None
    self.mapWithWrongName = lvl.levels[level_name]["map"]
    ###############################################
    self.init_map()
    self.init_elements()

  def update(self):
    self.draw()

  def draw(self):
    for line in self.submap:
      for block in line:
        block.update()
    for element in self.elements:
      element.update()

  def init_map(self):
    self.submap = []
    t_y = 0
    for line in self.map:
      line_sprites = []
      t_x = 0
      for block in line:
        sprite_name = blk.names[block]["name"]
        obstacle = False
        if "obstacle" in blk.names[block] and blk.names[block]["obstacle"] == True:
          obstacle = True
        sprite_name = blk.names[block]["name"]
        x =  t_x * self.size_blocks * 2
        y =  t_y * self.size_blocks * 2
        sprite = Drawable(self.screen, sprite_name, x, y, obstacle=obstacle, scale=self.scale)
        t_x += 1
        line_sprites.append(sprite)
      self.submap.append(line_sprites)
      t_y += 1

  def init_elements(self):
    self.elements = []
    if "elements" in lvl.levels[self.name]:
      for element in lvl.levels[self.name]["elements"]:
        sprite_name = element["name"]
        x = element["x"]
        y = element["y"]
        category = element["category"]
        obstacle = False
        if "obstacle" in element and element["obstacle"] == True:
          obstacle = True
        transparent = False
        if "transparent" in element and element["transparent"] == True:
          transparent = True
        sprite = Drawable(self.screen, sprite_name, x, y, obstacle=obstacle, scale=self.scale, category=category, transparent=transparent)
        self.elements.append(sprite)

  def get_block(self,x,y):
    size = self.size_blocks
    stride = size / 2
    i_x = int((x + stride) // (size*self.scale))
    i_y = int((y + stride) // (size*self.scale))
    block = self.submap[i_y][i_x]
    return block

  def get_element_in(self,x,y):
    for elem in self.elements:
      if elem.collide_point(x,y):
        return elem
    return None
  