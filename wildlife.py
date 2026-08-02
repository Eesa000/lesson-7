import pygame
import sys

# Initialize Pygame
pygame.init()

# Create the display window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

# Load and scale images
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

animal = pygame.image.load("wildlife.png")
animal = pygame.transform.scale(animal, (250, 250))

# Create fonts
title_font = pygame.font.Font(None, 48)
text_font = pygame.font.Font(None, 30)

# Render text
title = title_font.render("Wildlife Information Display", True, (255, 255, 255))
fact = text_font.render(
    "Fun Fact: Tigers are excellent swimmers!", True, (255, 255, 0)
)

# Clock for frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Draw animal image
    screen.blit(animal, (275, 170))

    # Draw text
    screen.blit(title, (120, 40))
    screen.blit(fact, (80, 520))

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()