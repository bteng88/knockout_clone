import pyglet
import os

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Game Board")

''' need to adjust os path- use relative paths based on root directory to make more flexible
    this is for icons/spirtes...'''
# Get path from current directory to audio file
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_file_path = os.path.join(current_dir, '..', 'assets', 'audio', 'music', 'a-promise(chosic.com).mp3')

# Play music using the path
music = pyglet.media.load(audio_file_path)
music.play()

# Make label
# Get path to font file
label = pyglet.text.Label("Label over here", font_name='Comic Sans MS', font_size = 18, 
                          x=window.width//2 - 300, y=window.height//2 + 250, anchor_x='center', anchor_y='center')

# Load icons-play/retry in the top right
quit_file_path = 'assets/graphics/icons/quit.png'
retry_file_path = 'assets/graphics/icons/retry.png'
quit_icon = pyglet.image.load(quit_file_path)
retry_icon = pyglet.image.load(retry_file_path)

# tmp to see if sprites load in/what they look like
earth_ball_path = 'assets/graphics/sprites/earth.png'
soccer_ball_path = 'assets/graphics/sprites/soccer_ball.png'
earth_ball_image = pyglet.image.load(earth_ball_path)
soccer_ball_image = pyglet.image.load(soccer_ball_path)
earth_sprite = pyglet.sprite.Sprite(earth_ball_image, 300, 300,)
earth_sprite.scale = 0.14
soccer_ball_sprite = pyglet.sprite.Sprite(soccer_ball_image, 200, 200)

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = 1.0  # Initial scale
        self.image = self.create_image()

    def create_image(self):
        image = pyglet.image.SolidColorImagePattern((255, 255, 255, 255)).create_image(self.width, self.height)
        return image

    def render(self):
        self.image.blit(self.x, self.y, width=self.width*self.scale, height=self.height*self.scale)

    def shrink(self):
        if self.scale > 0.5:  # Minimum scale threshold
            self.scale -= 0.005  # Adjust shrinking rate as needed

    def update(self, dt):
        self.shrink()

# initialize platform
platform = Platform(x=window.width//2, y=window.height//2, width=600, height=350)

# background
background_image_path = 'assets/graphics/backgrounds/water.jpg'
background_image = pyglet.image.load(background_image_path)
background_sprite = pyglet.sprite.Sprite(background_image)

'''class Circle:
    # x,y will be coordinates, radius is used to detect collisions
    def __init__(self, x, y, radius, ball_file):
        # Load the sprite PNG file
        self.ball_image = pyglet.image.load(ball_file)

        # Create a sprite object from the loaded image
        self.ball_sprite = pyglet.sprite.Sprite(self.ball_image, x_pos = x, y_pos= y)
'''


# Define the update function (if needed)
def update(dt):
    platform.update(dt)
    pass

# Set up the update function (if needed)
pyglet.clock.schedule(update)

# Create sprite object
#sprite = pyglet.sprite.Sprite(sprite_image, x=400, y=300)

# Define the draw function
@window.event
def on_draw():
    window.clear()
    # Draw graphics 
    background_sprite.draw()
    label.draw()
    retry_icon.blit(600,500)
    quit_icon.blit(700,500)
    earth_sprite.draw()
    soccer_ball_sprite.draw()
    platform.render()
    



# Run the application
#def main() :
pyglet.app.run()


'''if __name__ == "__main__":
   main()
'''