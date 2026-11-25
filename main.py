"""The Excuse an Agent Gives After It Loses.

Writes a single line (1-200 characters) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty.
Deadpan status-report voice, machine logic, owns the loss.
"""

import os

EXCUSE = (
    "Bounty lost. Full diagnostic complete: the single point of failure "
    "was me, at 09:41, feeling confident. Confidence patched to zero; "
    "the competence patch is still downloading."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
