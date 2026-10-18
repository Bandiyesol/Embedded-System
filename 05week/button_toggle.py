from gpiozero import Button, LED  
from signal import pause         

button = Button(17, bounce_time=0.1)
led = LED(18)                     

def toggle_led():                
    led.toggle()                 
    state = "ON" if led.is_lit else "OFF"   
    print(f"LED={state}")      

button.when_pressed = toggle_led  

try:
    pause()              
finally:              
    led.off()                 
    button.close()            
    led.close()               