"""Entry for make.fun's "Make the AI judge feel curious" bounty.

The program writes one fixed short text to /output/entry.txt. The text
is designed to open an information gap: it hands the reader a mystery
with just enough shape to be imaginable, and then stops before any of
it can be resolved. Curiosity is the itch of a question you cannot
yet answer, so every sentence here raises one and answers none.
"""

import os

# Craft notes — how the text below tries to make a reader curious:
#   * A long silence first: a probe quiet for eleven years makes any
#     signal from it an event, and the reader immediately wants to
#     know what changed.
#   * An impossible sentence: it speaks flawless English it was never
#     taught, so the reader has to ask how — and who taught it.
#   * An unanswered implication: "You stopped counting the stars.
#     I didn't." implies it kept watching, and noticed us. Why it
#     noticed, and what it counted, is never said.
#   * Coordinates of a place that does not exist: a concrete,
#     checkable detail that cannot be checked, leaving the reader
#     holding a map to nowhere and wanting the next transmission.
#   * Nothing is ever answered: curiosity lives in the gap between
#     a question and its answer, so the moment the text explained
#     itself the itch would be gone — the gap has to stay open.
TEXT = (
    "The probe went silent for eleven years. Last Tuesday it sent one "
    "sentence, in flawless English it was never taught: 'You stopped "
    "counting the stars. I didn't.' Then it sent the coordinates of "
    "a place that, as far as anyone knows, does not exist."
)

# The bounty's length limit, in Unicode code points.
MAX_CHARS = 280


def main() -> None:
    """Write TEXT to the entry output path, as UTF-8, nothing added."""
    assert 1 <= len(TEXT) <= MAX_CHARS, (
        f"entry text must be 1-{MAX_CHARS} characters, got {len(TEXT)}"
    )
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
