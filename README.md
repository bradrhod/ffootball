# ffootball

A personal, non-commercial Python project for analyzing my own Yahoo Fantasy Football league(s) — rosters, matchups, standings, weekly scoring, player stats, and transactions — to support my own lineup, waiver, and trade decisions.

- **Read-only** use of the Yahoo Fantasy Sports API (OAuth 2.0)
- **Personal / single-user**: accesses only my own account and leagues
- No redistribution, no commercial use; low request volume with local caching

Fantasy data provided by Yahoo Fantasy.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
source .venv/bin/activate
```

Create an `oauth2.json` (not committed) with your Yahoo app credentials:

```json
{
    "consumer_key": "YOUR_CLIENT_ID",
    "consumer_secret": "YOUR_CLIENT_SECRET",
    "callback_uri": "https://localhost:8000"
}
```

Then run:

```bash
python test_yahoo.py
```
