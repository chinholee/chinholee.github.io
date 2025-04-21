import random

random.seed(42)

num_vertices = 20
vertices = list(range(1, num_vertices + 1))

# Step 1: Create a random Hamiltonian cycle
random.shuffle(vertices)
edges = set()
for i in range(num_vertices):
    u = vertices[i]
    v = vertices[(i + 1) % num_vertices]  # wrap around to form a cycle
    weight = random.randint(1, 30)
    edge = tuple(sorted((u, v)) + [weight])
    edges.add(edge)

# Step 2: Add extra edges to make it more connected (optional)
extra_edges = random.randint(10, 30)  # Add a few extra edges for richness
while len(edges) < num_vertices + extra_edges:
    u = random.randint(1, num_vertices)
    v = random.randint(1, num_vertices)
    if u != v:
        edge_pair = tuple(sorted((u, v)))
        if all(e[:2] != edge_pair for e in edges):
            weight = random.randint(1, 30)
            edges.add((edge_pair[0], edge_pair[1], weight))

# Step 3: Print all edges
for u, v, w in sorted(edges):
    print(f"{u} {v} {w}")
