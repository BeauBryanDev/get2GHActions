import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"Hello There, {nombre} from GitHub!")


if __name__ == "__main__":
    main()
