
import arcade
import random

def main():
    arcade.open_window(600, 600, "Drawing Example")
    arcade.set_background_color((0,150,255))
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0,600,200,0, (225,225,225))

    ninot(300,300)
    arcade.finish_render()
    arcade.run()

def ninot(x,y):
    #Estructura Basica
    arcade.draw_circle_filled(x,y ,60,(255,255,255))
    arcade.draw_circle_filled(x, y+50, 50,(255,255,255))
    arcade.draw_circle_filled(x,y+100,40, (255,255,255))

    #Ulls
    arcade.draw_circle_filled(x-12,y+115,5, (0,0,0))
    arcade.draw_circle_filled(x+12,y+115,5, (0,0,0))
    #Botons
    arcade.draw_lrtb_rectangle_filled(x-10,x+10,y+100,y+95,(0,0,0))

main()
