# two-lines-back

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/nmlyz/two-lines-back/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/nmlyz/two-lines-back/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

A tiny program that writes two lines to your past self to a file.

The first line warns about one specific moment — a phone call at
2 a.m. — and the second line says why that moment mattered and what
changed because of it. The two lines are written as plain text, one
sentence each, with no setup and no summary after them.

The program writes the two lines to `entry.txt`:

```
Don't answer the phone at 2 a.m. when your father calls from the hospital.
The words you say half-asleep that night are the last ones he hears from you, and you will spend ten years wishing you had waited until you were awake.
```

## Run it

```sh
python3 main.py
```

The lines are written to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or to
`/output/entry.txt` when that variable is not set. The output file is
created with mode `0644`, and running the program twice produces
byte-identical output.

## Requirements

Python 3.10 or later. No third-party packages — the standard library
is all it needs.

## License

MIT. See [LICENSE](LICENSE).
