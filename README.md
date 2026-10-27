# Itinerary Prompt Template

Render a consistent prompt for summarizing a flight itinerary. An f-string inserts local itinerary details into a fixed instruction so repeated uses retain the same wording and structure. This tiny example demonstrates template rendering; it does not call a model, summarize the itinerary, book travel, or transmit the input.

## Run

Requires Python 3.10 or newer and no external packages.

```powershell
python -B main.py --details "Example flight ZX123: Chicago to Boston, November 2, departure 09:00, arrival 12:10."
python -B main.py --input itinerary.txt
```

The input file must contain UTF-8 text. The generated prompt is printed to stdout. Input is inserted verbatim, including braces and line breaks; empty input is rejected. Itinerary contents remain untrusted data when passed to any downstream model. This template alone provides no prompt-injection protection or factual verification.

## Code map

| File | Responsibility |
|---|---|
| `main.py` | `render_prompt` inserts the itinerary into the f-string; the CLI reads either inline text or a local file and prints the result. |
| `requirements.txt` | Records the standard-library-only runtime requirement. |
| `.gitignore` | Excludes caches, environments, local configuration, and generated data. |

One source file handles the complete flow: local text → template rendering → stdout.
