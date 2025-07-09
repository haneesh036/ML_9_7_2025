import random
import statistics

random_numbers = [random.randint(100, 150) for _ in range(100)]

print("Mean:", statistics.mean(random_numbers))

print("Median:", statistics.median(random_numbers))

print("Mode:", statistics.mode(random_numbers))
