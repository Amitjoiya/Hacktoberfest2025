import re
def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s-]+', '-', s)
    return s.strip('-')
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python slugify.py \"Your Title Here\"")
    else:
        print(slugify(" ".join(sys.argv[1:])))
