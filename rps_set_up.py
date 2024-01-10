import pygame as pg
import math as mt

# pygame setup
pg.init()
pg.font.init()
pg.display.set_caption('Rock, Paper, Scissors')
screen = pg.display.set_mode((1000, 620))
running = True
color = 61, 82, 114
bg = pg.transform.scale(pg.image.load('bg.jpg'),(1000, 620))
coord = 0, 0
screen.blit(bg, (coord))
icon_size = (250, 200)

#loading in menus and graphics
start_menu = pg.transform.scale(pg.image.load("menu.png"), (500.91, 460))
inst_menu = pg.transform.scale(pg.image.load("inst.png"), (500.91, 460))
p1_wins = pg.transform.scale(pg.image.load("p1_wins.png"), (500.91, 460))
p2_wins = pg.transform.scale(pg.image.load("p2_wins.png"), (500.91, 460))

#adding a font
font = pg.font.Font('BolgartDisplay.otf', 45)

#for background music
bgm = pg.mixer.music.load('brain.mp3')
pg.mixer.music.play()

#seeting up the clock
clock = pg.time.Clock()

#to set the element places within the game window
p1_place = screen.get_width()//6, screen.get_height()//3
p2_place = screen.get_width()//1.75, screen.get_height()//3
p1_score_place = screen.get_width()//9, screen.get_height()//9
p2_score_place = screen.get_width()//1.5, screen.get_height()//9

# rock, paper, scissors container
r = ['rock_l.png', 'rock_r.png']
p = ['paper_l.png', 'paper_r.png']
s = ['scissor_l.png', 'scissor_r.png']

#to store player scores
p1_score = 0
p2_score = 0

#score increment and best of determiner for a whole game
inc = 1
best_of = 5

#to store the player moves (changes every round)
p1_move = ''
p2_move = ''

#function for the menu
def menu():
    time_2 = pg.time.get_ticks()/100
    y_coord = 9*mt.sin(0.3*time_2)
    screen.blit(bg, (coord))
    screen.blit(start_menu, (225, y_coord+60))

#function for the instructions
def instructions():
    time_2 = pg.time.get_ticks()/100
    y_coord = 9*mt.sin(0.3*time_2)
    screen.blit(bg, (coord))
    screen.blit(inst_menu, (225, y_coord+60))

#fucntion for when player 1 wins
def p1_win():
    time = pg.time.get_ticks()/100
    y_coord = 9*mt.sin(0.3*time)
    screen.blit(bg, (coord))
    screen.blit(p1_wins, (225, y_coord+60))

#function for when player 2 wins
def p2_win():
    time = pg.time.get_ticks()/100
    y_coord = 9*mt.sin(0.3*time)
    screen.blit(bg, (coord))
    screen.blit(p2_wins, (225, y_coord+60))

#function for the y-coordinate of the players' positions
def pos_players(x):
    initial_y = -1*mt.sqrt(-1*(1000*(3*(-1*x)-500))/3)+(620/2)
    y = pg.math.clamp(initial_y,120.0, 230.0)
    return y

#function for the starting elements before each round
def starter():
    time = (pg.time.get_ticks() % 1000)/3
    initial_x = -1*((3*(time**2) - 1860*time - 211700)/3000)
    x_for_func = (3*(time**2) - 1860*time - 211700)/3000
    #to restrict the range of the function
    x_2 = pg.math.clamp(initial_x, 600.0, 700.0)
    x_1 = x_2-500
    screen.blit(bg, (coord))
    screen.blit(pg.transform.scale(pg.image.load('rock_l.png'),icon_size), (x_1, pos_players(x_for_func)))
    screen.blit(pg.transform.scale(pg.image.load('rock_r.png'),icon_size), (x_2, pos_players(x_for_func)))


#function for blitting player scores to the screen   
def blitScores():
    screen.blit(p1_stext, (p1_score_place))
    screen.blit(p2_stext, (p2_score_place))

#function for checking each players' move for scoring
def scoring(p1_move, p2_move):
    if p1_move in r and (p2_move not in p and p2_move not in r):
        return "p1"
    elif p1_move in p and (p2_move not in s and p2_move not in p):
        return "p1"
    elif p1_move in s and (p2_move not in r and p2_move not in s):
        return "p1"
    elif p2_move in r and (p1_move not in p and p1_move not in r):
        return "p2"
    elif p2_move in p and (p1_move not in s and p1_move not in p):
        return "p2"
    elif p2_move in s and (p1_move not in r and p1_move not in s):
        return "p2"

#function for announcing the current match's winner
def winner(p1_score, p2_score):
    mssg_place = screen.get_width()//3, screen.get_height()//2.3
    if p1_score == 5:
        p1_win()
    elif p2_score == 5:
        p2_win()

#to determine if the game just started
run = 0
start = 0

#to be able to call some functions within every iteration under their respective conditions
to_loop = []

#game loop
while running:
    if run == 0 and start == 0:
        menu()
    elif run>0 and start>0 and p1_score != best_of and p2_score != best_of:
        starter()
        blitScores() 
        pg.time.wait(402)
    
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
        if p1_score != best_of and p2_score != best_of:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    start+=1
                    to_loop.append("s")
                elif event.key == pg.K_g:
                    to_loop.append("g")
                elif event.key == pg.K_1:
                    p1_move = 'rock_l.png'
                elif event.key == pg.K_2:
                    p1_move = 'paper_l.png'
                elif event.key == pg.K_3:
                    p1_move = 'scissor_l.png'
                elif event.key == pg.K_7:
                    p2_move = 'rock_r.png'
                elif event.key == pg.K_8:
                    p2_move = 'paper_r.png'
                elif event.key == pg.K_9:
                    p2_move = 'scissor_r.png'
                elif event.key == pg.K_p:
                    if scoring(p1_move, p2_move) == "p1":
                        p1_score += inc
                    elif scoring(p1_move, p2_move) == "p2":
                        p2_score += inc
                    screen.blit(bg, (coord))
                    screen.blit(pg.transform.scale(pg.image.load(p1_move),icon_size), (p1_place))
                    screen.blit(pg.transform.scale(pg.image.load(p2_move),icon_size), (p2_place))
                    p1_stext = font.render(f'score: {p1_score}', True, color)
                    p2_stext = font.render(f'score: {p2_score}', True, color)
                    blitScores()
                    time_elapsed = pg.time.get_ticks()
                    run+=1
        if p1_score == best_of or p2_score == best_of:
            winner(p1_score, p2_score)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    p1_score = 0
                    p2_score = 0
                    p1_stext = font.render(f'score: {p1_score}', True, color)
                    p2_stext = font.render(f'score: {p2_score}', True, color)
                    blitScores()
    if "s" in to_loop and start==1:
        instructions()
    if "g" in to_loop and run==0:
        start+=1
        starter()
        score = font.render('score: 0', True, color)
        screen.blit(score, (p1_score_place))
        screen.blit(score, (p2_score_place))
    pg.display.flip()
    clock.tick(120)

pg.quit()