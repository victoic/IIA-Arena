from agents import *
import random

class RandomAgent(Agent):
  def program(self, percept) -> str:
    """
    Classe para seu Agente. O programa receberá como percepção a arena inteira,
    uma matriz com None onde não tem nada e um objeto de uma classe Agente onde há
    Essa função deve retornar uma String com uma das seguintes ações:
    - 'left', 'right', 'up', ou 'down' para se mover em uma direção
    - 'attack' para atacar as quatro direções em torno do agente
    """
    actions = ['left', 'right', 'up', 'down', 'attack']
    return random.choice(actions)
