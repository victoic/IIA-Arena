from agents import *
import random

class RandomAgent(Agent):
  def program(self, percept) -> str:
    """
    Classe de agente que toma ações aleatoriamente. Para testes contra
    sua implementação de Agente Inteligente.
    Parâmetros:
    - percept: ndArray, array do tamanho da arena com todas as informações
    do mundo.
    
    Retorno:
    - action: str, ação a ser tomada no próximo passo. Pode receber os
    valores: 'left', 'right', 'up', ou 'down' para se mover em uma di-
    reção ou 'attack' para atacar as quatro direções em torno do agen-
    te.
    """
    actions = ['left', 'right', 'up', 'down', 'attack']
    action = random.choice(actions)
    return action
