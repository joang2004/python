from easyinput import read
import arcade
import random

arcade.open_window(600, 600, "Drawing Example")


arcade.set_background_color(arcade.csscolor.SKY_BLUE)


arcade.start_render()
def entrada(nombre):
    for i in range(nombre):
        escala =read(float)
        px= read(float)
        py= read(float)
        arbre(px,py,escala)
def color():
    return [random.randrange(0,20),random.randrange(100,255),random.randrange(0,20)]

def arbre(px, py, escala):
    #Estructura bàsica de l'arbre
    arcade.draw_lrtb_rectangle_filled(px, (30*escala)+px, (80*escala)+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled((15*escala)+px, (80*escala)+py, (40*escala), color())
    #Detalls de les fulles
    
    arcade.draw_circle_filled((40*escala)+px, (70*escala)+py, (24*escala), color())
    
    arcade.draw_circle_filled((35*escala)+px, (95*escala)+py, (30*escala), color())
    arcade.draw_circle_filled(px-(10*escala), (65*escala)+py, (24*escala), color())
    arcade.draw_circle_filled(px-(10*escala), (95*escala)+py, (30*escala), color())
    arcade.draw_circle_filled(px+(15*escala), (105*escala)+py, (30*escala), color())


arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

nombre_arbre= read(int)
entrada(nombre_arbre)
arcade.finish_render()


arcade.run()