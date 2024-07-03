import pyglet 
import random
import os
from math import sqrt

# Create a window
window = pyglet.window.Window(width = 800, height = 600, caption="Game Board")

# Get path from current directory to audio file
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_file_path = os.path.join(current_dir, '..','assets', 'audio',
                               'music', 'a-promise(chosic.com).mp3')

# Play music using the path
music = pyglet.media.load(audio_file_path)
music.play()

# Make label
# Get path to font file
label = pyglet.text.Label("Label over here", font_name='Comic Sans MS', font_size = 18, 
                          x=window.width//2 - 300, y=window.height//2 + 270, anchor_x='center', anchor_y='center')

# Load icons-play/retry in the top right
quit_file_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'icons', 'quit.png')
retry_file_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'icons', 'retry.png')
quit_icon = pyglet.image.load(quit_file_path)
retry_icon = pyglet.image.load(retry_file_path)

# Main ball sprites to play with
earth_ball_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'sprites', 'earth.png')
soccer_ball_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'sprites',
                                'soccer_ball.png')
earth_ball_image = pyglet.image.load(earth_ball_path)
soccer_ball_image = pyglet.image.load(soccer_ball_path)
#earth_sprite = pyglet.sprite.Sprite(earth_ball_image, 300, 300)
#earth_sprite.scale = 0.14
#soccer_ball_sprite = pyglet.sprite.Sprite(soccer_ball_image, 200, 200)

# Function to create the balls at random locations
def knockout_balls(num_balls, ball_image, scale_factor):
    balls = []
    for i in range(num_balls):
        # NEED TO CHANGE TO CENTER, Both radius 26, ewdith = 52 = swidth, eheight = 51, sheight = 50
        ball_x = random.randint(100, 600) # Bound in platform x position & width
        ball_y = random.randint(125, 350) 
        new_ball = pyglet.sprite.Sprite(ball_image, ball_x, ball_y)
        new_ball.scale = scale_factor
        new_ball.center_x = ball_x + 26 # Center position is right of relative x
        new_ball.center_y = ball_y + 26 # Center position is right of relative y
        balls.append(new_ball)
    return balls

earth_balls = knockout_balls(4, earth_ball_image, 0.07) 
soccer_ball_balls = knockout_balls(4, soccer_ball_image, .53)
all_balls = earth_balls + soccer_ball_balls

# Utility function that returns distance between two balls
def distance(ball1, ball2):
    return sqrt((ball1.center_x - ball2.center_y) ** 2 + (ball1.center_y - ball2.center_y) ** 2)

# Function to reposition balls if they are too close to one another
def reposition_balls(all_balls):
    for index, ball in enumerate(all_balls):
        print(index)
        valid_position = False
        while not valid_position:
            valid_position = True
            for i in range(index):
                if all_balls[i] != ball and distance(ball, all_balls[i]) < 55: 
                    ball.x = random.randint(100, 600) # Bound in platform x position & width
                    ball.y = random.randint(125, 350)
                    ball.center_x = ball.x + 26 # Center position is right of relative x
                    ball.center_y = ball.y + 26
                    valid_position = False
                    print("new position made")
                    break # Reset while loop so it checks from the beginning again
    
reposition_balls(all_balls)

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


    def center_platform(self):
        self.x = self.x - (self.width // 2)
        self.y = self.y - (self.height // 2) 


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
        #self.shrink()
        pass


# initialize platform in the middle
platform = Platform(x=window.width//2, y=window.height//2, width=600, height=350)
Platform.center_platform(platform)

# background
background_image_path = os.path.join(current_dir, '..', 'assets', 'graphics', 'backgrounds',
                                     'water.jpg')
background_image = pyglet.image.load(background_image_path)
background_sprite = pyglet.sprite.Sprite(background_image)


'''docstring:Set anchor point of image to center instead of lower left''' 
'''def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.width // 2
'''


# Define the update function (if needed)
def update(dt):
    '''
    Handles all updates for the game
    '''
    platform.update(dt)
    #pass


# Set up the update function (if needed)
pyglet.clock.schedule(update)


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
    retry_icon.blit(600,500)
    quit_icon.blit(700,500)
    platform.render()
    #earth_sprite.draw()
    #soccer_ball_sprite.draw()
    for earth in earth_balls:
        earth.draw()
    for soccer_ball in soccer_ball_balls:
        soccer_ball.draw()
    
    

# Run the application
#def main() :
pyglet.app.run()


'''if __name__ == "__main__":
   main()
'''
