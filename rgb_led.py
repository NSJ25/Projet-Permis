from gpiozero import RGBLED, Button
from time import sleep

# Création de l'objet LED RGB et du bouton
rgb_led = RGBLED(red=17, green=27, blue=22)
bouton = Button(12, bounce_time=0.2)  # Bouton sur le pin GPIO 12

# Fonction pour définir une couleur avec des valeurs RGB (0-1)
def definir_couleur(rouge, vert, bleu):
    rgb_led.color = (rouge, vert, bleu)


# Variable pour suivre l'état de la LED
led_allumee = False

# Fonction pour gérer l'appui sur le bouton
def toggle_led():
    global led_allumee
    if led_allumee:
        rgb_led.off()
        led_allumee = False
    else:
        rgb_led.on()
        led_allumee = True

# Associer la fonction au bouton
bouton.when_pressed = toggle_led

while True:
        # Rouge pur
        definir_couleur(1, 0, 0)
        sleep(0.5)
        
        # Vert pur
        definir_couleur(0, 1, 0)
        sleep(0.5)
        
        # Bleu pur
        definir_couleur(0, 0, 1)
        sleep(0.5)
        
        # Jaune (rouge + vert)
        definir_couleur(1, 1, 0)
        sleep(0.5)
        
        # Magenta (rouge + bleu)
        definir_couleur(1, 0, 1)
        sleep(0.5)
        
        # Cyan (vert + bleu)
        definir_couleur(0, 1, 1)
        sleep(0.5)
        
        # Blanc (toutes les couleurs)
        definir_couleur(1, 1, 1)
        sleep(0.5)


