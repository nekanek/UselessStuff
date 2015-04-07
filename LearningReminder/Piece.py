from datetime import date


class LearnedPiece:
    def __init__(self, desc, tags, d=date.today()):
        self.desc = desc
        self.tags = list(tags)
        self.date = d

    def __repr__(self):
        return self.desc + ", " + str(self.tags) + ", " + str(self.date)