import sys

from contextlib import contextmanager


@contextmanager
def custom_redirection(fileobject):
    old = sys.stdout
    sys.stdout = fileobject
    try:
        yield fileobject
    finally:
        sys.stdout = old


if __name__ == "__main__":
    with open("path/to/your/context_text.txt", "w") as out:
        with custom_redirection(out):
            print("This values will be written in our file")
            print("Also this string xd")
        print("But this value WONT, this will be printed in console as should be")
