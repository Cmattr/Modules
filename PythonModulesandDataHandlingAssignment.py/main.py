import moods

mood = input("How are you feeling today? (happy / sad / excited): ")

if mood == 'Happy':
    moods.happy_mood()
elif mood == "sad":
    moods.sad_mood()
elif mood == "excited":
    moods.excited_mood()
else:
    print("please enter your mood as happy, sad, or excited.")