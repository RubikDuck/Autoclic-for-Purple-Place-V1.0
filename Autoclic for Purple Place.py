import mouse
import time
import keyboard

delay=4

def sexy_move():
    mouse.move(1185, 328, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(958, 152, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(1050, 261, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(1143, 354, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(1238, 463, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(1322, 549, absolute=True, duration=0.2)
    mouse.click('left')

    mouse.move(698, 597, absolute=True, duration=0.2)
    mouse.click('left')
    
    mouse.move(42, 120, absolute=True, duration=0.2)
    mouse.click('left')

time.sleep(delay)

for _ in range(3125):
    sexy_move()

    if keyboard.is_pressed('q'):
        print("The script has stopped")
        break

exit()
