# main.py
import sys
import pygame
from scenes.menu_scene import MenuScene

def main():
    pygame.init()

    WIDTH, HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mission Horizon")

    clock = pygame.time.Clock()
    FPS = 60

    # Start the application on the Menu Screen
    active_scene = MenuScene()

    running = True
    while running:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        # Global event checking (like clicking the window close button)
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Pass inputs over to the active scene
        active_scene.process_input(events, keys)
        active_scene.update()

        # Render the current scene
        active_scene.render(screen)
        pygame.display.flip()

        # Monitor for scene updates
        if active_scene != active_scene.next_scene:
            active_scene = active_scene.next_scene

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
