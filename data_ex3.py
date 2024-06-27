import random

def toss_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

print("Tossing a coin...")
results = []
for i in range(1, 4):
    result = toss_coin()
    results.append(result)
    print(f"Round {i}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")
