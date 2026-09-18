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
- Status: in progress (Partner B) — not yet runnable.

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
