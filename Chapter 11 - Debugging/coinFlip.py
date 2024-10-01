import random

head = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 0:
        head += 1
    if i == 500:
        print("Halway done!")
print("Heads came up " + str(head) + " times.")
