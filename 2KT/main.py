import game

word, description = game.get_word()
table = game.create_table(word)
mistakes = game.get_mistakes()

game.show_start_message()
game.show_hint(description)
game.show_table(table)

while game.is_alive(mistakes) and not game.is_word_guessed(table):
    answer = game.prompt()

    if game.is_word_correct(word, answer):
        game.show_win()
        break

    elif game.is_letter_correct(word, answer):
        table = game.open_letter(word, table, answer)
        game.show_table(table)

        if game.is_word_guessed(table):
            game.show_win()

    else:
        mistakes = game.add_mistake(mistakes)
        game.show_gallows(mistakes)

        if not game.is_alive(mistakes):
            game.show_lose(word)
