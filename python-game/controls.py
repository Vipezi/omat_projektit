import sys
import pygame

class Controls:
  ####################################################
  # Task 1: Initialize the values of the dictionary
  # with False
  #
  # keys: "up", "down", "left", "right", 
  #       "w", "a", "s", "d", "space"
  ####################################################
  def __init__(self):
    self.movement = True
    self.keys = {
      ##############  Write your code here  ##############
      "up":False,
      "down":False,
      "left":False,
      "w":False,
      "a":False,
      "s":False,
      "d":False,
      #####################################################
      "right":False,
      "space":False
    }

  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
        value = False
        if event.type == pygame.KEYDOWN:
          value = True
        
        if event.key == pygame.K_RIGHT:
          self.keys["right"] = value
        elif event.key == pygame.K_LEFT:
          self.keys["left"] = value
        elif event.key == pygame.K_UP:
          self.keys["up"] = value
        elif event.key == pygame.K_DOWN:
          self.keys["down"] = value
        elif event.key == pygame.K_SPACE:
          self.keys["space"] = value
        elif event.key == pygame.K_w:
          self.keys["w"] = value
        elif event.key == pygame.K_a:
          self.keys["a"] = value
        elif event.key == pygame.K_s:
          self.keys["s"] = value
        elif event.key == pygame.K_d:
          self.keys["d"] = value