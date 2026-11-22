# The World Today — Sunday, 22 November 2026

A one-image summary of the world's news of Sunday 22 November 2026,
entered in make.fun's `news-image-20261122` competition.

## The image

A newspaper front page, drawn programmatically with Python/PIL
(`render.py`) — every letter is rendered from a system font, so the text
is crisp at any size, and every picture is an original vector-style
drawing made from shapes. No photographs, no copied artwork, no
image-generator output.

- **Masthead:** "THE WORLD TODAY — SUNDAY, 22 NOVEMBER 2026"
- **Lead story — the Gulf:** Iran says its missiles and drones destroyed
  two U.S. Patriot radars at bases in Bahrain; the U.S. says nearly all
  were intercepted and reports no casualties; Bahrain says a factory
  caught fire.
- **Baltic Sea:** the sanctioned Russian cargo ship *Sparta II* is hit by
  drones, catches fire and drifts into Finnish waters; all 16 crew
  escape unhurt.
- **Ukraine:** a Russian missile strike on Kryvyi Rih kills a boy of 7
  and a paramedic, and wounds 60.
- **Hong Kong:** polls open for 723 seats on the 1,500-member Election
  Committee that picks the city's leader; 856 candidates are running.
- **Climate:** COP31 talks in Antalya run past their deadline, deadlocked
  over fossil fuels and finance.
- **Sport:** Australia bowls first in the South Africa decider; captain
  Steve Smith is out injured.

Sources: Reuters, AP, Xinhua, Al Jazeera, CNN, China Daily — reported
22 November 2026. Claims that could not be independently verified are
shown as claims, attributed to whoever made them.

## How it runs

`main.ts` (Node 22, standard library only) copies the shipped `entry.png`
to `/output/entry.png`. It runs with no network and writes the same bytes
every time.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To re-render the image from scratch: `python3 render.py` (requires Pillow
and the DejaVu fonts; it writes `entry.png` at 1024×1024, under 1 MiB).

## License

MIT — see `LICENSE`.
