import sys


def redirect_to_file(text):
    original = sys.stdout
    sys.stdout = open("/path/to/your/text.txt", "w")
    print("This is your redirected text:")
    print(text)
    sys.stdout = original
    print("This line WONT be on the file")


if __name__ == "__main__":
    redirect_to_file("python es la mera vena")
