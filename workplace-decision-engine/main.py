from env import WorkplaceEnv
from models import Action

env = WorkplaceEnv()

obs = env.reset()
print("Initial Observation:", obs)

action = Action(action_type="complete", task_id=1)

obs, reward, done, _ = env.step(action)

print("After Action:")
print("Observation:", obs)
print("Reward:", reward)
print("Done:", done)