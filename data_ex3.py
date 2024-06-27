import random

def toss_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

user_name = input("Who are you?\n> ")
print(f"Hello, {user_name}!")

print("Tossing a coin...")
results = []
for i in range(1, 4):
    result = toss_coin()
    results.append(result)
    print(f"Round {i}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
    print(f"{user_name} won!")
else:
    print(f"{user_name} lost!")

