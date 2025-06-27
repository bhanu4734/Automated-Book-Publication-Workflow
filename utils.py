def save_to_file(filename: str, content: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def load_from_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
