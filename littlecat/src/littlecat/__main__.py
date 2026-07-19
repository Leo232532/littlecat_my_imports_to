import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="littlecat",
        description="Littlecat Command Line Tool"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version"
    )

    args = parser.parse_args()

    if args.version:
        print("Littlecat OS 1.0")
        return

    print("Welcome to littlecat!")

if __name__ == "__main__":
    main()