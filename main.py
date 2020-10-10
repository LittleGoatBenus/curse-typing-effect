import curses # curses library
from pygame import mixer # allows sound effect, delete this if you dont want it 


effect = mixer.Sound('key.wav') #importing the typing sound effect 

words = "your words." # change this to what ever you want the typing effect to say 


            curses.curs_set(0)
            for char in words:
                curses.curs_set(1) # sets the curses to be viewed delete this if you dont want it 
                
                time.sleep(0.3) # change this time according to how fast you need your typing to be 

                stdscr.addch(char)
                
                effect.play() # sound effect delete it if you dont want it
                
                stdscr.refresh() # refresh screen 
