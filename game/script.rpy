define kyu = Character("KyuSiik", color="#B486D9")
define nerva = Character("[Nerva_name]", color="#86D5D9")
define varce = Character("[Varce_name]", color="#ACD986")
define tsuzu = Character("[Tsuzu_name]",  color="#D98A86")

transform laugh:
    linear 0.05 yalign 0.9
    linear 0.1 yalign 1.1
    linear 0.05 yalign 1.0
    repeat 3

transform rage:
    linear 0.02 xoffset 12
    linear 0.04 xoffset -24
    linear 0.02 xoffset 12
    repeat 5

transform left:
    xzoom -1.0
    xalign 0.12
    yalign 1.0

transform right:
    xzoom 1.0
    xalign 0.88
    yalign 1.0

transform faceright:
    xzoom -1.0

transform faceleft:
    xzoom 1.0


label start:
    #Intro scene, in which Kyu wakes up and meets the rest of the cast

    "Before beginning, please note that all dialogue images and sounds are currently placeholders, and are subject to change in future versions."
    "Also, this game contains sexual content, so first I need to verify you're of legal age."

    menu:
        "Are you over the age of 18?"

        "Yes":
            "Bonza, then you're free to go."
            "Hope you enjoy this early build of the game."

        "No":
            jump ending_0

    play music moonlight
    scene bg sea1
    "A growl escapes your throat. A deep rumble of resigned rage."
    "The guards either side of you visibly leer backwards as your rage bubbles through."
    "Fighting back would be a bad idea, with your hands bound behind your back. The cruel, barbed points of anti-dragon spikes visible protruding from the barrels of the guards' shotguns."
    "These bastards came prepared, ready to put you down at a moment's notice."
    "You take one last look at your faithful ship."
    "The Black Valiant, true to her name through many battles and rough seas. Even now she seemed to fight against the thick steel chains that dragged her unwillingly behind the smoke-belching warship of your captors."
    "You're snapped out of your thoughts by the rough questioning of a guard."
    stop music
    "Guard" "You listening bitch!? I said confirm your identity!"
    kyu "{i}Kernig Axeldrana the fucking Fourteenth!{/i}"
    kyu "There's no need for this, you know wh-{w=0.6}{nw}"
    "You feel the hard wooden stock of one of the guard's weapons strike you in the jaw" with hpunch
    "Guard" "Don't play games with us! I heard star-dragons, float but can't swim. I'm sure you don't want me testing that rumour!"
    "He punctuates his point with a cruel laugh."
    "Guard" "Now, answer the damn question. You are KyuSiik Greokhwang, the Neon Eviscerator. Please confirm!"
    "You shoot a glance at the other guard, ready to clobber you in the face again."
    kyu "Not the first time I've been called either of those names."
    kyu "Though I resent your insistance on calling me  anything but KyuSiik."
    "The guard begins scratching some marks into a wax tablet in his hand."
    "Guard" "The Kaxa'aad thanks you for your cooperation..."
    "Guard" "Now, with your identity confirmed, we're taking you into custody for the following charges."
    "Guard" "Piracy{w=1}{nw}"
    "Guard" "Murder{w=0.8}{nw}"
    "Guard" "Arson{w=0.6}{nw}"
    "Guard" "Armed Robbery{w=0.4}{nw}"
    "Guard" "Looting{w=0.3}{nw}"
    play music moonlight fadein 0.6
    "Guard" "Posession of Restricted Substances{w=0.3}{nw}"
    "Guard" "Distribution of Restricted Substances{w=0.3}{nw}"
    "Guard" "Intent to Desert a Designated Place of Exile{w=0.3}{nw}"
    "Guard" "Deserting a Designated Place of Exile{w=0.3}{nw}"
    "Guard" "Whistling on a Tuesday{w=0.3}{nw}"
    "Guard" "Desecration of Pizza with Pinapple, Chives and Mayonaise{w=0.3}{nw}"
    "The list of charges continue, as the small boat rows closer to the lumbering form of the grey and orange ironclad behind you."
    "Its three forward deck turrets remain trained on the Valiant even now, as though she might autonomously leap back into action and break her chains."
    "You can't help but grin to yourself. It's almost an honour, needing a fleet of five cutting-edge battleships to finally bring you in."
    "Still, this was bad."
    "Sailing one day with absolute freedom toward strange horizons with the cool sea breeze across your wings, bellowing out shanties with friends, a cargo hold full of iced tea and a warm bed full of warm bodies to spend the night with."
    "Life was so fine, the ocean so vast and it felt like all of it was your playground. But you got complaicent, only to have it ripped away from you overnight, by the engine of opression, the Kaxa'aad."
    "Their chuffing cast-iron war machines steamed over the horizon in the early hours of the morning. By the time you could make it to the bridge the thundering of cannons was already echoing across the waters from both sides of the engagement."
    "By sunrise the Valiant was taking on water and the deep bellowing warhorns of the dark grey ships sitting all around her lofting shell, demanded surrender or death."
    menu:
        "I surrendered":
            "Insert surrender scene here"

        "I fought back":
            "Better to die free, than to live as a slave. Together, you and your crew put up a viscious last stand. With nothing but your trusty revolver, you held off the first few waves."
            "Six gem-tipped rounds flew true, slicing through the armour of the boarding infantry and leaving a trail of green sparks."
            play sound "audio/clink.ogg"
            "You crack open your weapon, fumbling for another six rounds. The scent of gunpowder filling your nostrils as the spent casings scatter loosely at your feet."
            play sound "audio/bang.ogg"
            "You hear the crack of rifle fire, instinctually forcing you to your knees behind a barrel of spice. The bulky shape of a Kaxa infantryman barreling toward you. Two more quickly mounting the deck."
            play sound "audio/bang.ogg"
            play sound "audio/bang.ogg"
            "Another rifle crack, followed by another. The soldiers work in pairs, one moving while the other shoots. With your weapon fully loaded you pop up, ready to loose another round into the rapidly appraching intruder when-"
            play sound "audio/bang.ogg"
            stop music
            "A rifle round strikes your shoulder, it glances off your scales but the impact takes the wind clean out of your lungs, knocking off your aim."
            "In that very same second, the armoured brute slams bodily into you, pinning you to the ground with his full weight."
            "Seeing their captain taken prisoner, a few crewmen begin to surrender. The rest stood fast, and died fighting for what they beleived in."

    "But for you, the captain of the Valiant, the one they called the Neon Eviscerator. For you, they had a special fate in store."

    "Guard" "For your crimes you will be taken to court martial and sentenced to death by firing squad."
    "Guard" "Your execution will be public, and will serve as an example to all those that make themselves enemies of Kaxa'aad"
    "Guard" "Do you understand the rights I've just read to you?"
    kyu "Heh, \"Rights\"..."
    "You take another glance at the other guard"
    kyu "Yeah...yeah I do."
    scene black
    "After the long and arduous process of loading you on board, you find yourself being marched toward the brig. By now, the exhaustion and lack of sleep is beginning to catch up with you, filling your head with a grey fog."
    "Even trying to think of a way out is near impossible, not that it would do much good with the constant threat of a dragon spike through the back of the skull at the slightest misstep."
    "Your legs practically give out beneath you as they throw you into the cell, and you hear the mechanical clunk of the key turning in the lock behind you."

    scene bg brig
    $ Nerva_name = "???"
    $ Varce_name = "???"
    $ Tsuzu_name = "???"


    "You wake up in a small room, four steel walls and a low ceiling. The room is almost pitch black, thankfully it happens that your kind can see quite well in the dark."
    "A few slivers of light poke through some rusted holes behind you, as well as through a few cracks around the edges of what appears to be a double door taking up almost the entire wall."
    "This might be an impressive feat had the wall not been so small."
    "The ground seems to shift and sway rhythmically beneath you, the familiar sensation of a ship bobbing about on the waves."
    "Your body is completely covered from the neck down in a baggy, scratchy hession jumpsuit"
    "The floor of the room is covered in a thin layer of hay or straw, presumably for comfort?"
    "Not exactly living it up in here is it?"
    "You try to move."
    play sound "audio/clink.ogg"
    "*Clink*" with hpunch
    "Your hands are bound behind your back, the cold steel of a pair of manicles digging into your wrists."
    kyu "Shit!"
    "Footsteps sound softly around the chamber, accompanied by a harsh mechanical ticking."
    "You start to think about how you're going to get out of this one."
    "Taking a look around, you realize you're not alone in here. There are three others chained down in a similar fashion to yourself."

    show nerva crying with dissolve
    "Opposite you, a young coyote quietly sobs. Tears pour from her eyes as she seemingly does her best to shrink into the corner."
    hide nerva with moveoutright
    show varce neutral with moveinleft
    "Beside her, a stocky dragon sits slumped against the steel wall. Thick golden-brown scales cover his sides as he gazes blankly off at seemingly nothing."
    hide varce with moveoutright
    show tsuzu neutral with moveinleft
    "Finally, to your left, sits a rather irritated looking black and red honey badger. That is to say, the parts of her that aren't heavily augmented or replaced by clockwork."
    show tsuzu annoyed
    "The amber glow of the eyes behind her visor narrows as she notices you."
    tsuzu "Yeah! Keep staring punk!!"
    tsuzu "Get a nice good look, see what happens."
    show tsuzu annoyed at left with move
    show varce neutral at right with moveinright
    varce "Ahh! Finally awake are you?"
    varce "Don't listen to her, she tried the same thing on ME would you beleive it!?"
    "The dragon lets out a deep mirthful chuckle."
    tsuzu "Shut your whore mouth!!" with hpunch
    show varce happy at laugh
    "The dragon chuckles"

    kyu "Hey!"
    kyu "Would you two pipe down!?"
    kyu "I know this probably isn't the most relaxing cruise we've all been on. But fighting ain't gonna get us nowhere!"
    tsuzu "..."
    varce "..."
    tsuzu "Whatever"
    varce "Sure"
    kyu "Bonza..."
    kyu "Well...Hello everybody! My name is Kyu, it's nice to meet you all. I'd shake your hands but..."
    play sound "audio/clink.ogg"
    "You shake your chains."
    kyu "Now, unlike the looks of you lot this ain't the first time I've been chained to a wall (even if you don't count the times I did it with consent)"
    kyu "Point is, I reckon I can get us out of here. I just need to know a bit about what's going on."
    kyu "However, first thing's first."
    hide varce with moveoutleft
    hide tsuzu with moveoutleft
    show nerva crying with moveinright
    kyu "You there..."
    kyu "You doing okay?"
    nerva "...!?"
    nerva "*Sobs*"
    "She turns to you, breathing heavily and wide-eyed with fear."
    nerva "N-no!?"
    nerva "Of course I'm not okay!"
    kyu "Fair enough"
    kyu "We're gonna get you out of here though, okay?"
    "She nods silently. Doubtful and clearly still shaken, but more hopeful than before."
    hide nerva with dissolve
    kyu "Right. Listen up lads, if we're getting out of here I'm gonna need to know what's going on."


    $ varceknown = False
    $ tsuzuknown = False
    $ nervaknown = False

