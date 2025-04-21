import random

random.seed(42)  # for reproducibility

num_items = 100
items = []

for _ in range(num_items):
    weight = random.randint(1, 20)
    value = random.randint(10, 100)
    items.append((weight, value))

# Print each item as "weight,value" on a new line
for w, v in items:
    print(f"{w} {v}")
