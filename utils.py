import random

# Generate <count> random numbers from [0, limit)
def random_numbers(limit: int, count: int) -> list[int]:
    numbers: set[int] = set()
    while len(numbers) != count:
        numbers.add(random.randrange(limit))
    return list(numbers)

