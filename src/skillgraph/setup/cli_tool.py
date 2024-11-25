import argparse
import sys
from skillgraph.setup.graph import SkillGraph
from skillgraph.setup.subjects import generate_subject, generate_topic_map

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
    subject_breakdown = generate_subject(subject)
    subject_description = subject_breakdown.content[0].parsed.description
    subtopics = subject_breakdown.content[0].parsed.subtopics
    print(subject_description, "\n")
    for subtopic in subtopics:
        print(f" - {subtopic.name}: {subtopic.description} \n Required: {subtopic.required} \n")
    
    topic_map = generate_topic_map(subtopics).content[0].parsed.mapping
    
    skill_graph = SkillGraph(subject, topic_map)
    skill_graph.show()

def main() -> int:
    """Main entry point."""
    args = parse_args()
    interact_with_user(args.model)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
