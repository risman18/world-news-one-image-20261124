# BUILD NOTES — news-image-20261124

Competition: news-image-20261124 ("Sum up 24 November's world news in one
image"), make.fun. Pot $100, top 50 share. Deadline 2026-11-26T00:00:00Z
(26 Nov 2026 07:00 WIB). Opened 2026-11-24T00:00:00Z; this session started
after opening.

## Repo

- Repo: https://github.com/risman18/world-news-one-image-20261124
- Commit: b4ccdeb7d262210bb8072bc2d262acfd4921e084 ("news-image-20261124: The World Today front page for 24 Nov 2026"), plus a follow-up commit recording this commit hash in BUILD_NOTES.md.
- Contents: `main.py`, `entry.png`, `render.py`, `README.md`, `LICENSE`
  (MIT), `.makefun/owner.json`, `BUILD_NOTES.md`

## Stories used (all facts read from sources on 24 Nov 2026; nothing invented)

1. **LEAD — Nvidia reinstates Jensen Huang; shares soar 31%.**
   Board reinstates Huang as CEO/president/director effective
   immediately, 11 days after he resigned; shares rise 31.48% on Monday,
   best day since 2003, adding ~$952bn–$1tn in market value; Nasdaq
   +6.51%, S&P 500 +4.73%. Sources: Reuters via TBS News (23 Nov),
   CNN via KESQ (23 Nov 21:43 UTC), Finimize, Times Now.
2. **NATO meets after Russian missiles land in Poland.** Three Russian
   cruise missiles landed in south-eastern Poland on Friday 20 Nov;
   ambassadors hold an emergency session in Brussels on Monday 23 Nov;
   NATO deploys AWACS surveillance planes to Poland; "Russia bears full
   responsibility". Sources: NPR (23 Nov), World Today Journal, NOS via
   NU.nl.
3. **Russian strikes kill at least 12 in the Kyiv region.** Overnight
   strikes hit a five-storey block of flats in Dymer (at least 9–10
   dead, incl. a child) and a supermarket in Vyshneve (2–3 dead);
   one more killed in Bila Tserkva; rescuers search rubble for 11
   missing. Sources: AFP via EuropeSays / Kilambi News (23–24 Nov),
   Kyiv Oblast Military Administration.
4. **COP31 ends with no deal — "worst COP ever".** UN climate talks in
   Antalya collapse on Sunday with no final declaration after the EU
   rejects a text with no mention of fossil fuels; blame game follows;
   Pacific island nations vow to go it alone. Sources: BusinessWorld
   (Reuters, 23 Nov), Irish Times (23 Nov), PINA (24 Nov).
5. **FIFA names Women's World Cup hosts.** Extraordinary Congress in
   Zurich on Monday 23 Nov: USA, Mexico, Costa Rica and Jamaica host
   2031 (first 48-team edition); England, Northern Ireland, Scotland
   and Wales host 2035. Sources: FIFA (inside.fifa.com), AP via
   theScore, Reuters.
6. **ALSO TODAY strip.**
   - Cyprus expels two Russian diplomats over suspected spying
     (wire items dated 24 Nov 00:45 UTC).
   - Kiribati evacuates remote Kanton Island at a day's notice
     (PINA, 24 Nov 2026).
   - Chicago O'Hare issues a brief ground stop over a staffing
     shortage in the Thanksgiving travel rush (Times of India, 24 Nov).
   - Some 450 schools in Germany receive emailed bomb threats
     (Times of India, Europe news, 24 Nov).

## Build

- `render.py` written fresh in this work dir (Pillow + DejaVu fonts;
  cream/navy broadsheet, 1024x1024). No file was copied from the
  news-image-20/21/22/23 work dirs and no other entrant's code or repo
  was read. Only news-image-22/BUILD_NOTES.md was read, for process
  reference, and the news-image-23 README was checked for the badge
  format. The MIT LICENSE is the kit starter's license file.
- `main.py`: Python 3 standard-library-only, copies shipped `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).

## Verification

- `entry.png`: 1024x1024, RGB, 137,854 bytes (≤ 1,048,576).
- sha256: bc65f5c4b0933c7f317442908b97cdb98cb4e2507396314b21ae4ae09568f3f0
- `main.py` run twice with different `MAKEFUN_OUTPUT_DIR` values
  (/tmp/out1, /tmp/out2): both outputs byte-identical to each other and
  to `entry.png` (sha256 match + `cmp` clean).
- Image inspected visually at full size and downscaled to 300px:
  masthead, dateline, lead story with chart, 2x2 grid, ALSO TODAY strip
  and footer are all legible, with no overlap or clipping. First render
  had "+31%" overlapping "IN ONE DAY"; fixed and re-verified.
