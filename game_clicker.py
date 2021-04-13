import pygame

# some constants
WIDTH = 800
HEIGHT = 650
# colors
WHITE = (255, 255, 255)
RED = (254, 0, 98)
BLUE = (60, 50, 255)
BLACK = (0, 0, 0)
PINK = (254, 202, 177)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# set the start picture
sport_surf = pygame.image.load('firstscreen.jpg')
sport_rect = sport_surf.get_rect(bottomright=(650, 550))
screen.blit(sport_surf, sport_rect)

# text at the top of the page
font_ = pygame.font.Font(None, 29)
words = font_.render("Hello, my dear friend", True, BLACK)
screen.blit(words, (300, 10))

words = font_.render("Due to quarantine in 2020, you are very fat. And now you and I need to lose weight.", True,
                     BLACK)
screen.blit(words, (10, 570))
words = font_.render("To go out, you need to reset 1,000,000,000,000 kcal. Good luck! You will succeed!", True, BLACK)
screen.blit(words, (10, 600))

words = font_.render("press space to start", True, RED)

screen.blit(words, (300, 623))

pygame.display.update()

# COUNTERS
num_of_clicks = -1
MAX = 1_000_000_000_000
Produce = 0


class Button:
    # producing1 - how much it will plus to producing, if you press the button
    # producing2 - how much is it produce now
    def __init__(self, x, y, width, height, text='', producing1=0.0, producing2=0, costs=MAX, number=0, color=PINK):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.producing1 = producing1
        self.costs = costs
        self.producing2 = producing2
        self.number = number

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont('comicsans', 25)
        text = font.render(self.text, True, BLACK)
        win.blit(text, (
            self.x + 10, self.y + 5))

        text = font.render("Producing: " + "+" + str(self.producing1) + " / " + str(self.producing2), True, BLACK)
        win.blit(text, (
            self.x + 10, self.y + 25))

        text = font.render("Price: " + str(self.costs), True, BLACK)
        win.blit(text, (
            self.x + 10, self.y + 45))
        font = pygame.font.SysFont('comicsans', 50)
        text = font.render(str(self.number), True, BLACK)
        win.blit(text, (
            self.x + self.width - 60, self.y + 17))

    def isOver(self, position):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                return True
        return False


# Buttons for automatic clicks
button1 = Button(WIDTH // 2 + 2, 3, WIDTH // 2, 65, 'get out of bed', 0.1, 0, 15)
button2 = Button(WIDTH // 2 + 2, 3 + 65, WIDTH // 2, 65, 'do a squat', 0.5, 0, 100)
button3 = Button(WIDTH // 2 + 2, 3 + 65 * 2, WIDTH // 2, 65, 'to jump', 4, 0, 500)
button4 = Button(WIDTH // 2 + 2, 3 + 65 * 3, WIDTH // 2, 65, 'stand at the bar', 10, 0, 3000)
button5 = Button(WIDTH // 2 + 2, 3 + 65 * 4, WIDTH // 2, 65, '5 minutes training', 40, 0, 10000)
button6 = Button(WIDTH // 2 + 2, 3 + 65 * 5, WIDTH // 2, 65, 'exercise bike', 100, 0, 40000)
button7 = Button(WIDTH // 2 + 2, 3 + 65 * 6, WIDTH // 2, 65, 'treadmill', 400, 0, 200000)
button8 = Button(WIDTH // 2 + 2, 3 + 65 * 7, WIDTH // 2, 65, '1 hour training', 6666, 0, 1666666)
button9 = Button(WIDTH // 2 + 2, 3 + 65 * 8, WIDTH // 2, 65, '2 hours training', 98765, 0, 141975807)
button10 = Button(WIDTH // 2 + 2, 3 + 65 * 9, WIDTH // 2, 61, 'magic diet pills', 12123123, 0, 3999999999)

Buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10]


def Field(x):
    surf_left = pygame.Surface((WIDTH // 2, HEIGHT))
    surf_left.fill((254, 210, 214))
    screen.blit(surf_left, (0, 0))

    if x:
        for k in range(10):
            Buttons[k].draw(screen, BLACK)

    font = pygame.font.Font(None, 36)
    text = font.render("Clicks:", True, BLACK)
    screen.blit(text, (WIDTH // 4 - 50, HEIGHT // 2 - 100))

    text = font.render("Produce:", True, BLACK)
    screen.blit(text, (WIDTH // 4 - 50, 550))

    font = pygame.font.Font(None, 40)
    text = font.render(str(num_of_clicks), True, BLACK)
    screen.blit(text, (WIDTH // 4 - 50, HEIGHT // 2 - 70))
    text = font.render(str(Produce), True, BLACK)
    screen.blit(text, (WIDTH // 4 - 50, 580))

    man_surf = pygame.image.load('secondscreen.jpg')
    man_rect = sport_surf.get_rect(bottomright=(550, 820))
    screen.blit(man_surf, man_rect)

    font = pygame.font.Font(None, 30)
    text = font.render(
        "To lose a calorie, press the space bar.",
        True, RED)
    screen.blit(text, (27, 20))
    text = font.render("You can also buy automatic clicks", True, BLACK)
    screen.blit(text, (27, 70))

    text = font.render("There you can also see their price,", True, BLACK)
    screen.blit(text, (27, 95))

    text = font.render("how much they will add", True, BLACK)
    screen.blit(text, (27, 120))

    text = font.render("and how much they already adding", True, BLACK)
    screen.blit(text, (27, 145))

    text = font.render("Automatic clicks adds every second", True, BLUE)
    screen.blit(text, (27, 180))


second = 0
while True:
    pygame.display.update()
    for i in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                num_of_clicks += 1
                if num_of_clicks == 0:
                    Field(True)
                else:
                    Field(False)
        elif i.type == pygame.MOUSEBUTTONDOWN:
            for j in range(10):
                if Buttons[j].isOver(pos) and num_of_clicks - Buttons[j].costs >= 0:
                    num_of_clicks = round(num_of_clicks - Buttons[j].costs, 3)
                    Buttons[j].producing2 = round(Buttons[j].producing1 + Buttons[j].producing2, 2)
                    Buttons[j].costs = round(Buttons[j].costs * 1.15)
                    Buttons[j].number += 1
                    Buttons[j].draw(screen, BLACK)
                    Produce = round(Produce + Buttons[j].producing1, 2)
        elif i.type == pygame.MOUSEMOTION and num_of_clicks != -1:
            for j in range(10):
                if Buttons[j].isOver(pos):
                    Buttons[j].color = (254, 218, 177)
                else:
                    Buttons[j].color = (254, 202, 177)
                Buttons[j].draw(screen, BLACK)

    ticks = pygame.time.get_ticks()
    seconds = int(ticks / 1000)
    if seconds > second:
        second = seconds
        if num_of_clicks != -1:
            Field(False)
        for j in range(10):
            num_of_clicks = round(num_of_clicks + Buttons[j].producing2, 3)

    pygame.display.flip()
    clock.tick(60)
