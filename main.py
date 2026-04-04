from env import WorkplaceEnv
from models import Action

env = WorkplaceEnv()

obs = env.reset()
print("\n=== INITIAL TASKS ===")
for task in obs.tasks:
    print(task)

# STEP 1: Handle HIGH priority
print("\n--- Handling HIGH priority task ---")
obs, reward, done, info = env.step(Action(action_type="complete", task_id=1))
print("Reward:", reward)
print("Score:", info["score"])

# STEP 2: Handle MEDIUM priority
print("\n--- Handling MEDIUM priority task ---")
obs, reward, done, info = env.step(Action(action_type="schedule", task_id=2))
print("Reward:", reward)
print("Score:", info["score"])

# STEP 3: Handle LOW priority
print("\n--- Handling LOW priority task ---")
obs, reward, done, info = env.step(Action(action_type="respond", task_id=3))
print("Reward:", reward)
print("Score:", info["score"])

print("\n=== FINAL STATE ===")
for task in env.state():
    print(task)