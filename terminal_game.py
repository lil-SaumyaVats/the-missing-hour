print("=" * 40)
print("THE MISSING HOUR")
print("=" * 40)
print("        >> A MYSTERY AWAITS <<")
print("=" * 40)
print()
print("You wake up confused.")
print("An entire hour of your memory is gone.")
print("You don't remember what happened between 11 PM and 12 AM.")
print()
print("-" * 40)
print()
print("What would you like to investigate first?")
print("1. Check your phone")
print("2. Look around your room")

choice1 = input("Enter 1 or 2: ")

if choice1 == "1":
    print("You unlock your phone.")
    print("There are two strange things on your screen:")
    print("1. A missed call from an unknown number")
    print("2. A text message: 'DON'T GO TO THE STATION'")
    print("-" * 40)
    choice2 = input("What do you open? (1 or 2): ")
    
    if choice2 == "1":
        print("The call log is empty... but something feels wrong")
        print("But you made an outgoing call at 11:37 PM.")
        print("You don't remember calling anyone.")
    
    elif choice2 == "2":
         print("The message disappears after you read it.")
         print("Your phone heats up suddenly.")
         print("A new message flashes: 'They are watching you.'")

    print()
    print("-" * 40)
    print("What do you do next?")
    print("1. Go to the station")
    print("2. Try calling the number back")
    choice3 = input("Enter 1 or 2: ")

    if choice3 == "1":
        print()
        print("You arrive at the station at midnight.")
        print("It's empty. But your phone buzzes again.")
        print("A photo. You. Standing here. Last night.")
        print("=" * 40)
        print("--- ENDING: YOU WERE NEVER SUPPOSED TO REMEMBER ---")
        print("=" * 40)
    
    elif choice3 == "2":
        print()
        print("The number rings.... then someone picks up.")
        print("Silence. Then your own voice says: 'Don't look for me.'")
        print("=" * 40)
        print("--- ENDING: THE CALL WAS FROM YOU ---")
        print("=" * 40)

elif choice1 == "2":
    print("You look around your room.")
    print("You find two strange things:")
    print("1. A crumpled note")
    print("2. A muddy shoe")
    print("-" * 40)
    choice2 = input("What do you check? (1 or 2): ")

    if choice2 == "1":
        print("The note says: 'You left at 11:30 PM willingly.'")
        print("The handwriting looks like yours...... but different")
        print("You trusted someone. But who?")

    elif choice2 == "2":
        print("The shoe has dirt from the underground tunnels.")
        print("Metro station dust.")
        print("You didn't go alone last night.")

    print()
    print("-" * 40)
    print("What do you do now?")
    print("1. Go to the station")
    print("2. Stay home and piece it together")
    choice3 = input("Enter 1 or 2: ")

    if choice3 == "1":
        print()
        print("You rush to the station.")
        print("On the platform you find your own jacket.")
        print("In the pocket — a note in your handwriting:")
        print("'You chose to forget. Don't undo it.'")
        print("=" * 40)
        print("--- ENDING: SOME TRUTHS ARE MEANT TO STAY HIDDEN ---")
        print("=" * 40)
    
    elif choice3 == "2":
        print()
        print("You sit down and connect every clue.")
        print("The note. The mud. The missing hour.")
        print("You were used as a messenger. And then erased.")
        print("=" * 40)
        print("--- ENDING: YOU WERE NEVER SUPPOSED TO REMEMBER ---")
        print("=" * 40)
        



