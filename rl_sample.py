import random 
from typing import List, Tuple 

class VirtualEnvironment:
	def __init__(self, steps_req_to_complete=2) -> None:
		self._total_applicable_steps = steps_req_to_complete

	def get_observations(self) -> List:
		return [0.0, 0.0, 0.0]

	def get_actions(self) -> Tuple:
		return (0,1)

	def is_done(self) -> bool:
		return self._total_applicable_steps == 0

	def reward_system(self, action: int = None) -> float:
		if action not in self.get_actions():
			raise Exception('Action is not permitted')
		self._total_applicable_steps -= 1
		if action == 0:
			negative_reward = float(random.randint(-20,0))
			return negative_reward
		if action == 1:
			positive_reward = float(random.randint(1,20))
			return positive_reward

class Agent:
	def __init__(self) -> None:
		self._total_reward = 0
		self._number_of_step_performed = 0

	def step(self, env: VirtualEnvironment) -> int:
		current_obs = env.get_observations()
		print("Observations", current_obs)
		get_applicable_actions = env.get_actions()
		deciside_action = random.choice(get_applicable_actions)
		earn_reward = env.reward_system(deciside_action)
		self._total_reward+=earn_reward
		self._number_of_step_performed+=1


DummyEnviron = VirtualEnvironment(100)
MaxDoom = Agent()

while not DummyEnviron.is_done():
	MaxDoom.step(DummyEnviron)
	print("No of Step: ", MaxDoom._number_of_step_performed)
	print("Earned Reward: ", MaxDoom._total_reward)