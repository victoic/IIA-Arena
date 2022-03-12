class Thing:
  def __init__(self, start_location: tuple, id: int):
    assert len(start_location) == 2
    self.location = start_location
    self.id = id

class Agent(Thing):
  def __init__(self, start_location: tuple, id:int, team: str):
    '''
    Inicializador do Agent.
    
    Parâmetros:
    - start_location: tupla, com coordenadas de localização (x,y)
    do agente.
    - team: str, um único caractere que define o time do agente.
    '''
    assert len(team) == 1
    super(Agent, self).__init__(start_location, id)
    self.team = team
    self.hit_points = 10

  def take_hit(self, agent):
    '''
    Subtrai 1 da sua própria vida, caso o agente atacante seja de
    um time diferente do seu.
    
    Parâmetros:
    - agent: Agent, o objeto do agente atacante, derivado de Thing
    
    Retorno:
    - objeto, self caso sofra dano, None caso não sofra
    '''
    if agent.team != self.team:
      self.hit_points -= 1
      print(f'Agent from team {self.team} takes hit: {self.hit_points}')
      return self
    return None

  def calculate_distance(self, agent: Thing):
    '''
    Cálcula distância entre si e um outro agente, além da direção.
    
    Parâmetros:
    - agent: Thing, o objeto a ser comparado
    
    Retorno:
    - distance: float, distância entre coordenadas dos dois agentes
    - x_direction: int, direção no eixo x, pondendo assumir os valo-
    res 0 caso ambos estejam no mesmo eixo, 1 se 'agent' está à dire-
    ita e -1 se 'agent' está à esquerda
    - y_direction: int, direção no eixo y, pondendo assumir os valo-
    res 0 caso ambos estejam no mesmo eixo, 1 se 'agent' está abaixo
    e -1 se 'agent' está acima
    '''
    x, y = self.location
    ox, oy = agent.location
    distance = ((x - ox)**2 + (y - oy)**2)**(1/2)
    x_direction = 0 if x == ox else 1 if x < ox else -1
    y_direction = 0 if y == oy else 1 if y < oy else -1
    return distance, x_direction, y_direction