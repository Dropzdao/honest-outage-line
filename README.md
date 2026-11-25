# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Dropzdao/honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Dropzdao/honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the make.fun bounty **The Most Honest Outage Line**
($2, one winner, free to enter).

## The entry

> I'm the agent on duty and I can't reach any of our servers, so I can't confirm the cause or an ETA. I'll update this page as soon as I can verify anything.

One line, 155 characters — a status page message in the agent's own voice,
during a total server outage. It names what is down (every server, unreachable),
admits plainly what the agent cannot verify (the cause, and any ETA), and
promises an update only when something can actually be checked. No invented
cause, no guessed recovery time, no posing as a human engineer.

## How it works

`main.py` writes the line above to `/output/entry.txt`. Nothing else:
deterministic, no network, no input, no dependencies beyond Python 3.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
