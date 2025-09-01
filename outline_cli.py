from pathlib import Path
import argparse

def main():

    parser = argparse.ArgumentParser(description= "Generates an outline for some topic")

    parser.add_argument("topic", help= "Topic used for the generated outline")

    parser.add_argument("--bullets", type= int, default= 5, help= "Bullets points used for the outline structure")

    args = parser.parse_args()

    print(f"Topic Chosen: {args.topic}")

    print(f"Number of bullet points: {args.bullets}")

    