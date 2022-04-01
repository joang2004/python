import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
def colisio(a,b):
    #de les posicions i el radi, retorni si hi ha colisió
    if abs(a.position_x-b.position_x)<(a.radius+b.radius) :
        return True
    else:
        return False

"""
class Arbre:
    #Aquesta calse pinta un arbre
    def __init__(self, px,py,escala):
        self.px=px
        self.py=py
        self.escala =escala
        self.color =arcade.csscolor.GREEN
    def draw(self):
        px =self.px
        py=self.py
        escala=self.escala
        #Estructura bàsica de l'arbre
        arcade.draw_lrtb_rectangle_filled(px, (30*escala)+px, (80*escala)+py, py, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled((15*escala)+px, (80*escala)+py, (40*escala), arcade.csscolor.DARK_GREEN)
    #Detalls de les fulles
    
        arcade.draw_circle_filled((40*escala)+px, (70*escala)+py, (24*escala), self.color)
    
        arcade.draw_circle_filled((35*escala)+px, (95*escala)+py, (30*escala), self.color)
        arcade.draw_circle_filled(px-(10*escala), (65*escala)+py, (24*escala), self.color)
        arcade.draw_circle_filled(px-(10*escala), (95*escala)+py, (30*escala), self.color)
        arcade.draw_circle_filled(px+(15*escala), (105*escala)+py, (30*escala), self.color)

    def canvia(self):
        self.color = arcade.csscolor.YELLOW

"""
class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1
    def xoquen(self):
        self.change_x *= -1
    


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

                # Attributes to store where our ball is
        self.ball = Ball(50, 150, 3, 0, 20, arcade.color.AUBURN)
        self.ball2 = Ball(300, 150, 1, 0, 50, arcade.color.BLUE)

     #   self.arbre =Arbre(200, 200 ,0.5)
 
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()
      #  self.arbre.draw()

    def update(self, delta_time):
        if colisio(self.ball,self.ball2) ==True:
            print("a")
            self.ball.xoquen()
            self.ball2.xoquen()  
        self.ball.update()
        self.ball2.update()
        
        
        
        # self.arbre.canvia()
def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()