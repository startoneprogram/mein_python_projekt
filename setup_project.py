import os


def create_structure():
    folders = ["src", "tests", "docs"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("Projektstruktur erfolgreich erstellt!")


if __name__ == "__main__":
    create_structure()
