import pygame


class Sound:

    def __init__(self) -> None:
        self.mute = False
        self.sounds = {
            'ho': pygame.mixer.Sound('audio/ho.ogg'),
            'eat': pygame.mixer.Sound('audio/eat.ogg'),
            'rep': pygame.mixer.Sound('audio/rep.ogg'),
            'die': pygame.mixer.Sound('audio/die.ogg')
        }

    def play(self, sound_id:str) -> None:
        if self.mute:
            return
        self.sounds[sound_id].play()

    def play_eat(self):
        self.play('eat')

    def play_rep(self):
        self.play('rep')

    def play_die(self):
        self.play('die')
