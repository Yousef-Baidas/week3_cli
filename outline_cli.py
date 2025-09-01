import argparse
from pathlib import Path

def main():
    
    parser = argparse.ArgumentParser(description= "Generate an outline for a topic")

    parser.add_argument("topic", help= "Topic used for the outline")

    parser.add_argument("--bullets", type= int, default= 5, help= "Bullet points for the outline structure")

    args = parser.parse_args()

    print(f"Topic chosen: {args.topic}")

    print(f"Number of bullets: {args.bullets}")

    out_dir = Path("outlines")

    out_dir.mkdir(parents= True, exist_ok= True)

    file_path = out_dir / f"{args.topic}.md"

    print(file_path)

    with file_path.open("w") as f:

        f.write(f"# {args.topic}\n")

        for i in range(1, args.bullets + 1):
            
            f.write(f"- point {i}\n")

if __name__ == "__main__":
    
    main()