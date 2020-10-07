import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **counts):
    self.counts = copy.deepcopy(counts)
    self.contents = []
    for k,v in counts.items():
      self.contents += [k] * v

  def draw(self, n):
    contents = []
    if n > len(self.contents):
      contents = self.contents
      self.contents = []
      return contents
    for i in range(n):
      x = random.randint(0, len(self.contents) - 1)
      contents.append(self.contents[x])
      self.contents = self.contents[:x] + self.contents[x+1:]
    return contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for i in range(num_experiments):
    curhat = copy.deepcopy(hat)
    x = curhat.draw(num_balls_drawn)
    x_counts = Counter(x)
    flag = 1
    for k, v in expected_balls.items():
      if x_counts.get(k, 0) < v:
        flag = 0
        break
    success += flag
  if success == 0:
    return 0
  return success / num_experiments

