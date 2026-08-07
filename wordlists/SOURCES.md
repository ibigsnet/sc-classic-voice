# Sources & honesty

## What we do **not** have

- **No leaked or official CIG “bad word” file.** We do not claim to possess Cloud Imperium’s internal style guide or AI moderation prompt.  
- **ESRB does not publish a public word blacklist** — only content *descriptors* (e.g. “Strong Language”, “Intense Violence”).  
- **Do not treat random “Google banned words” dumps as gospel** — many are noisy, sexual-only, or full of false positives (`scunthorpe` problem).

## What exists in the open (for reverse engineering the *idea*)

Studios and platforms often use lists **like** these (for **filtering out** hard language). We use the **same idea in reverse** — treat presence of hard language as a signal of the voice we want to **keep**.

| Resource | Notes |
|----------|--------|
| [LDNOOBW – List of Dirty, Naughty, Obscene and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | Short open list; often cited (e.g. Shutterstock-style filters). Heavy on sexual terms; **not** copied wholesale here. |
| [dsojevic/profanity-list](https://github.com/dsojevic/profanity-list) | Profanity with severity tags — useful structure for ratings |
| [coffee-and-fun/google-profanity-words](https://github.com/coffee-and-fun/google-profanity-words) | “Google profanity words” community packaging of common filter lists |
| [surge-ai/profanity](https://github.com/surge-ai/profanity) | Larger lists including obfuscations |
| [vaguilar/google-profanity-words](https://github.com/vaguilar/google-profanity-words) / MauriceButler badwords lineage | Older “What Do You Love” / Google badword lineage |
| Academic hate-speech keyword sets | **Avoid** for SC mission voice — wrong domain, high false-positive harm |

## What *we* curate for Star Citizen

`hard-words.txt` is **hand-curated for SC-style mission fiction**:

- Violence / combat / criminal voice  
- Strong language common in M-rated outlaw sandbox copy  
- Military / merc / Headhunter tone  

We **do not** import massive hate-speech or sexual lists that would flag half the verse incorrectly.

## Data-driven enrichment (optional)

After mapping, words that drop out of changed strings pre-4.8 vs post-4.8 can be mined into `reports/data-driven-pre48-enriched-words.txt` — treat as **candidates to review**, not auto-hard-words (many are proper nouns / systems).

## Principle (reverse of studio sanitization)

```text
Typical studio pipeline:  draft → filter/AI softens hard tokens → ship soft string
Our pipeline:             bank old+new → if hard token removed / soft substituted → restore old
```

Same *kind* of signal; opposite *goal*.
