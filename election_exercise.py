class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0
        
    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other
        return self

class Election:
    def __init(self, candidates):
        self.candidates = candidates