import random

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

count = 0

while True:
    text = input("> ")

    if text == text.upper() and text != text.lower():
        if text == "ПОКА!":
            count += 1

            if count == 3:
                print("ДО СВИДАНИЯ, МИЛЫЙ!")
                break
        else:
            count = 0

        year = random.randint(1930, 1950)
        print("НЕТ, НИ РАЗУ С {} ГОДА!".format(year))

    else:
        count = 0
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
