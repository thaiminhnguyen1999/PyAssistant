from datetime import date, datetime
import pyttsx3
import speech_recognition
from game import rps, math_game, pacman, tetris, snake

voice_processor = speech_recognition.Recognizer()
return_result = pyttsx3.init()
assistant_handler = ""

usr_name = input("Please indicate your name: ")

while True:
    with speech_recognition.Microphone() as mic:
        print("Assistant: I'm listening")
        audio = voice_processor.listen(mic)

    print("Assistant: Wait a minute")

    try:
        user = voice_processor.recognize_google(audio)
    except:
        user = ""

    print("User: " + user)

    if user == "":
        assistant_handler = "I can't hear you, try again"
    elif "hello" in user:
        assistant_handler = "Hello " + usr_name
    elif "today" in user:
        today = date.today()
        assistant_handler = today.strftime("%B %d, %Y")
    elif "time" in user:
        now = datetime.now()
        assistant_handler = now.strftime("%H hours %M minutes %S seconds")
    elif "rock paper scissor" in user:
        print("Wait a moment to open the game Rock Paper Scissors")
        rps()
    elif "math game" in user:
        print("Wait a moment to open the game Math Game")
        math_game()
    elif "Pac-Man" in user:
        print("Wait a moment to open the game Pacman")
        pacman()
    elif "Tetris" in user:
        print("Wait a moment to open the game Tetris")
        tetris()
    elif "snake" in user:
        print("Wait a moment to open the game Snake")
        snake()
    elif "Bye" in user:
        assistant_handler = "Bye " + usr_name
        print("Assistant: " + assistant_handler)
        return_result.say(assistant_handler)
        return_result.runAndWait()
        break
    else:
        assistant_handler = "I don't know what you're talking about. Let's try to say it again"

    print("Assistant: " + assistant_handler)
    return_result.say(assistant_handler)
    return_result.runAndWait()