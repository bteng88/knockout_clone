'''
sample pyglet application with stuff
'''
import os
import pyglet

# Create a window
window = pyglet.window.Window(width=800,
                              height=700,
                              caption="Game Board")

# Get path from current directory to audio file
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_file_path = os.path.join(current_dir, '..','assets', 'audio',
                               'music', 'a-promise(chosic.com).mp3')

# Play music using the path
music = pyglet.media.load(audio_file_path)
music.play()

# Make label
# Get path to font file
label = pyglet.text.Label("Label over here",
                          font_name='Calibri',
                          font_size = 18,
                          x=window.width//2 - 300,
                          y=window.height//2 + 300,
                          anchor_x='center',
                          anchor_y='center')


# Load icons-play/retry in the top right
quit_file_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'icons', 'quit.png')
retry_file_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'icons', 'retry.png')
quit_icon = pyglet.image.load(quit_file_path)
retry_icon = pyglet.image.load(retry_file_path)

# tmp to see if sprites load in/what they look like
earth_ball_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'sprites', 'earth.png')
soccer_ball_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'sprites',
                                'soccer_ball.png')
earth_ball_image = pyglet.image.load(earth_ball_path)
soccer_ball_image = pyglet.image.load(soccer_ball_path)
earth_sprite = pyglet.sprite.Sprite(earth_ball_image, 400, 300)
earth_sprite.scale = .093
soccer_ball_sprite = pyglet.sprite.Sprite(soccer_ball_image, 300, 300)
soccer_ball_sprite.scale = .7

class Platform:
    '''
    This class creates the platform for the game,
    contains the methods,create, shrink, update, and render
    '''
    def __init__(self, x, y, width, height):
        '''
        initializes the neccesarry parameters for platform creation
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = 1.0  # Initial scale
        self.image = self.create_image()

    def create_image(self):
        '''
        Method to create the image of the platform
        '''
        image = (pyglet.image
                .SolidColorImagePattern((255, 255,255, 255))
                .create_image(self.width, self.height))
        return image

    def render(self):
        '''
        Renders the platform onto the screen
        '''
        self.image.blit(self.x, self.y, width=self.width*self.scale, height=self.height*self.scale)

    def shrink(self):
        '''
        Method to shrink the platform, like the knockout game
        TODO: make shrink from all directions, instead of just topright corner
        '''
        if self.scale >= 0.5:  # Minimum scale threshold
            self.scale -= 0.00005
            return True  # Adjust shrinking rate as needed
        return False

    def update(self, dt):
        '''
        Constantly updates the size of the platform
        by continuously calling the shrink method
        '''
        if self.shrink():
            self.shrink()

# initialize platform
platform = Platform(x=window.width//2 - (.25 * 900), y=window.height//2 - (.25 * 700), width=900, height=700)

# background
background_image_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'backgrounds',
                                     'water.jpg')
background_image = pyglet.image.load(background_image_path)
background_sprite = pyglet.sprite.Sprite(background_image)

# class SpriteBall:
#     '''
#     Class to create the sprites and place
#     them on the platform with no overlaps
#     '''
#     def __init__(self, x, y, radius, sprite):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sprite = sprite

        

    # def move(self):
    #     pass

    # def collision(self):
    #     pass



# Define the update function (if needed)
def update(dt):
    '''
    Handles all updates for the game
    '''
    platform.update(dt)
    #pass

# Set up the update function (if needed)
pyglet.clock.schedule(update)

# Create sprite object
#sprite = pyglet.sprite.Sprite(sprite_image, x=400, y=300)

# Define the draw function
@window.event
def on_draw():
    '''
    draws the sprites for the two players
    '''
    window.clear()
    # Draw graphics
    background_sprite.draw()
    platform.render()
    label.draw()
    retry_icon.blit(600, 600)
    quit_icon.blit(700, 600)
    earth_sprite.draw()
    soccer_ball_sprite.draw()
    earth_sprite.event


if __name__ == '__main__':
    pyglet.app.run()