label intro_decision_1:
    if varceknown & tsuzuknown & nervaknown:
        jump intro_decision_1_skip

    menu:
        "Talk to the dragon":
            $ varceknown = True
            jump intro_decision_1_varce

        "Talk to the protomaton":
            $ tsuzuknown = True
            jump intro_decision_1_tsuzu

        "Talk to the coyote":
            $ nervaknown = True
            jump intro_decision_1_nerva

label intro_decision_1_varce:
    show varce neutral at center with dissolve
    if(not tsuzuknown and not nervaknown):
        "You decide that the dragon seems the most amicable, and resolve to speak to him first."
    kyu "So, big boi! What's your deal?"
    varce "Hah, wrong place, wrong time!"
    varce "They don't much like my kind around these parts..."
    varce "Not that your ancestors  would have anything to do with that...heh"
    varce "Not to throw any bad blood on yourself of course."
    varce "I know what it's like to have others judge you for what you are rather than who."
    varce "I'm guessing we're both in the same boat..."
    kyu "Yeah, literally and metaphorically!"
    show varce at laugh
    varce "Hahah, nice one!"
    kyu "Thanks!"
    kyu "But yeah. My kind's reputation is hardly unfounded, but we don't take others against their will. It's just that we can be very persuasive."
    kyu "It's wrong that we should be hunted for being who we are, and expressing our sexuality in a place where pleasure is considered evil."
    kyu "It's even more wrong that your kind should be hunted too, just because we're both kinds of dragon from above the sky."
    "He shrugs"
    varce "It is what it is."
    $ Varce_name = "Varce"
    varce "Anyway, name's Varce."
    varce "Pleasure to meet you!!"
    kyu "Ohh~ It will be!"
    kyu "Heheh, I'm sorry. Big strong men like yourself always send my nuts churning!"
    varce "Hahah, don't worry about it! Those that put us here are right about one thing!"
    show varce happy
    varce "We dragons are united in our unstoppable urge to fuck!"

    hide varce with dissolve
    jump intro_decision_1

