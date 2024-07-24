TRAP_ARTIST=[
    "Reacky Ross"
    "future"
    "designer"
]
class Trapartist:
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name
    @name.__setattr__
    def name(self, name):
        if name not in TRAP_ARTIST:
            raise ValueError("is not a TRAPARTIST" % name)
        self.name=name
    
rr = Trapartist('Reacky Ross')
print(rr.name)
rr.name = 'reacky rose'
print(rr.name)