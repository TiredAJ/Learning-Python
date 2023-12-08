import sys, time, keyboard

Val = 0

def PrintVal():
    sys.stdout.flush()
    print("\r" + '{0:010b}'.format(Val) + f"   {Val}", end='')

PrintVal()

while True :
    event = keyboard.read_event();
    
    if (Val > 0) and (event.event_type == keyboard.KEY_DOWN) and (event.name == "backspace"):
        Val -= 1
        PrintVal()
    elif (Val < 1023) and (event.event_type == keyboard.KEY_DOWN) and (event.name == "enter"):
            Val += 1
            PrintVal()
