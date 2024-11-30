import argparse
import sys

from skillgraph.setup.graph import build_graph_layers


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="CLI tool for skill graph generation"
    )
    parser.add_argument(
        "--model",
        type=str,
        help="The model to use for the skill graph generation",
        default="gpt-4o-2024-08-06",
    )

    return parser.parse_args()

def interact_with_user(model: str) -> None:
    """Interact with the user to generate the skill graph."""
    subject = input("Enter the subject you want to generate a skill graph for: ")

    topic_breakdowns, topic_graphs = build_graph_layers(subject)
    """
    print(topic_graphs, "\n")
    print(topic_breakdowns)
    """


def main() -> int:
    """Main entry point."""
    args = parse_args()
    interact_with_user(args.model)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
