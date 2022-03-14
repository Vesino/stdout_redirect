from contextlib import redirect_stdout


def redirected(text, path):
    with open(path, "w") as out:
        with redirect_stdout(out):
            print("Here is the text that you provided: ")
            print("*" * 40)
            print(text)
            print("*" * 40)


if __name__ == "__main__":
    path = "path/to/your/redirected.txt"
    text = "This is a really amazing text, but if it were it should not be mentioned xd"
    redirected(text, path)
