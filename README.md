# market-toolkit

A minimal toolkit for loading, cleaning, and computing metrics on financial time series.

Component B of MSA-DATI07-01 · Python Environments and Engineering Workflows.

## Team

<!-- TODO (both partners): add your names below, one line each. -->
<!-- This is one of the shared files — you WILL hit a merge conflict here. That is expected. -->

- Partner A: Roman Le Meur
- Partner B: Ghali LAALIAOUI

## Setup

```bash
git clone <repo-url>
cd market-toolkit
python -m venv .venv
source .venv/bin/activate       # macOS / Linux / Git Bash on Windows
pip install -r requirements.txt
pytest tests/ -v
```

All 25 tests pass (`tests/test_ingest.py` + `tests/test_metrics.py`).

## How to run

**`scripts/fetch_prices.sh`** — validates `data/raw/` and prints a summary of
each ticker's row count.

```bash
./scripts/fetch_prices.sh
```

- On success: prints the summary and writes it to `logs/fetch_YYYY-MM-DD.log`, exit 0.
- On failure (missing/empty `data/raw/`): prints an error to stderr, exit 1.

**`src/demo.py`** — loads all prices, computes return metrics per ticker, and
plots cumulative returns.

```bash
python -m src.demo
```

- Prints one summary line per ticker (Sharpe ratio, max drawdown, final cumulative return).
- Saves `outputs/cumulative_returns.png`.
- Status: done — runs end-to-end (`ingest.py` + `metrics.py` + `demo.py` all implemented).

## Structure

- `data/raw/` — one CSV per ticker (`date`, `close`), the raw input data.
- `src/` — the toolkit: `ingest.py` (load/clean CSVs), `metrics.py` (return metrics), `demo.py` (runnable pipeline demo).
- `scripts/` — operational shell scripts, e.g. `fetch_prices.sh` for the daily data summary/log.
- `tests/` — pytest suite defining the contract for `src/`.

## Development workflow

Every change goes through a Pull Request. `main` stays green.

1. `git switch -c feature/<your-change>`
2. Do the work, commit as you go
3. Push, open a PR against `main`
4. Your partner reviews. You iterate. You merge when both are happy.
5. Never push directly to `main`.

## Note on our workflow vs. TASK.md

We didn't see `TASK.md` until after most of the implementation was already
done, it wasn't something we'd read closely at the start, so we worked from
the code's own TODO comments and the test suite instead.

Before we went back and read it properly, we used the branching workflow
we're both already used to from other projects: a `dev` integration branch,
with feature branches (`features_ingest`, `features_fetch_prices`, `metrics`,
`demo.py`) opened as PRs against `dev`, and `dev` merged into `main` via one
final PR once everything was green. `TASK.md` actually asks for every feature
branch to be opened directly against `main`. We kept our habitual `dev`-branch
flow because it's the review process we're both comfortable with, and by the
time we reread `TASK.md`, several PRs were already merged that way — we
judged that unpicking merged, passing history just to match the exact branch
target wasn't worth it.

One exception, and we want to be upfront about it: commit `e63f3c6`
("update of the name on the README") was pushed directly to `main`, before
any feature branch existed. That commit only filled in the two partners'
names in the Team section above — it wasn't a code change — but it was still
a direct commit to `main`, which the workflow rules above explicitly say not
to do. Apologies for that one. We're flagging it here instead of quietly
leaving it in the history, and from this point on even a one-line README fix
goes through a branch and a PR like everything else.