label intro_decision_1_tsuzu:
    show tsuzu neutral at center with dissolve
    if not(varceknown or nervaknown):
        "You decide to first speak to the protomaton, if for no other reason than to show you're not intimidated by her uncouth conduct."
    kyu "So, who might you be, and how did you end up in this mess?"
    show tsuzu shocked
    tsuzu "Who am I!?"
    tsuzu "Ach! As if my day couldn't get any worse now this fucker says they don't know who I am!"
    tsuzu "Typical!"
    show tsuzu at faceright
    "She scoffs and turns to the rest of the room, as if for approval."
    "The others look at her blankly"
    show tsuzu at faceleft
    "She rolls her eyes, shaking her head a little in disbelief."
    tsuzu "Uncultured swines."
    show tsuzu neutral
    tsuzu "Still...it makes sense I suppose."
    tsuzu "The Kaxa'aad did all they could to shut me up..."
    tsuzu "Never thought they'd take it this far though."
    $ Tsuzu_name = "Tsuzu"
    tsuzu "Name's Tsuzu. I'm a musician."
    show varce happy at right with moveinright
    show tsuzu at left with move
    varce "Never heard of ya"
    show tsuzu annoyed at rage
    tsuzu "Listen here you littl-"
    hide varce with moveoutright
    show nerva shocked at right with moveinright
    nerva "Oh shit!!"
    nerva "THE Tsuzu!?"
    show tsuzu shocked
    tsuzu "Y-..."
    show tsuzu happy
    tsuzu "Yeah!"
    nerva "I have like...all your phonograph recordings!!"
    show nerva sad
    nerva "Well...had...I guess."
    tsuzu "Hey! Who needs a recording when you have the real thing eh?"
    "With that, she begins humming out the melody to presumably one of her songs."
    kyu "Uhm...Much as I hate to break up the show, ladies. But there are probably guards around here somewhere, and if they hear you they're likely to come in here and try shut us up."
    hide nerva with moveoutright
    show tsuzu at center with move

    hide tsuzu with dissolve
    jump intro_decision_1

