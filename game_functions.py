import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, ship):
    """Update images on screen and flip to new screen."""
    #Redraw screen druing each pass through loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make most recently drawn screen visible.
    pygame.display.flip()
