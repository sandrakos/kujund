from kujund import Pyramid

class Model:
    def __init__(self):
        self.pyramid = None

    def create_pyramid(self, base_length, height):
        self.pyramid = Pyramid(base_length, height)

    def get_pyramid(self):
        return self.pyramid
