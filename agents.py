class Thing:
  def __init__(self, start_location):
    self.location = start_location

class Agent(Thing):
  def __init__(self, start_location, team):
    super(Agent, self).__init__(start_location)
    self.team = team
    self.hit_points = 10

  def take_hit(self, agent):
    if agent.team != self.team:
      self.hit_points -= 1
      print(f'Agent from team {self.team} takes hit: {self.hit_points}')
      return self
    return None

  def calculate_distance(self, agent):
    x, y = self.location
    ox, oy = agent.location
    distance = ((x - ox)**2 + (y - oy)**2)**(1/2)
    return distance