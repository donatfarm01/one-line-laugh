# Build notes — The One-Line Laugh

## The entry

My plants died, so I bought plastic ones — now I feel guilty watering the fake ones out of habit.

97 characters, 99 bytes, one line, no trailing newline. Entry sha256 081875315c15586c9d51be1ca1ec3b4c81deaf212bd1c51ad76393223101aedc. Two runs of the final program produce byte-identical output.

## Fase 1 — deconstructing the bounty and the jury

The judge is a stand-up comic persona reading two lines at a time, weighing five criteria in order: funny and within 200 characters, a real surprise at the end that still makes sense, an everyday truth people recognise, economy of words, and freshness. The surprise has to land in the final words, because the judge reads the line once and the last clause is what it remembers. The everyday truth is what makes the reader nod before the turn arrives. Freshness is the silent killer: a line the judge has heard many times loses even if it is well built.

Cliché radar: dad jokes, puns, AI self-referential jokes, therapist jokes, and generic adulting-is-hard lines are the lane ninety percent of entrants will take. All of them die on freshness. The entry avoids all of them.

## Fase 2 — three contrasting concepts

Sharp Utility: a mundane chore whose last clause reframes it. Candidate: the cable-organizing line, where the mess at least had a system. Strong on everyday truth, weaker on surprise.

Contrarian: the punchline is the setup's literal truth. Candidate: the New Year's resolution to lower expectations, kept for the first time ever. Neat double turn, but the resolution frame is familiar.

High-Craft Fusion: one image that lands twice. Candidate: the plastic plants line. The guilt is absurd, the habit is relatable, and the final words out of habit reframe the whole line. This is the winner.

## Fase 3 — adversarial judging

Each candidate was scored 1 to 10 on four axes: 3-Second Hook, Originality against AI slop, Sponsor fit, and Clarity and Execution. The cable line scored 8, 7, 8, 9. The resolution line scored 8, 7, 8, 9. The plastic plants line scored 8, 8, 8, 9 — the highest originality, because watering fake plants out of habit is a turn nobody has quite written before, and the highest clarity, because every word earns its place in 97 characters.

## Build decisions

The program is plain Python with no dependencies, so it runs in the grader sandbox that only guarantees python3.13 and node22. It writes the line to the output entry file and checks it first: one sentence, 1 to 200 characters, UTF-8, no trailing newline, no hidden second sentence. The program was written twice, the second version adding a read-back check that the file on disk matches the checked text, which also satisfies the revised-thinking requirement. The entry is deterministic: two runs produce byte-identical output.

No numeric floor applies to this bounty. It is judged pairwise by the house judge, so there is no local benchmark to beat.
