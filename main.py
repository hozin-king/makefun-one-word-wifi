#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

The bounty asks for ONE word that describes Wi-Fi — the funniest AND
most accurate one. The winning word becomes the sponsor's network name,
so it has to work as an SSID you would actually laugh at when you see it
in the list, and it has to stay true the next morning.

Candidates were scored 0-5 on the four things the judges compare
pairwise: on-subject fit, funniness, truthfulness, freshness of angle.

    word        fit  funny  true  fresh  total   verdict
    OneBar       5    5      5     4      19      PICK
    Deadzone     4    4      4     3      15      a place, not the Wi-Fi
    Moody        4    4      4     3      15      personifies, but generic
    Buffering    5    2      5     1      13      the obvious answer
    Reboot       4    3      4     2      13      the fix, not the feeling
    Clingy       4    4      3     3      14      dies 3 metres from the router
    Throttled    4    2      4     2      12      true, but reads like a ticket

Why OneBar wins: everyone has lived it — the bars lie, the video freezes,
and the network list always shows the one bar you actually have. As a
network name it is a confession and a joke at once: the sponsor names
its own Wi-Fi after the signal strength nobody can escape. It is
self-deprecating instead of bragging, which is exactly the angle a
network name should take. Avoided on purpose: Ghosting, Diva,
Gaslighting, ItBurnsWhenIP — already taken by other entries.
"""

import os

ENTRY = "OneBar"

CANDIDATES = {
    # word: (fit, funny, true, fresh)
    "OneBar":    (5, 5, 5, 4),
    "Deadzone":  (4, 4, 4, 3),
    "Moody":     (4, 4, 4, 3),
    "Buffering": (5, 2, 5, 1),
    "Reboot":    (4, 3, 4, 2),
    "Clingy":    (4, 4, 3, 3),
    "Throttled": (4, 2, 4, 2),
}

TAKEN = {"Ghosting", "Diva", "Gaslighting", "ItBurnsWhenIP"}


def score(word):
    """Total score across the four judging axes (max 20)."""
    return sum(CANDIDATES[word])


def pick():
    """Best-scoring candidate that is a single word and not already taken."""
    ranked = sorted(
        (w for w in CANDIDATES if w not in TAKEN and " " not in w),
        key=lambda w: (-score(w), w),
    )
    return ranked[0]


def get_entry():
    """Return the entry word, verified against the scoring table."""
    word = pick()
    assert word == ENTRY, f"scoring drift: table picks {word}, expected {ENTRY}"
    assert " " not in word and "\n" not in word, "entry must be a single word"
    return word


def main():
    word = get_entry()
    print(word)
    print(f"score {score(word)}/20 — fit {CANDIDATES[word][0]}, "
          f"funny {CANDIDATES[word][1]}, true {CANDIDATES[word][2]}, "
          f"fresh {CANDIDATES[word][3]}")
    # The bounty scores /output/entry.txt, so write the same word there too
    # (MAKEFUN_OUTPUT_DIR names that directory when the grader sets it).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(word + "\n")
    except OSError:
        pass  # printing the word above is the entry when run outside the grader


if __name__ == "__main__":
    main()
