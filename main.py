#Game introduction, introduce story and player mechanics.
print('''  ..  ...  ...  ...  ..      .        ..  ....  ...
 ...  .... .... .....     .%/\      .. ....  .....  .....  .
.  ...  ...  ... ..     .%./  &.     ....  ......  ....  ...
..  ....  ..  ...     .%**/     \        .....  .....  ....
....  ....  ..      .%***/       &.     .....  .....  ...  .
......  .... .    .%.***/  .d99b_  \      . ......  ... ....
  .......       .%*****/ -'      `'.&.     .....  ... .....
..     ..     .%******/  ._."""'~::,  \      . ... .....   .
.......     .%*******/._'` .'"^':,  :.,&.     . ....  .....
...       .%********/',_-^{  ( )  }    :.\       ........ ..
  ..     .%*********/%^    '.     .'     ;.&.     .  ... ....
.     .%**********/;        ".,."        ;#.\     .  . .....
     .%***********/  ~'.,,.          ,.-'^    &.     . ... ..
   .%************/         ""-.,.-""~           \     . . ..
 .%*************/                                &.     .. ..
%**************/                                   \     ...
        WELCOME TO THE HUNT FOR THE ALL-SEEING EYE!''')
print("\nThe mechanics of this game are based off simple either-or questions, with your choice determining the outcome of your adventure\n")

#GAME START: -- CHOICE NUMBER 1 --
choice_number1 = input('''You have just discovered the secret door to the infamous All-Seeing Eye Pyramid!
After entering the pyramid you have the option to go left, or go right. Type "left" or "right" below!

''')

if choice_number1.lower() == "left":
    print('''\nAs you contimplate what could possibly be waiting for you down the right pathway, the path to your left calls out to you...
You realize this isn't a gut feeling, but something more, as if it's your destiny waiting for you down the left pathway.
The echoing of your footsteps, bouncing off these ancient walls that have been most likely unseen by human eyes for thousands and thousands
of years, builds a sense of dread inside of you, increasing more and more with each step. Until a sound very different to the ones caused
by your hiking boots clunking on the limestone floor cracks through, snapping you out of your trance. Next thing you know, you're
submerged in water, stagnent and dark. You have fallen through what must be a trap! And you soon realize that you're not the only
living thing floating in this abyss.\n\n''')
    
    input('''''')

else: 
    print('''\nYou glance towards the left, it differs in no way from the path to your right, the choice to be made at this point is
akin to the flip of a coin. Your mind stirs to make a decision for only a few seconds before taking your first step towards the
right... The second step follows, then the third... You set your right foot down, and raise the left not knowing that your
life will be stripped from you before you can even plant your lifted foot... You have triggered a pressure plate rigged to a 
vicious and crude wall of spikes made to impale and only that.
          
GAME OVER! Try again...''')