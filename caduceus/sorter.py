class SnakeSorter:   
 def __init__(self, snakes):
"""initializes snake sorter"""
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
"""sorts snakes by weight"""
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
"""sorts snakes by length"""
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)

