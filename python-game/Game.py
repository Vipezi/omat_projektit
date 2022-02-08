import pygame

import settings
from screen import Screen
from drawable import Drawable
from controls import Controls
from hero import Hero

from npc import NPC

from level import Level
import resources.levels as lvl

####################################################################
# Task 9: Program the Logic of moving between different levels
#  * level_name: Name of the current Level
#  * x,y: Current position of the hero
# 
# For each transition in the current level, check if x and y is between
# the x0,x1 and y0,y1 specified
#
# The transitions are defined in a dictionary called "transitions" 
# located in resources/levels.py
# 
# If the player is located in a transition area, return a tuple with
# three elements: the name of the new level, newx and newy
# Otherwise return just False
#####################################################################
def is_transition(level_name,x,y):
  if level_name not in lvl.transitions:
    return False
  for tr in lvl.transitions[level_name]:
    x0, x1, y0, y1 = tr["x0"], tr["x1"], tr["y0"], tr["y1"]
    #############    Insert your code here    ################
    if False: # Check if x and y is between x0,x1 and y0,y1
      newx = None
      newy = None
      new_level = None
      return None, None, None
    ##########################################################
  return False

def run_game():
  pygame.init()
  fps = settings.fps
  screen = Screen()
  screen.change_level(settings.first_level)
  clock = pygame.time.Clock()
  controls = Controls()
  #hero = Hero(screen, controls, scale=settings.scale)
  while True:
    x, y = screen.get_center_coordinates()
    print(x,y)
    is_trans = is_transition(screen.get_current_level_name(),x,y)
    if is_trans != False:
      new_level, newx, newy = is_trans
      screen.change_level(new_level, newx, newy)
    controls.update()
    screen.update()
    #hero.update()
    pygame.display.flip()
    clock.tick(fps)

run_game()
