import os


def main():
    lenguaje = os.getenv("LANGUAGE")
    print(f"¡Mi lenguaje favorito es:, {lenguaje}!")


if __name__ == "__main__":
    main()