import random
import sys
from os import system

import romkan
import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    speech = r.recognize_google(audio)
    return speech.lower()


def speak(text):
    system(f'say {text}')


def gen_word_map():
    """
    TODO - generate a word list from JLPT word list
    """
    return [
        ('watashi', 'me'),
        ('anata', 'you'),
        ('dare', 'who'),
        ('otoko', 'male'),
        ('onna', 'female'),
        ('hito', 'person'),
        ('sensei', 'teacher'),
        ('gakusei', 'student'),
        ('jimunohito', 'admin staff'),
        ('gako', 'school'),
        ('nihongo', 'japanese'),
        ('kore', 'this'),
        ('sore', 'that'),
        ('are', 'that over there'),
    ]


def welcome():
    speak("Welcome to SteveYeahs super fun happy Japanese learning time thing")
    speak('Are you ready to get started?')
    answer = listen()
    print(answer)

    if answer != 'yes':
        fairwell()
    else:
        speak('Good, lets do this')


def fairwell():
    speak('OK. Goodbye!')
    sys.exit()


def play(word_map):
    """
    TODO
    * Score the result
    * Less praise
    * Don't say the words
    """
    random.shuffle(word_map)
    for word in word_map:
        speak(word[0])
        print(romkan.to_hiragana(word[0]))

        answer = listen()
        print(answer)

        if answer == word[1]:
            speak(correct())
        else:
            speak(bubu())
            speak(f'The correct answer was {word[1]}')


def correct():
    phrases = [
        'Thats right!',
        'Nailed it!',
        'Damn, you good!',
        'Nice work Ace!',
        'You got it going on slick!',
    ]
    return random.choice(phrases)


def bubu():
    phrases = [
        'BuBu',
        'Its good, but its not right',
        'Come on, you can do better',
        'oooo so close',
    ]
    return random.choice(phrases)


if __name__ == '__main__':
    welcome()
    word_map = gen_word_map()
    play(word_map)
    fairwell()
