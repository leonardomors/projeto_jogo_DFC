import random
import time

import pygame as pg
from classes import Ciringa, Projetil, Coronas, Doses, Mascara, Variantes
import pyautogui



def main():
    def tela_derrota():
        txt3 = 'GAME OVER'
        text3 = fonte_over.render(txt3, True, (255, 255, 255))
        display.blit(bg_derrota, (0, 0))
        display.blit(text3, (60, 160))
        display.blit(texto_novo, (60, 350))
        display.blit(txt_novo_2, (180,400))

    def tela_inicial():
        tela0 = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\defeat_corona_virus.jpg')
        display.blit(tela0, (0,0))


    # Mensagens na tela
    pg.font.init()
    fonte = pg.font.Font("C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\fonte_2.ttf", 20)
    fonte_over = pg.font.Font("C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\FONTE.ttf",95)
    txt_novo = 'Deseja começar um novo jogo?'
    txt_novo_2 = 'Pressione F'
    texto_novo = fonte.render(txt_novo, True, (255,255,255))
    txt_novo_2 = fonte.render(txt_novo_2, True, (255,255,255))



    # Criando e personalizando o display
    pg.init()
    display = pg.display.set_mode([500,600])
    pg.display.set_caption('Derrote o corona')
    clock = pg.time.Clock()

    # Tela de fundo
    grupo_bg = pg.sprite.Group()
    bg = pg.sprite.Sprite(grupo_bg)
    bg.image = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\hospital.jpg')
    bg.image = pg.transform.scale(bg.image, [500,600])
    bg.rect = bg.image.get_rect()

    bg_derrota = pg.image.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\bg_derrota.png')
    bg_derrota = pg.transform.scale(bg_derrota, [500,600])

    # Musicas e sons
    pg.mixer.init()

    tiro_som = pg.mixer.Sound('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\tiro.mp3')
    morte_som = pg.mixer.Sound('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\game_over.mp3')
    item_som = pg.mixer.Sound('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\item.mp3')
    pg.mixer.Sound.set_volume(item_som, 0.1)
    pg.mixer.Sound.set_volume(tiro_som, 0.05)
    pg.mixer.Sound.set_volume(morte_som, 0.1)
    pg.mixer.music.load('C:\\Users\\leomo\\PycharmProjects\\Ateroides_corona\\novo_jogo\\musica_jogo.ogg')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1)
    # pg.mixer.so.set_volume(0.5)



    # Objetos
    grupo_ciringa = pg.sprite.Group()
    vacina = Ciringa(grupo_ciringa)
    grupo_corona = pg.sprite.Group()
    grupo_tiros = pg.sprite.Group()
    grupo_doses = pg.sprite.Group()
    grupo_mascara = pg.sprite.Group()
    grupo_variantes = pg.sprite.Group()

    # Outras variaveis
    game_over = False
    pontuacao = 0
    gameLoop = True
    timer = 0
    timer_2 = 0
    timer_3 = 0

    ## Criando loop do jogo

    if __name__ == '__main__':
        while gameLoop:


            clock.tick(60)
            for evento in pg.event.get():
                keys = pg.key.get_pressed()
                if evento.type == pg.QUIT:
                    gameLoop = False

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        pyautogui.PAUSE = 1
                        if vacina.doses > 0:
                            tiro = Projetil(grupo_ciringa, grupo_tiros)
                            tiro.rect.center = vacina.rect.center
                            tiro.rect.x +=10
                            pg.event.wait(2)
                            tiro_som.play()
                            vacina.doses -=1
                if game_over == True:
                    if evento.type == pg.KEYDOWN:
                        if evento.key == pg.K_f:
                            game_over = False
                            main()



            #Updates da logica
            if not game_over:

                vacina.update()
                grupo_corona.update()
                grupo_tiros.update()
                grupo_doses.update()
                grupo_mascara.update()
                grupo_variantes.update()

                timer += 1
                timer_2 +=1
                timer_3 +=1
                if timer_3 > 800: # A cada 15s surge uma mascara (vida extra)
                    nova_mascara = Mascara(grupo_ciringa, grupo_mascara)
                    timer_3 = 0
                    nova_variante = Variantes(grupo_ciringa, grupo_variantes)

                if timer_2 > 600:  # A cada 10s surge um novo frasco de doses
                    nova_dose = Doses(grupo_ciringa, grupo_doses)
                    timer_2 = 0


                if timer > 30:   # a cada meio segundo (que corresponde a 30 updates na variavel timer, se usarmos 60fps)
                    timer = 0    # existe 50% de chance de adicionar um novo corona


                    if pontuacao < 20:
                        if random.random() < 0.3: # 30% de chance de criar um novo corona
                            novo_corona = Coronas(grupo_ciringa, grupo_corona)
                        if random.random() < 0.005:
                            Doses(grupo_ciringa, grupo_doses)


                    elif pontuacao >= 20 and pontuacao < 50:
                        if random.random() < 0.5: # 60% de chance de criar um novo corona
                            novo_corona = Coronas(grupo_ciringa, grupo_corona)
                        if random.random() < 0.0005:
                            nova_variante = Variantes(grupo_ciringa, grupo_variantes)
                        if random.random() < 0.09:
                            nova_dose = Doses(grupo_ciringa, grupo_doses)

                    elif pontuacao > 50:
                        if random.random() < 0.7:  # 80% de chance de criar um novo corona
                            novo_corona = Coronas(grupo_ciringa, grupo_corona)
                        if random.random() < 0.001:
                            nova_variante = Variantes(grupo_ciringa, grupo_variantes)
                        if random.random() < 0.1:
                            nova_dose = Doses(grupo_ciringa, grupo_doses)

                # Colisoes


                hit = pg.sprite.groupcollide(grupo_tiros, grupo_corona, True, True, pg.sprite.collide_mask)
                if hit:
                    pontuacao += 1

                colisao_dose_vacina = pg.sprite.spritecollide(vacina, grupo_doses, True, pg.sprite.collide_mask)
                if colisao_dose_vacina:
                    vacina.doses += 15
                    item_som.play()

                colisao_mascara_vacina = pg.sprite.spritecollide(vacina, grupo_mascara, True, pg.sprite.collide_mask)
                if colisao_mascara_vacina:
                    Ciringa.vidas += 1
                    item_som.play()

                hit_variante = pg.sprite.groupcollide(grupo_tiros, grupo_variantes, True, False, pg.sprite.collide_mask)
                colisao_variante = pg.sprite.spritecollide(vacina, grupo_variantes, True, pg.sprite.collide_mask)



                if hit_variante:
                    nova_variante.vidas -=1
                    pontuacao += 1
                    hit_variante = False

                colisao_corona_ciringa = pg.sprite.spritecollide(vacina, grupo_corona, False, pg.sprite.collide_mask)
                if colisao_corona_ciringa or colisao_variante or Ciringa.vidas == 0:
                    pg.mixer.music.stop()
                    game_over = True
                    Ciringa.vidas = 3
                    morte_som.play()
                    tela_derrota()


                pg.display.update()


                # Desenhos
                display.fill((255, 255, 255))
                grupo_bg.draw(display)
                grupo_ciringa.draw(display)
                grupo_corona.draw(display)
                grupo_doses.draw(display)
                grupo_mascara.draw(display)
                grupo_variantes.draw(display)
                txt1 = f'Pontuação: {pontuacao}'
                texto = fonte.render(txt1, True, (0, 0, 0))
                txt2 = f'Vidas: {Ciringa.vidas}'
                texto2 = fonte.render(txt2, True, (0,0,0))
                txt3 = f'Doses: {vacina.doses}'
                txt3 = fonte.render(txt3, True, (0,0,0))


                display.blit(texto2, (335, 85))
                display.blit(texto, (335,50))
                display.blit(txt3, (335, 120))



if __name__ == '__main__':
    main()