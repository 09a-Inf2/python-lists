import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#globale Variablen
WIDTH = 300
HEIGHT = 200
ball_radius = 50
ball_color = "red"

# Handler für keydown 
def keydown(key):
  pass


# Handler zum Zeichnen des Kreises
def draw(canvas):
  pass




# Erzeuge frame und registriere event handler

frame = simplegui.create_frame("Change Color", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Starte die Frame-Animation
frame.start()








