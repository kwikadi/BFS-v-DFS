import random
import itertools

def get_random_pairs(numbers):
  # Generate all possible non-repeating pairs
  pairs = list(itertools.combinations(numbers, 2))

  # Randomly shuffle these pairs
  random.shuffle(pairs)
  return pairs[::2]


numbers = 1000
a = random.randint(0,numbers)
b = random.randint(0,numbers)

with open('input.txt', 'w') as outputFile:
    outputFile.write(str(numbers) + '\n')
    outputFile.write(str(a) + '\n')
    outputFile.write(str(b) + '\n')
    for pair in get_random_pairs(range(numbers)):
        outputFile.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
