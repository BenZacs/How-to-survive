import arcade.key
from random import randint
from time import time
MOVEMENT_SPEED = 5
DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
REC_SPEED1 = [4, 6, 8]
REC_SPEED2 = [4, 6, 7, 8]

KEY_MAP = { arcade.key.W: DIR_UP,
            arcade.key.S: DIR_DOWN,
            arcade.key.A: DIR_LEFT,
            arcade.key.D: DIR_RIGHT}
 
DIR_OFFSETS = { DIR_STILL: (0, 0),
                DIR_UP: (0, 1),
                DIR_RIGHT: (1, 0),
                DIR_DOWN: (0, -1),
                DIR_LEFT: (-1, 0)}


class Spot:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.next_direction = DIR_STILL
 
    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]

    def update(self, delta):
        self.direction = self.next_direction
        self.move(self.direction)


class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2
    STATE_DEAD = 3
    STATE_RESTART = 4

    def __init__(self, width, height):
        self.state = World.STATE_FROZEN
        self.width = width
        self.height = height
        self.start_time = 0
        self.all_time = 0
        self.spot = Spot(self, 400, 300)
        self.big = Big(self, randint(200, 600), 900, 10)
        self.build_recx_and_recy()

    def build_recx_and_recy(self):
        recx = []
        recy = []
        for i in REC_SPEED1:
            recx.append(Rec1(self, 880, randint(1, 600), i))
        for i in REC_SPEED2:
            recy.append(Rec2(self, randint(1, 800), 680, i))
        self.recx_list = recx
        self.recy_list = recy
        
    def on_key_press(self, key, key_modifiers):
        if key in KEY_MAP:
            self.spot.next_direction = KEY_MAP[key]
        if self.state == self.STATE_DEAD:
            self.restart()

    def update(self, delta):
        if self.state in [World.STATE_FROZEN, World.STATE_DEAD,World.STATE_RESTART]:
            return

        self.spot.update(delta)
        if self.spot.x > 807 or self.spot.y > 607 or self.spot.x < -13 or self.spot.y < -13:
            self.die()

        self.check_recx()
        self.check_recy()
        self.check_big()

        if self.state == World.STATE_STARTED:
            self.all_time = f"{time() - self.start_time:.0f}"

    def check_recx(self):
        for i in self.recx_list:
            i.move()
            if i.x <= -80:
                i.x = 880
                i.y = randint(100, 500)
            if hit_x(self.spot.x, self.spot.y, i.x, i.y) is True:
                self.die()

    def check_recy(self):
        for j in self.recy_list:
            j.move()
            if j.y <= -80:
                j.y = 680
                j.x = randint(1, 800)
            if hit_y(self.spot.x, self.spot.y, j.x, j.y) is True:
                self.die()

    def check_big(self):
        if int(self.all_time) % 10 == 0 and int(self.all_time) > 0:
            if self.big.start is False:
                self.big.x = randint(self.spot.x - 50, self.spot.x + 50)
            self.big.start = True
        if self.big.start is True:
            self.big.move()
        if self.big.y <= -300:
            self.big.start = False
            self.big.y = 900
            self.big.x = randint(1, 800)
        if hit_big(self.spot.x, self.spot.y, self.big.x, self.big.y) is True:
            self.die()

    def start(self):
        self.state = World.STATE_STARTED
        if self.start_time == 0:
            self.start_time = time()

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def die(self):
        self.state = World.STATE_DEAD

    def is_dead(self):
        return self.state == World.STATE_DEAD

    def restart(self):
        self.state = World.STATE_RESTART


class Rec1:
    def __init__(self, world, x, y, speed):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x -= self.speed


class Rec2:
    def __init__(self, world, x, y, speed):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y -= self.speed


class Big:
    def __init__(self, world, x, y, speed):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.start = False

    def move(self):
        self.y -= self.speed


def hit_x(player_x, player_y, rec_x, rec_y):
    if rec_x - 68 < player_x < rec_x + 68 and rec_y - 30 < player_y < rec_y + 30:
        return True
    else:
        return False


def hit_y(player_x, player_y, rec_x, rec_y):
    if rec_x - 30 < player_x < rec_x + 30 and rec_y - 68 < player_y < rec_y + 68:
        return True
    else:
        return False


def hit_big(player_x, player_y, rec_x, rec_y):
    if rec_x - 100 < player_x < rec_x + 100 and rec_y - 175 < player_y < rec_y + 175:
        return True
    else:
        return False
