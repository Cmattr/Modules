import moods

i = input("How are you feeling today? (happy / sad / excited): ")
mood = i.lower()

if mood == 'happy':
    moods.happy_mood()
elif mood == "sad":
    moods.sad_mood()
elif mood == "excited":
    moods.excited_mood()
else:
    print("please enter your mood as happy, sad, or excited.")