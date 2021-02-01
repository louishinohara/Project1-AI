# Node: used for search algorithm
class Node():
  def __init__(self, x: int, y: int, prev=None):
      self.x = x
      self.y = y
      self.prev = prev