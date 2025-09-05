import argparse
import unicodedata
import re
import os
from pathlib import Path
from dotenv import load_dotenv
import ollama

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
if not api_key:
    print("Missing OLLAMA_API_KEY in .env (set to any dummy value).")
    exit(1)


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

    response = ollama.chat(
     model="gemma3n",
        messages=[
            {"role": "user", "content": f"Write {args.bullets} concise bullet points about {args.topic}. Output plain text, one bullet per line, no numbering."}
        ]
    )

    outline = response["message"]["content"]



    with file_path.open("w", encoding= "utf-8") as f:
        f.write(f"# {args.topic}\n\n")

        f.write(outline.strip() + "\n")

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

    if result == "":
        result = "untitled"

    result = result[:50].strip("-")

    reserved = ["con", "prn", "aux", "nul", "com1", "com2", "com3", "com4", "com5", "com6", "com7", "com8", "com9", "lpt1", "lpt2", "lpt3", "lpt4", "lpt5", "lpt6", "lpt7", "lpt8", "lpt9"]

    if result in reserved:
        result += "-file"

    return result

if __name__ == "__main__":
    main()