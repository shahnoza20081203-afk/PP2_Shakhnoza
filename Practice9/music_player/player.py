import pygame
import os


class MusicPlayer:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_dir = os.path.join(self.base_dir, "music")

        self.playlist = [
            "song1.mp3",
            "song2.mp3",
            "song3.mp3"
        ]

        self.current_song = 0

    def play(self):
        path = os.path.join(
            self.music_dir,
            self.playlist[self.current_song]
        )

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_song = (
            self.current_song + 1
        ) % len(self.playlist)

        self.play()

    def previous_song(self):
        self.current_song = (
            self.current_song - 1
        ) % len(self.playlist)

        self.play()

    def get_current_song(self):
        return self.playlist[self.current_song]
