print("""# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. #""")

from pygame import mixer # importa somente a funcionalidade mixer do módulo pygame
mixer.init() # comando inicia o uso da bibliote do pygame
mixer.music.load('ex021.mp3')# comando carrega o audio
mixer.music.play() # comando começa tocar a música
parar = input('Digite algo para parar ...') # comando e espera o evento terminar para encerrar o programa
