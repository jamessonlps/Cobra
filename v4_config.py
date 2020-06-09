import pygame
from os import path
from math import pi
# Configurações da Tela
WIDTH = 700
HEIGHT = 450

# Clock
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)/1000

# Identifica diretórios de imagens, sons e fontes
GAME_DIR = path.dirname(__file__)
MAP_DIR = path.join(GAME_DIR, 'maps')
IMG_DIR = path.join(GAME_DIR, 'assets/img')
SONG_DIR = path.join(GAME_DIR, 'assets', 'song')
FONT_DIR = path.join(GAME_DIR, 'assets', 'fontes')

# Layers: -- Faz o jogo dar blit numa sequência específica
WALL_LAYER = 1
PLAYER_LAYER = 3
FRUITS_LAYER = 2

# Configurações do player
PLAYER_SPEED = 15
PLAYER_HEALTH = 100
PLAYER_VISION = 150
PLAYER_HIT_RECT = pygame.Rect (0, 0, 35, 35)

# DIREÇÃO DE MOVIMENTO



# Tamanho da cobrinha
SNAKE_WIDTH = 64
SNAKE_HEIGHT = 64

# Tamanho dos objetos
OBJECT_WIDTH = 20
OBJECT_HEIGHT = 20

# === Lista de Imagens p/ carregar
# FRUTAS
LISTA_FRUTAS = ['abacaxi.png', 'cereja.png', 'laranja.png', 'limao.png', 'maca.png', 'morango.png', 'uva.png']
WALK_LEFT = ['L0.png', 'L1.png', 'L2.png']
WALK_RIGHT = ['R0.png', 'R1.png', 'R2.png']
WALK_UP = ['U0.png', 'U1.png', 'U2.png']
WALK_DOWN = ['D0.png', 'D1.png', 'D2.png']

# Configuração do MHS:
A = 10 # amplitude do movimento
T = 2000  # período em milisseg
OMEGA = 2*pi/T

# Arsenal de cores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BROWN = (106, 55, 5)
ORANGE = [255, 140, 0]

# Estados para controle do fluxo
INIT = 0
GAME = 1
QUIT = 2

# Configurações do mob Bird
BIRD_IMG = 'tile004.png'
BIRD_SPEEDS = [20, 15, 10, 5, 10]
BIRD_HEALTH = 100
BIRD_DAMAGE = 10 # dano que o pássaro causa
BIRD_KNOCKBACK = 30 # repulsão quando atinge player
BIRD_HIT_RECT = pygame.Rect (0, 0, 30, 30) #ret. de colisão
BIRD_ZONE = 100 # círculo que evita superposição de pássaros

# REFERÊNCIAS
"""
https://opengameart.org/content/2d-fruits  #tile de frutas
https://opengameart.org/content/lpc-terrain-repack # tile de terrenos
https://opengameart.org/content/king-cobra # tile da cobrinha

"""
