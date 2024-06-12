from model import Model
from view import View

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)
        self.view.set_calculate_button_command(self.calculate_pyramid)

    def calculate_pyramid(self):
        base_length = self.view.get_base_length()
        height = self.view.get_height()

        if base_length is not None and height is not None:
            self.model.create_pyramid(base_length, height)
            pyramid = self.model.get_pyramid()
            base_area = pyramid.base_area()
            volume = pyramid.volume()
            lateral_surface_area = pyramid.lateral_surface_area()
            surface_area = pyramid.surface_area()

            self.view.display_results(base_area, volume, lateral_surface_area, surface_area)
