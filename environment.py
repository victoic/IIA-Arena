import numpy as np
#from agents import *
from my_agent import *
import os

class Environment():
  def __init__(self, size):
    assert len(size) == 2
    self.size = size
    self.arena = np.ndarray(size, dtype=Thing)

  def add_thing(self, thing: Thing, location: tuple):
    if self.arena[location] is None:
      self.arena[location] = thing
      return True
    return False

  def remove_thing(self, thing: Thing):
    for i in range(self.arena.shape[0]):
      for j in range(self.arena.shape[1]):
        if thing == self.arena[i,j]:
          self.arena[i,j] = None

  def percept(self, agent):
    return self.arena

  def execute_action(self, agent, action):
    if action == 'left':
      x,y = agent.location
      new_y = y-1
      if new_y > 0 and self.arena[x,new_y] is None:
        self.arena[agent.location] = None
        self.arena[x,new_y] = agent
        self.arena[x,new_y].location = (x,new_y)
    
    elif action == 'right':
      x,y = agent.location
      new_y = y+1
      if new_y < self.size[1]-1 and self.arena[x,new_y] is None:
        self.arena[agent.location] = None
        self.arena[x,new_y] = agent
        self.arena[x,new_y].location = (x,new_y)

    if action == 'up':
      x,y = agent.location
      new_x = x-1
      if new_x > 0 and self.arena[new_x,y] is None:
        self.arena[agent.location] = None
        self.arena[new_x,y] = agent
        self.arena[new_x,y].location = (new_x,y)

    elif action == 'down':
      x,y = agent.location
      new_x = x+1
      if new_x < self.size[0]-1 and self.arena[new_x,y] is None:
        self.arena[agent.location] = None
        self.arena[new_x,y] = agent
        self.arena[new_x,y].location = (new_x,y)

    elif action == 'attack':
      x,y = agent.location
      top = (x-1, y)
      bot = (x+1, y)
      lft = (x, y-1)
      rgt = (x, y+1)
      rivals = []
      if top[0] > 0 and self.arena[top] != None:
        rivals.append(self.arena[top].take_hit(agent))
      if bot[0] < self.size[0]-1 and self.arena[bot] != None:
        rivals.append(self.arena[bot].take_hit(agent))
      if lft[1] > 0 and self.arena[lft] != None:
        rivals.append(self.arena[lft].take_hit(agent))
      if rgt[1] < self.size[1]-1 and self.arena[rgt] != None:
        rivals.append(self.arena[rgt].take_hit(agent))

  def get_victorious(self):
    team_a = 0
    team_b = 0
    for i in range(self.arena.shape[0]):
      for j in range(self.arena.shape[1]): 
        if self.arena[i,j] != None:
          if self.arena[i,j].team == 'a':
            team_a+=self.arena[i,j].hit_points
          else:
            team_b+=self.arena[i,j].hit_points
    return team_a, team_b

  def print_environment(self, actions):
    arena_print = ''
    for i in range(self.arena.shape[0]):
      for j in range(self.arena.shape[1]):
        if self.arena[i,j] is None:
          arena_print+='-'
        else:
          arena_print+=self.arena[i,j].team
      arena_print+='\n'
    print(arena_print+actions)
    os.system('cls')
    return arena_print+actions

  def step(self, time=1):
    copy_arena = self.arena.copy()
    printed = ''
    for i in range(time):
      actions = '\n'
      for i in range(self.arena.shape[0]):
        for j in range(self.arena.shape[1]):
          if copy_arena[i,j] is not None:
            agent = copy_arena[i,j]
            action = agent.program(self.percept(agent))
            actions = actions + f"agent from {agent.team} at {agent.location} uses {action}\n"
            self.execute_action(copy_arena[i,j], action)
      for i in range(self.arena.shape[0]):
        for j in range(self.arena.shape[1]):
          if self.arena[i,j] is not None and self.arena[i,j].hit_points <= 0:
            self.remove_thing(self.arena[i,j])
      printed = self.print_environment(actions)
    return printed