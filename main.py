# Game introduction, introduce story and player mechanics.
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

# GAME START: -- CHOICE NUMBER 1 --
choice_number1 = input('''You have just discovered the secret door to the infamous All-Seeing Eye Pyramid!
After entering the pyramid you have the option to go left, or go right.\n 
Type "left" or "right" below!\n''')

# CHOICE NUMBER 1 -- Correct Option
if choice_number1.lower() == "left":
    print('''\nAs you contimplate what could possibly be waiting for you down the right pathway, the path to your left calls out to you...
You realize this isn't a gut feeling, but something more, as if it's your destiny waiting for you down the left pathway.
The echoing of your footsteps, bouncing off these ancient walls that have been most likely unseen by human eyes for thousands and thousands
of years, builds a sense of dread inside of you, increasing more and more with each step. Until a sound very different to the ones caused
by your hiking boots clunking on the limestone floor cracks through, snapping you out of your trance. Next thing you know, you're
submerged in water, stagnent and dark. You have fallen through what must be a trap! And you soon realize that you're not the only
living thing floating in this abyss.\n\n''')
    
    # -- CHOICE NUMBER 2 --
    choice_number2 = input('''All that can run through your head is a mantra of "STAY. STILL!!!. But every ounce of fight or flight programming in your
human code is pushing your body to move in an attempt to get away from whatever it is swimming alongside you in this murky
water. Your two choices, simple as they are in terms of execution, are choices of life and death. You can wait and try to hold your breath
in hopes that the unknown creature swims away, or attempt to swim and flee before the creature is aware of your presence.\n
Type "swim" or "wait" below!\n''')
    
    # CHOICE NUMBER 2 -- Correct Option
    if choice_number2.lower() == "wait":
        print('''Every bit of you wants to start using your limbs to swim away from whatever it is slithering around you. Not only is
the creature starting to swim closer to you, even brushing up against your legs a few times, you also begin to feel your head swimming
from a lack of oxygen. Bubbles escape from the slit of your mouth, your lungs take on a bit of water making you choke and your panic 
increase right up to its very limit. And even though the visibilty beneath the water is non-existent, you can tell you're beginning to
blackout... You decide to throw caution to the wind and rise for maybe the last gasp of breath you'll ever take, kicking out with your
feet you feel one of them bumping into something solid that gives with the contact. Almost right away the water swooshes all around you
with the force of an oceans current. You lose all sense of direction. Not knowing which way to swim for air, all you can do is hope the
ordeal ends quick... Next thing you're aware of is water erupting from your lungs and out your mouth as you're sprawled out on your back
entirely unaware of where you are. The first sound that grabs your attention is a monsterous shriek to which you raise your head to see
where the source of this horrid sound is originiating from. What meets your eyes can only be described as hell in the form of some sort
of aquatic beast, writhing and flopping before it's flushed entirely down a drain with the rest of the water that almost ended your life.
\n\n''')
        
        # -- CHOICE NUMBER 3 --
        choice_number3 = input('''Nothing but the awareness of what would have happened if that monster got it's jaws around you fills your head, until that all but
known but still familiar feeling washes away your fear. In its place swells the same sense of destiny that you first felt when
initially entering the pyramid. This time though, it's accompanied with a whisper, "Three doors, each with nothing but darkness
residing behind them. Still, if your life is something you wish to keep a grasp on, one of them you must open and walk through. One
must embrace the darkness that is death in order to live. The voice then escapes your mind as quick as it entered, and when you come to
you find yourself standing amongst three large, ancient looking doors, a red one on the left, one blue door on the right, and a yellow
door that stands in between.\n
Type "red", "blue" or "yellow" below!\n''')
        
        # CHOICE NUMBER 3 -- Correct Option???
        if choice_number3.lower() == "yellow":
            print('''Though you feel the sense of destiny confirming your choice to be the right one, you can't help but feel
as if you're still making a decision that will cast a shadow on your existence that will reside with you even in death. Rigid, wet
and cold fingers from your hand wrap around the door's handle; this isn't you making these movements. You pull the handle down slowly,
and pull the door towards you even slower; this isn't you making these movements. Inch by single inch, closer and closer you come to
finding what lies behind this door, and the closer you come, the more you begin to feel less like yourself, until the door is finally
fully ajar... Your eyes right away recognize what they are looking upon. Your mind recognizes what that sense of destiny truly was this
entire time. And most importantly, you realize what the voice meant when it said the darkness that is my death must be embraced... For 
what lies on the opposing side of the doors threshhold, is unmistakingly your lifeless corpse, the chest gaped apart with no sign of
internal organs residing inside, nor are they laid out on the floor in front of the body. Besides the horrifying sight of your own body
knelt on the floor, lifeless, the only other thing you can recognize filling that dank chamber is what appears to be a bronze dagger,
crudely engraved with ancient glyphs and a hilt that appears to be made in the image of the All-Seeing Eye; the namesake of the very
pyramid you entered, and will never, ever leave.\n
GAME OVER!''')
            
        # CHOICE NUMBER 3 -- Correct Option???
        elif choice_number3.lower() == "blue":
            print('''Though you feel the sense of destiny confirming your choice to be the right one, you can't help but feel
as if you're still making a decision that will cast a shadow on your existence that will reside with you even in death. Rigid, wet
and cold fingers from your hand wrap around the door's handle; this isn't you making these movements. You pull the handle down slowly,
and pull the door towards you even slower; this isn't you making these movements. Inch by single inch, closer and closer you come to
finding what lies behind this door, and the closer you come, the more you begin to feel less like yourself, until the door is finally
fully ajar... Your eyes right away recognize what they are looking upon. Your mind recognizes what that sense of destiny truly was this
entire time. And most importantly, you realize what the voice meant when it said the darkness that is my death must be embraced... For 
what lies on the opposing side of the doors threshhold, is unmistakingly your lifeless corpse, the chest gaped apart with no sign of
internal organs residing inside, nor are they laid out on the floor in front of the body. Besides the horrifying sight of your own body
knelt on the floor, lifeless, the only other thing you can recognize filling that dank chamber is what appears to be a bronze dagger,
crudely engraved with ancient glyphs and a hilt that appears to be made in the image of the All-Seeing Eye; the namesake of the very
pyramid you entered, and will never, ever leave.\n
GAME OVER!''')
            
        # CHOICE NUMBER 3 -- Correct Option???
        elif choice_number3.lower() == "red":
            print('''Though you feel the sense of destiny confirming your choice to be the right one, you can't help but feel
as if you're still making a decision that will cast a shadow on your existence that will reside with you even in death. Rigid, wet
and cold fingers from your hand wrap around the door's handle; this isn't you making these movements. You pull the handle down slowly,
and pull the door towards you even slower; this isn't you making these movements. Inch by single inch, closer and closer you come to
finding what lies behind this door, and the closer you come, the more you begin to feel less like yourself, until the door is finally
fully ajar... Your eyes right away recognize what they are looking upon. Your mind recognizes what that sense of destiny truly was this
entire time. And most importantly, you realize what the voice meant when it said the darkness that is my death must be embraced... For 
what lies on the opposing side of the doors threshhold, is unmistakingly your lifeless corpse, the chest gaped apart with no sign of
internal organs residing inside, nor are they laid out on the floor in front of the body. Besides the horrifying sight of your own body
knelt on the floor, lifeless, the only other thing you can recognize filling that dank chamber is what appears to be a bronze dagger,
crudely engraved with ancient glyphs and a hilt that appears to be made in the image of the All-Seeing Eye; the namesake of the very
pyramid you entered, and will never, ever leave./n
GAME OVER!''')
        
    # CHOICE NUMBER 2 -- Wrong Option
    else:
        print('''The fear of potentially drowning seems to outweigh the fear of potentially being torn apart by this unknown beast.
You have felt it brush against your leg, and even though the filthy water you're trying to escape from clouds your vision, you can tell
from the few minor glimpses of the beast that it is more than capable of rendering you into an unrecognizable pile of tissue and bone.
The decision to throw caution to the wind has been made. With no real sense of direction to point you to the surface, you take a guess
and use all the remanining strength you have to begin swimming. A few seconds and a few kicks of the feet pass when one of those very
kicks makes contact with something solid... Before the contact you've made with your foot even registers with you, the beast has already
registered you as prey, wrapping it's eel-like body around the entire length of yours in a matter of milleseconds. The creature begins
to squeeze and constrict, putting fear inside you deserving of such a crude predator as this one. Although, while this fear goes through
your mind, a familiar voice makes itself known inside your head. "This was your destiny no matter what, that being death and darkness.
A eternity serving me and my creations. You had potential though... Potential to serve at my knees instead of serving as sustanance for
the creature your remains reside in. Don't you fear though, it is not anything like laying your head down for a dreamless sleep, your
death that is... I would say it is more akin to how the blind dream. Just sound, coming from unknown realms of the collective mind.
Though... the only mind you'll be connected to will be mine, and the millions that've come before you and the billions that will come 
after you.\n
GAME OVER! Try again...''')
        
# CHOICE NUMBER 1 -- Wrong Option
else: 
    print('''\nYou glance towards the left, it differs in no way from the path to your right, the choice to be made at this point is
akin to the flip of a coin. Your mind stirs to make a decision for only a few seconds before taking your first step towards the
right... The second step follows, then the third... You set your right foot down, and raise the left not knowing that your
life will be stripped from you before you can even plant your lifted foot... You have triggered a pressure plate rigged to a 
vicious and crude wall of spikes made to impale and only that.\n   
GAME OVER! Try again...''')