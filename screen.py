import arcade
from models import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
class HowToSurvive(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.spot_sprite = ModelSprite("pacman.png", model=self.world.spot)
        self.big = ModelSprite("bigrectangle.gif", model=self.world.big)
        self.build_recx_and_recy()

    def build_recx_and_recy(self):
        recx = []
        recy = []
        for i in self.world.recx_list:
            recx.append(ModelSprite("rectanglex.jpg", model=i))
        for j in self.world.recy_list:
            recy.append(ModelSprite("rectangley.jpg", model=j))
        self.recx = recx
        self.recy = recy
                                 
    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Time: "+str(self.world.all_time),self.world.width-180,self.world.height-30,arcade.color.BLACK,30)
        if self.world.state == self.world.STATE_FROZEN:
            arcade.draw_text("Press any key to start.", 210, 400,arcade.color.BLACK, 30)
            arcade.draw_text("Use key W A S D to move.", 190, 200, arcade.color.BLACK, 30)
            arcade.draw_text("If you hit block you die.", 205, 150, arcade.color.BLACK, 30)
            arcade.draw_text("If you go out of screen you die too!!", 110, 100, arcade.color.BLACK, 30)

        self.spot_sprite.draw()

        if self.world.state != self.world.STATE_RESTART:
            self.draw_rec()
            self.big.draw()

        if self.world.state == self.world.STATE_DEAD:
            score = self.high_score()
            arcade.draw_text("You Can Survive",200,350,arcade.color.RED_DEVIL,50)
            arcade.draw_text(self.world.all_time,380,260,arcade.color.BLACK,60)
            arcade.draw_text("s.", 460, 260, arcade.color.BLACK, 30)
            arcade.draw_text("Press any key to restart.", 210, 200, arcade.color.BLACK, 30)
            arcade.draw_text(f"High score: {score} s. ", 260, 150, arcade.color.BLACK, 30)

    def high_score(self):
        file = open("score.txt").readline()
        if file == "" or int(file) < int(self.world.all_time):
            with open("score.txt", "w") as file:
                file.write(self.world.all_time)
        with open("score.txt", "r") as file:
            score = file.readline()
        return score

    def restart(self):
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.spot_sprite = ModelSprite("pacman.png", model=self.world.spot)
        self.big = ModelSprite("bigrectangle.gif", model=self.world.big)
        self.build_recx_and_recy()

    def draw_rec(self):
        for block in self.recx:
            block.draw()
        for block in self.recy:
            block.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
        if self.world.state == World.STATE_RESTART:
            self.restart()
        if not self.world.is_dead():
            self.world.start()


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()


def main():
    window = HowToSurvive(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 

if __name__ == '__main__':
    main()
