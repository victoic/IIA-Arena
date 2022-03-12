from environment import *
from my_agent import *
from test_agent import *
import random

def main():
  print("Starting...")
  size = 10
  print(f"Created environment with size {size}")
  env = Environment((size,size))
  team_members = 2
  # Trocar o valor de 'a' para sua classe
  team_dict = {'a': MyAgent, 'b': RandomAgent}
  agents = ['a']*team_members + ['b']*team_members
  ordered_agents = random.sample(agents, len(agents))
  print(f"Agents will be created in this order: {ordered_agents}")
  print(f"Creating agents...")
  id_counter=0
  for team in ordered_agents:
    passed = False
    loct = ()
    while not passed:
      loc = (random.randint(0,size-1), random.randint(0,size-1))
      agent = team_dict[team](loc, id_counter, team)
      passed = env.add_thing(agent, loc)
    id_counter+=1
    print(f"\tAgent added to team {team} at {loc}")
  print(f"Running environment")
  print(env.step(100))
  print(f"Simulation over.")
  hp_team_a, hp_team_b = env.get_victorious()
  victor_team = 'A Wins' if hp_team_a > hp_team_b else 'B Wins'
  victor_team = 'Draw' if hp_team_b == hp_team_a else victor_team
  print(f'{victor_team} - HP-a: {hp_team_a} | HP-b: {hp_team_b}')


if __name__ == '__main__':
  main()