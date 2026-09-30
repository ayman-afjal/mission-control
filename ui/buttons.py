import pygame

class Button:
    def __init__(
        self,
        text,
        x,
        y,
        width,
        height,
        font,
        normal_color=(50, 50, 60),
        hover_color=(80, 80, 100),
        text_color=(255, 255, 255),
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

        # Pre-render text surface and center it within the button rect
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update(self, mouse_pos):
        """Update hover state based on current mouse position."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        """Returns True if the left mouse button was clicked on this button."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False

    def render(self, screen):
        """Draw the button background and centered text."""
        color = self.hover_color if self.is_hovered else self.normal_color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        # Optional border stroke
        pygame.draw.rect(screen, (120, 120, 140), self.rect, width=2, border_radius=8)
        screen.blit(self.text_surf, self.text_rect)