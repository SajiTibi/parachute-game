import random

import pygame
import pygame.draw
import pygame.image
import pygame.mouse

from BoatController import BoatDriver
from BoatModel import BoatModel
from BoatView import BoatView
from ParachuteController import ParachuteController
from ParachuteDescriptor import ParachuteDescriptor
from ParachuteModel import ParachuteModel
from ParachuteView import ParachuteView
from PlaneController import PlaneController
from PlaneModel import PlaneModel
from PlaneView import PlaneView


class App:
    def __init__(self):
        self._running = False
        self.display = None
        self.my_font = None
        self.clock = None
        self.debug_mode = True
        self.size = self.width, self.height = 640, 400
        self.background_color = [255, 255, 255]
        self.score = 0
        self.lives = 3

    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.my_font = pygame.font.Font(pygame.font.get_default_font(), 12)
        self.display.fill(self.background_color)
        self._running = True
        self.clock = pygame.time.Clock()
        pygame.display.update()

    def on_render(self):
        score_text = self.my_font.render(f'Score: {self.score}', 1, (0, 0, 0))
        lives_text = self.my_font.render(f'Lives: {self.lives}', 1, (0, 0, 0))
        debug_mode_text = self.my_font.render(f'Debug Mode: {self.debug_mode}', 1, (0, 0, 0))
        self.display.blit(score_text, (0, 0))
        self.display.blit(lives_text, (0, 10))
        self.display.blit(debug_mode_text, (0, 20))
        pygame.display.update()
        self.display.fill(self.background_color)
        self.clock.tick(120)

    def on_execute(self):
        self.on_init()
        drop_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(drop_timer, 1000)
        # please do note the image is loaded here and not in view cause we need its dimension for the model to check
        # intersection with other objects
        plane_img_path = "./resources/plane.png"
        plane_img = pygame.image.load(plane_img_path)
        plane_view = PlaneView(self.display, plane_img, self.debug_mode)
        plane = PlaneModel(self.width - plane_img.get_width(), 0, plane_img.get_width(), plane_img.get_height(),
                           self.width - plane_img.get_width())
        plane_controller = PlaneController()
        plane_controller.set_plane_model(plane)

        sea_lvl = 200
        sea_rect = pygame.rect.Rect(0, 300, 640, 100)

        boat_img_path = "./resources/boat.png"
        boat_img = pygame.image.load(boat_img_path)
        boat_view = BoatView(self.display, boat_img, self.debug_mode)
        boat = BoatModel(200, 200, boat_img.get_width(), boat_img.get_height())
        boat_driver = BoatDriver()
        boat_driver.set_model(boat)

        parachute_img_path = "./resources/parachutist.png"
        parachute_img = pygame.image.load(parachute_img_path)
        parachute_view = ParachuteView(self.display, parachute_img, self.debug_mode)
        parachute_model = ParachuteModel()
        parachute_controller = ParachuteController()
        parachute_controller.set_model(parachute_model)

        while self._running:
            parachute_controller.fall()
            plane_controller.drive()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                boat_driver.drive(boat.get_speed())
            elif keys[pygame.K_LEFT]:
                boat_driver.drive(-boat.get_speed())

            for p in parachute_controller.parachute_model.get_parachutes():
                if p.intersects(boat):
                    self.score += 10
                    parachute_controller.parachute_model.remove_parachute(p)
                    continue
                if p.y >= sea_lvl:
                    self.lives -= 1
                    if self.lives <= 0:
                        self._running = False
                        print(f'Game ended. Score:{self.score}')
                        return pygame.quit()
                    parachute_controller.parachute_model.remove_parachute(p)
                    continue

            for event in pygame.event.get():
                if event.type == drop_timer:
                    p_desc = ParachuteDescriptor(plane.x, plane.y, parachute_img.get_width(),
                                                 parachute_img.get_height())
                    parachute_model.add_parachute(p_desc)
                    next_spawn_time = random.randint(1000, 3000)
                    pygame.time.set_timer(drop_timer, next_spawn_time)

            pygame.draw.rect(self.display, (0, 0, 255), sea_rect)
            parachute_view.draw(parachute_controller.parachute_model.get_parachutes())
            plane_view.draw(plane)
            boat_view.draw(boat)
            self.on_render()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
