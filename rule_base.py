from experta import *

class AgentFact(Fact):
  """
  Informação à respeito do próprio agente.
  Fique avontade para adicionar novas informações a serem extraídas
  dos agentes.    
  """
  def get_information(self, self_agent, agent):
    self['distance'], self['x_direction'], self['y_direction'] = self_agent.calculate_distance(agent)
    self['team'] = agent.team
    self['hit_points'] = agent.hit_points
    self['id'] = agent.id

class AgentAct(KnowledgeEngine):
  enemy_team = 'b'
  '''
  Classe para o Motor de Inferência e Memória de Trabalho
  Apresenta exemplo base de regras para mover e atacar, mas 
  pode ser bem melhor!
  '''
  #@Rule(AgentFact(distance=TEST(lambda x: x>1), y_direction=L(-1), team=L(enemy_team)))
  @Rule(AgentFact(distance=P(lambda distance: distance > 0), y_direction=-1, team=L(enemy_team)))
  def go_left(self):
    self.action = 'left'
  
  @Rule(AgentFact(distance=P(lambda distance: distance > 0), y_direction=1, team=L(enemy_team)))
  def go_right(self):
    self.action = 'right'

  @Rule(AgentFact(distance=P(lambda distance: distance > 0), x_direction=-1, team=L(enemy_team)))
  def go_up(self):
    self.action = 'up'

  @Rule(AgentFact(distance=P(lambda distance: distance > 0), x_direction=1, team=L(enemy_team)))
  def go_down(self):
    self.action = 'down'

  @Rule(
    AgentFact(distance=P(lambda distance: distance == 1), x_direction=0, team=L(enemy_team))
    | AgentFact(distance=P(lambda distance: distance == 1), y_direction=0, team=L(enemy_team))
    )
  def attack(self):
    self.action = 'attack'