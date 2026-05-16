import argparse

parser = argparse.ArgumentParser()

parser.add_argument("console")

args = parser.parse_args()

print(f"I like {args.console}")