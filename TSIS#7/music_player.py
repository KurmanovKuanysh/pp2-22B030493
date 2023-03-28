import pygame
import os

pygame.init()

WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)


music_files = [os.path.abspath("Pygame/music/alarm.mp3"),               os.path.abspath(
    "Pygame/music/2.wav"),               os.path.abspath("Pygame/music/3.wav")]
current_music_file_index = 0

pygame.mixer.music.load(music_files[current_music_file_index])
pygame.mixer.music.play()

font = pygame.font.SysFont(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:
                current_music_file_index = (
                    current_music_file_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_file_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_music_file_index = (
                    current_music_file_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_file_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

    # Clear the screen
    screen.fill((255, 255, 255))


    text_surface = font.render(os.path.basename(
        music_files[current_music_file_index]), True, (0, 0, 0))
    text_rect = text_surface.get_rect(
        center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

