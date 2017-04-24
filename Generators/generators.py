import random
import string


def chain(iterable_one, iterable_two):
    for x in iterable_one:
        yield x

    for y in iterable_two:
        yield y


def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]


def cycle(iterable):
    while True:
        for x in iterable:
            yield x


def chapters(filenames):
    for file_ in filenames:
        with open(file_, 'r') as f:
            line = f.readline()
            while line:
                if line.startswith('#'):
                    line = f.readline()
                    yield line
                line = f.readline()


def generate_book(count, length):
    letters = string.ascii_letters + string.digits + string.punctuation
    with open('book.txt', 'w') as f:
        for chapter in range(count):
            yield "#Chapter {}\n".format(chapter + 1)
            f.write("#Chapter {}\n".format(chapter + 1))
            for num in range(length):
                word = ''.join([random.choice(letters) for i in range(0, random.randint(1, 10))])
                yield word + " "
                f.write(word + " ")
            yield "\n"
            f.write("\n")


def main():
    pass


if __name__ == '__main__':
    main()
