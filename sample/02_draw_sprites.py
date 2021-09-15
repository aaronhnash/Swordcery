"""
Platformer Game
"""
import arcade


#Made using dictionary references instead of lists

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.


        self.sprites = {}
        self.sprites["coins"] = None
        self.sprites["walls"] = None
        self.sprites["player"] = None

        #self.coin_list = None
        #self.wall_list = None
        #self.player_list = None

        # Separate variable that holds the player sprite
    
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        #self.player_list = arcade.SpriteList()
        #self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        #self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.sprites["player"] = arcade.SpriteList()
        self.sprites["walls"] = arcade.SpriteList()
        self.sprites["coins"] = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 
                                           CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.sprites["player"].append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.sprites["walls"].append(wall)
            #^ this is the same as a list

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[256, 96],
                           [512, 96],
                           [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.sprites["walls"].append(wall)


# dictionary = "key" : entry
# self.sprites["key"] -> [list]


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        #self.wall_list.draw()
        #self.coin_list.draw()
        #self.player_list.draw()
        for sprite_list in self.sprites.values():
            sprite_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()