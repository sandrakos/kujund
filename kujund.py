class Pyramid:
    def __init__(self, base_length, height):
        self.base_length = base_length
        self.height = height

    def base_area(self):
        return round(self.base_length ** 2, 3)

    def volume(self):
        return round((1/3) * self.base_area() * self.height, 3)

    def slant_height(self):
        return (self.height**2 + (self.base_length/2)**2) ** 0.5

    def lateral_surface_area(self):
        return round(2 * self.base_length * self.slant_height(), 3)

    def surface_area(self):
        return round(self.base_area() + self.lateral_surface_area(), 3)