label intro_decision_1_nerva:
    show nerva crying at center with dissolve
    if not(varceknown or tsuzuknown):
        "She's clearly the most distressed by the situation. Best to keep talking to her."

    kyu "So, what about you? What's your story?"
    nerva "..."
    nerva "There were five of us."
    nerva "We had to get out..."
    nerva "There was a guy...smuggled us onto a goods train in Tannheim."
    nerva "It took us from there to Dorvagrad where we stole a boat and tried to cross the Chine."
    kyu "{i}The chine. The rocky and treacherous ocean between the Northlands and the Perissyan Union...{/i}"
    kyu "{i}That must be where we are!{/i}"
    nerva "We drifted for days, when this patrol ship found us. By then there were only three of us left."
    nerva "They hailed us, ordering us not to resist arrest. When we refused they opened fire."
    nerva "The others...the others didn't make it, and like a coward I surrendered."
    "She bursts into tears again."
    kyu "Hey, you did the right thing! You were put in an impossible situation."
    nerva "No!!"
    nerva "I...I deserve this. I abandoned the only people that ever showed me kindness."
    kyu "Your friends sound like brave people, I'm sorry I never got the opportunity to meet them."
    kyu "But you're still here! As long as there's breath in your body, there's still hope for freedom. You have to keep going...for them. I'm sure they'd want you to at least try!"
    kyu "If you make it out...then it means their fight wasn't for nothing."
    nerva "Maybe you're right...maybe not."
    kyu "Look...what's your name?"
    nerva "Bil-..."
    $ Nerva_name = "Nerva"
    show nerva neutral
    nerva "Nerva!"
    nerva "My name's Nerva."
    kyu "Listen, Nerva. You're not the problem here."
    kyu "You deserve to be free, to be happy! So don't blame yourself."
    "She takes a deep breath"
    nerva "Maybe you're right...maybe not"
    nerva "But I'd rather die a free woman than...than live out the rest of my days digging coal up in the freezing north!!"
    show nerva at right with move
    show tsuzu happy at left with moveinleft
    tsuzu "That's more like it!"
    tsuzu "I knew there was a firey spirit somewhere down in there!"
    if tsuzuknown:
        show nerva blush
        nerva "Th-thanks Tsuzu!"
        nerva "It means a lot coming from you!"

    hide nerva with dissolve
    hide tsuzu with dissolve
    jump intro_decision_1

