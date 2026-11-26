def convert_book(line):
    book = line.strip().split('|')

    return [
        book[0],
        book[1],
        book[2],
        int(book[3]),
        float(book[4])
    ]


def get_books(filename):
    file = open(filename, 'r', encoding='utf-8')

    lines = file.readlines()[1:]

    file.close()

    return list(map(convert_book, lines))


def filtered_books(books, search):
    return list(map(
        lambda book: [
            book[0],
            book[1] + ', ' + book[2],
            book[3],
            book[4]
        ],
        filter(
            lambda book: search.lower() in book[1].lower(),
            books
        )
    ))


def get_book_totals(books):
    return list(map(
        lambda book: (book[0], book[2] * book[3]),
        books
    ))


def main():
    books = get_books('books.csv')

    filtered = filtered_books(books, 'python')

    result = get_book_totals(filtered)

    print(books)
    print(filtered)
    print(result)


main()
