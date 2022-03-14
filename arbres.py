

import arcade

arcade.open_window(600, 600, "Drawing Example")


arcade.set_background_color(arcade.csscolor.SKY_BLUE)


arcade.start_render()

def arbre(px,py, multiple):
    #Estructura bàsica de l'arbre
    arcade.draw_lrtb_rectangle_filled(px, (30*multiple)+px, (80*multiple)+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled((15*multiple)+px, (80*multiple)+py, (40*multiple), arcade.csscolor.DARK_GREEN)
    
    #Detalls de les fulles
    
    arcade.draw_circle_filled((40*multiple)+px, (70*multiple)+py, (24*multiple), arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled((35*multiple)+px, (95*multiple)+py, (30*multiple), arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(px-(10*multiple), (65*multiple)+py, (24*multiple), arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(px-(10*multiple), (95*multiple)+py, (30*multiple), arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(px+(15*multiple), (105*multiple)+py, (30*multiple), arcade.csscolor.DARK_GREEN)


arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arbre(300,300,0.5)
arcade.finish_render()


arcade.run()