label intro_decision_1_skip:
    show tsuzu annoyed at center with dissolve
    tsuzu "So then!?"
    kyu "What?"
    tsuzu "We've had the draconic inquisition from you, but we don't know a damn thing about you!"
    show tsuzu at left with move
    show nerva annoyed at right with moveinright
    nerva "Yeah! Who actually are you, and why should we trust you to get us out of here?"
    kyu "I'm a pirate"
    show tsuzu shocked
    tsuzu "!?" with hpunch
    kyu "Yarr~"
    kyu "Yeah, I'm not what people think of right!"
    show tsuzu at left with move
    show nerva shocked at right with moveinright
    nerva "I mean...I guess that explains why you're locked up anyway!"
    show varce neutral at center with dissolve
    varce "And why you think you can get out of here"
    show varce angry
    varce "But I assume you'll be leaving us to rot"
    show tsuzu neutral
    tsuzu "Yeah, why should we trust you to bring us with you?"
    kyu "Ahh...it's a sad thing"
    kyu "We pirates actually have a strict code of honour."
    kyu "In days gone by I could give you my word and everyone would know that I'm bound by it."
    kyu "But thesedays you all assume us to be liars, cheats and drunkards!"
    nerva "Yup!"
    nerva "What the hell do you expect!? When your livelihood is based off ruining others?"
    kyu "That's an unfair assessment. We just see it as...redistributing wealth, away from those that horde it devoid of reason and making it available to those who need it more."
    varce "Oh yeah, I'm sure all those innocent souls at the bottom of the ocean are really glad you 'liberated' their rich masters of their assets?"
    kyu "Rule 1 of pirate law. Don't attack one who would not attack you first. We make that perfectly clear to any crews we come upon and usually they just let us have our way."
    kyu "It's a victimless crime really"
    show tsuzu angry at rage
    tsuzu "I'm not so sure that's true!"
    kyu "Okay fair enough, I'll find a way to convince you down the line. But first do you want out of here or not?"
    tsuzu "Not if you're gonna ditch us!"
    tsuzu "You dragons are all the fucking same!!"
    tsuzu "Only think about yourselves!!"
    show varce angry
    varce "Hey!!" with hpunch
    varce "You shut your fucking mouth before I shut you up!!"
    show nerva at faceright
    "Nerva curls up again, her ears flattening out"
    kyu "Guys please! Keep your voices down!"
    show varce at rage
    varce "Shut the fuck up!!"
    show tsuzu at rage
    tsuzu "Keep out of this you filthy pirate scum!!"
    play sound "audio/bang.ogg"
    "Suddenly the chamber floods with light, a tall imposing figure standing at the door, flanked by the stocky shapes of two guards clad in thick plates of armour." with hpunch
    keera "What's going on in here!?"
    "Everyone goes silent"

    #Endings
label ending_placeholder:
    scene black
    "The game has now ended"
    jump terminate

label ending_0:
    scene black
    "Ending 0: You are too young to play this game"
    jump terminate


label terminate:
return
