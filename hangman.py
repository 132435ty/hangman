import random
import textures

hp = [textures.vis0, textures.vis1, textures.vis2, textures.vis3, textures.vis4, textures.vis5, textures.vis6, textures.vis7]

def choose_word():
    word_list = ['привет', 'листок', 'счастье', 'яйцо', 'колонна', 'огурец', 'компьютер']
    return random.choice(word_list)

def display_word(word, letters):
    display = ""
    for letter in word:
        if letter in letters:
            display += letter
        else:
            display += "_"
    return display

def vis():
    word = choose_word()
    letters = []
    attempts = 7

    print(display_word(word, letters))

    while attempts > 0:
        guess = input("введи букву: ")
        print(hp[attempts])

        if len(guess) != 1 or not guess.isalpha():
            print(hp[attempts])
            print("впиши 1 букву.")
            continue

        if guess in letters:
            print(hp[attempts])
            print("ты уже называл эту букву.")
            continue

        letters.append(guess)

        if guess in word:
            print("угадал!")
            if display_word(word, letters) == word:
                print("ура, ты угадал слово:", word)
                print(hp[attempts])
                break
        else:
            attempts -= 1
            print("не правильный ответ. у тебя осталось", attempts, "попыток.")
            print(hp[attempts])

        print(display_word(word, letters))

    if attempts == 0:
        print(hp[attempts])
        print("прости, но у тебя закончились попытки, твоим словом было:", word)

vis()
