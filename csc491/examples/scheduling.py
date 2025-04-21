import random

random.seed(42)
num_tasks = 1000
max_deps_per_task = 8  # can adjust to make it more or less connected
edges = []

for to_task in range(1, num_tasks):
    num_deps = random.randint(0, min(max_deps_per_task, to_task))
    from_tasks = random.sample(range(to_task), num_deps)
    for from_task in from_tasks:
        edges.append((from_task+1, to_task+1))

# Print dependencies
for from_task, to_task in edges:
    print(f"{from_task} {to_task}")
