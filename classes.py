import random

import pygame as pg
from random import choice, randint

class Ciringa(pg.sprite.Sprite):
    vidas = 5

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\vacina_nova.png') # Carrega a imagem
        self.image = pg.transform.scale2x(self.image) ## Altera escala da imagem
        # self.image = pg.transform.scale2x(self.image)
        # self.image = pg.transform.scale(self.image, (10,20))
        retangulo = self.image.get_rect()
        self.rect = pg.Rect(250,530, retangulo.x, retangulo.y)
        self.velocidade = 0
        self.aceleracao = 0.3
        self.doses = 15

    def update(self, *args):
        key = pg.key.get_pressed()

        if key[pg.K_d]:
            self.velocidade += self.aceleracao
        elif key[pg.K_a]:
            self.velocidade -= self.aceleracao
        else:
            self.velocidade *= 0.1

        self.rect.x += self.velocidade

        if self.rect.x < 0:
            self.rect.x = 0
            self.velocidade = 0
        elif self.rect.x > 440:
            self.velocidade = 0
            self.rect.x = 440


class Coronas(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load(choice(
        ['C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\corona_3.png',
                'C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\corona_2.png',
                'C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\corona_1.png',
                ]))
        self.image = pg.transform.scale2x(self.image)  ## Altera escala da imagem
        self.image = pg.transform.scale2x(self.image)
        self.rect = pg.Rect(randint(0,440), -130, 100, 100)
        self.timer = 0
        self.pontuacao = 0
        self.velocidade = randint(2,6)

    def update(self, *args):
        self.rect.y += self.velocidade
        if self.rect.y > 600:
            Ciringa.vidas -=1
            self.kill()


class Projetil(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\nova_gota.png')
        self.image = pg.transform.scale(self.image, [10,10])
        self.rect = self.image.get_rect()
        self.velocidade = -5

    def update(self, *args):
        self.rect.y += self.velocidade

        if self.rect.y < -10:
            self.kill()


class Doses(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\dose.png')
        self.image = pg.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 440)
        self.rect.y = -20
        self.speed = random.randint(1,3)

    def update(self, *args):
        self.rect.y += self.speed


class Mascara(Doses):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\mascara.png')
        self.image = pg.transform.scale2x(self.image)


class Variantes(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\variante.png')
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale2x(self.image)
        self.rect.x = randint(80,420)
        self.rect.y = -80
        self.speed = 1
        self.vidas = 3

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > 600:
            Ciringa.vidas -=3

        if self.vidas == 0:
            self.kill()











