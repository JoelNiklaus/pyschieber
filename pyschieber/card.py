class Card:
    names = {10: 'Banner', 11: 'Under', 12: 'Ober', 13: 'Könnig', 14: 'As'}

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        name = str(self.value)
        if self.value > 9:
            name = Card.names[self.value]
        return '<{0}:{1}>'.format(self.suit.name, name)
