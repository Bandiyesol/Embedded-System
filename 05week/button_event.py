from gpiozero import Button  
from signal import pause  

button = Button(17)           

def pressed():            
    print("PRESSED")

def released():               
    print("RELEASED")

button.when_pressed = pressed      
button.when_released = released   

try:
    pause()                  
finally:                      
    button.close()           