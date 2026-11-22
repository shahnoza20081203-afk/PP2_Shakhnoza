import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (70, 130, 220)
GRAY = (200, 200, 200)

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 20)

player = MusicPlayer()

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_song()

            elif event.key == pygame.K_b:
                player.previous_song()

            elif event.key == pygame.K_q:
                running = False

    title = font.render("Music Player", True, BLACK)
    screen.blit(title, (300, 40))

    song_text = small_font.render(
        "Now Playing: " + player.get_current_song(),
        True,
        BLACK
    )
    screen.blit(song_text, (250, 120))

    playlist_title = small_font.render("Playlist:", True, BLACK)
    screen.blit(playlist_title, (100, 180))

    for i, song in enumerate(player.playlist):

        if i == player.current_song:
            color = BLUE
        else:
            color = BLACK

        text = small_font.render(song, True, color)
        screen.blit(text, (100, 220 + i * 35))

    pygame.draw.rect(screen, GRAY, (100, 350, 600, 15))

    if pygame.mixer.music.get_busy():
        position = pygame.mixer.music.get_pos() / 1000
        progress_width = min(int(position * 10), 600)

        pygame.draw.rect(
            screen,
            BLUE,
            (100, 350, progress_width, 15)
        )

    controls = [
        "P - Play",
        "S - Stop",
        "N - Next track",
        "B - Previous track",
        "Q - Quit"
    ]

    for i, control in enumerate(controls):
        text = small_font.render(control, True, BLACK)
        screen.blit(text, (100, 390 + i * 22))

    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.quit()
