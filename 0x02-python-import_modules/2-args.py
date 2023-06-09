#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(f"{len(sys.argv) -1} arguments", end="")

    if (len(sys.argv) - 1 == 0):
        print(".")
    else:
        print(":")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
