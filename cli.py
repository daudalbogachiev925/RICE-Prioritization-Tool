import argparse
from rice import Feature, load_features, prioritize, save_features

def main():
    parser = argparse.ArgumentParser(description="RICE Prioritization CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list")
    p_add = sub.add_parser("add")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--reach", type=float, required=True)
    p_add.add_argument("--impact", type=float, required=True)
    p_add.add_argument("--confidence", type=float, required=True)
    p_add.add_argument("--effort", type=float, required=True)

    args = parser.parse_args()

    if args.cmd == "list":
        feats = prioritize(load_features())
        print(f"{'#':<3}{'Feature':<30}{'RICE':<10}")
        for i, f in enumerate(feats, 1):
            print(f"{i:<3}{f.name:<30}{f.rice_score:<10.2f}")
    elif args.cmd == "add":
        feats = load_features()
        feats.append(Feature(args.name, args.reach, args.impact, args.confidence, args.effort))
        save_features(feats)
        print("Feature added.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
