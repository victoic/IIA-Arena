from agents import *
from rule_base import *

class MyAgent(Agent):
  def __init__(self, *args):
    super(MyAgent, self).__init__(*args)
    self.knowledge_engine = AgentAct()
    self.knowledge_engine.enemy_team = 'a' if self.team == 'b' else 'b'
    self.facts = {}

  def update_knowledge_base(self, arena):
    for row in arena:
      for thing in row:
        if thing is not None:
          fact = AgentFact()
          fact.get_information(self, thing)
          self.knowledge_engine.declare(fact)
          self.facts[fact['id']] = fact

  def program(self, percept) -> str:
    """
    Classe para seu Agente. O programa receberá como percepção a arena inteira,
    uma matriz com None onde não tem nada e um objeto de uma classe Agente onde há

    As regras são criadas por meio do pacote experta, use o exemplo em
    [https://github.com/nilp0inter/experta] para se guiar.

    Para testar, mude o valor da chave 'a' de team_dict no arquivo main.py para a
    sua classe e execute o arquivo main.py.
    
    Parâmetros:
    - percept: ndArray, array do tamanho da arena com todas as informações
    do mundo.
    
    Retorno:
    - action: str, ação a ser tomada no próximo passo. Pode receber os
    valores: 'left', 'right', 'up', ou 'down' para se mover em uma di-
    reção ou 'attack' para atacar as quatro direções em torno do agen-
    te.
    """
    self.knowledge_engine.reset()
    self.update_knowledge_base(percept)
    print(self.knowledge_engine.facts)
    self.knowledge_engine.run()
    action = self.knowledge_engine.action
    print(action)
    return action