#!/usr/bin/env python3
"""Turning It Off — make.fun entry.

Prints the single-line entry for the competition
"Have You Tried Turning It Off?" (u-motasimfuad-have-you-tried-turning-it-off-154a938b):
one funny line a hopeless tech support agent says to a desperate customer.

Why this line (scored 24/25 against the judge's brief, see CANDIDATES.md):
the joke escalates in a rule of three — router, computer, then the agent's
own will to live — and the agent gives up so completely he tells the customer
to unplug the machine and let them both move on. The humour comes from the
agent's cheerful uselessness, never from mocking the customer, and it nods
at the "turn it off" classic with "just unplug it" instead of quoting it.

The entry is a fixed string, 131 characters, well under the 200-character
gate. The program is deterministic: it always prints exactly the same line,
and writes the same bytes to /output/entry.txt when that directory is
available (the program/v1 harness gate reads that file).
"""

# The em dash is written as an escape so the source stays plain ASCII;
# the printed line itself carries the real U+2014 character.
ENTRY = "Sir, I've restarted your router, your computer, and my will to live \u2014 at this point, please just unplug it and let us both move on."

def main():
    print(ENTRY)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
