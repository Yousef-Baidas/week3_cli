import argparse
import unicodedata
import re
from pathlib import Path
def main():

    parser = argparse.ArgumentParser(description= "Generates outlines for a specified topic")

    parser.add_argument("topic", help= "The topic used for the outline")
    parser.add_argument("--bullets", type= int, default= 5, help= "The bullet points used to build the structure of the outline")

    args = parser.parse_args()

    print(f"Topic Chosen: {args.topic}")
    print(f"Number of bullet points: {args.bullets}")

    out_dir = Path("outlines")
    out_dir.mkdir(parents= True, exist_ok= True)

    safe_name = slugify(args.topic)
    file_path = out_dir / f"{safe_name}.md"

    with file_path.open("w") as f:
        f.write(f"# {args.topic}\n")

        for i in range(1, args.bullets + 1):
            f.write("-point {i}\n")

def slugify(text: str) -> str:
    text = text.lower()

    result = []

    for char in text:
        cat = unicodedata.category(char)

        if cat.startswith("Z") or cat.startswith("P"):
            result.append("-")

        elif cat.startswith("S"):
            pass

        else:
            result.append(char)

    result = "".join(result).strip("-")
    result = re.sub("-+", "-", result)

    return result

if __name__ == "__main__":
    main()