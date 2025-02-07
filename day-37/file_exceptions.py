"""
Handle exceptions for file not found.

"""

def read_file(myfile):
    try:
        with open(myfile, "r") as file:
            print(file.read())
    except FileNotFoundError as err:
        print(err)


if __name__ == "__main__":
    myfile = "test.txt"
    read_file(myfile)
