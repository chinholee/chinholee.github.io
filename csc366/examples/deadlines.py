import random

random.seed(42)

num_tasks = 10000
tasks = []

for _ in range(num_tasks):
  duration = random.randint(1, 100)
  deadline = random.randint(duration, duration + 1000)
  tasks.append((duration, deadline))

for duration, deadline in tasks:
    print(f"{duration} {deadline}")
