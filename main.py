"""Render a consistent travel-summary prompt from local itinerary text."""

import argparse
from pathlib import Path


def render_prompt(itinerary_details: str) -> str:
    if not itinerary_details.strip():
        raise ValueError("Provide nonempty itinerary details.")
    return f"""You are a travel assistant.
Provide a summary of the following flight itinerary:
{itinerary_details}"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--details", help="Itinerary text to insert verbatim.")
    source.add_argument("--input", type=Path, help="UTF-8 text file containing the itinerary.")
    args = parser.parse_args()
    try:
        details = args.input.read_text(encoding="utf-8") if args.input else args.details
        print(render_prompt(details))
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
