import colours

class ColourMapper:
    def __init__(self):
        self.forward_map = {
            "red": colours.red,
            "orange": colours.orange,
            "yellow": colours.yellow,
            "green": colours.green,
            "blue": colours.blue,
            "purple": colours.purple,
            "white": colours.white,
            "pink": colours.pink,
        }
        self.reverse_map = {v: k for k, v in self.forward_map.items()}

    def map_colour(self, colour):
        return self.forward_map.get(colour, colours.nothing)

    def reverse_map_colour(self, colour):
        return self.reverse_map.get(colour, "nothing")