# Survival Info

A knowledge-retention survival library for North America. These are printable, long-term, grid-down guides meant to keep practical skills available if industrial infrastructure were lost. The series covers the United States (including Puerto Rico), Canada, Mexico, and, where it is relevant, Central America and Cuba.

This repository publishes **19 guides** (816 pages) and a 12-page series index. Start with [`guides/Survival_Info_Index.pdf`](guides/Survival_Info_Index.pdf). Each guide is a single combined PDF in [`guides/`](guides/).

The **Bunkers** volume (a directory of sites and listings) is kept offline and is not in this repository. The index PDF was last rebuilt on November 24, 2026, when that volume was still part of the set, so it still lists 20 guides and 1,039 pages and still names the Bunkers file. It does not contain site addresses or coordinates.

## Guides

| # | Guide | Pages | File |
|---|---|---:|---|
| 1 | Water | 57 | [Survival_Info_Water.pdf](guides/Survival_Info_Water.pdf) |
| 2 | Food | 49 | [Survival_Info_Food.pdf](guides/Survival_Info_Food.pdf) |
| 3 | Electricity & Fuel | 53 | [Survival_Info_Electricity.pdf](guides/Survival_Info_Electricity.pdf) |
| 4 | Concrete & Masonry | 60 | [Survival_Info_Concrete.pdf](guides/Survival_Info_Concrete.pdf) |
| 5 | Tools & Blacksmithing | 52 | [Survival_Info_Tools.pdf](guides/Survival_Info_Tools.pdf) |
| 6 | House Building | 58 | [Survival_Info_House.pdf](guides/Survival_Info_House.pdf) |
| 7 | Medical & First Aid | 40 | [Survival_Info_Medical.pdf](guides/Survival_Info_Medical.pdf) |
| 8 | Sanitation & Hygiene | 32 | [Survival_Info_Sanitation.pdf](guides/Survival_Info_Sanitation.pdf) |
| 9 | Fire & Heating | 32 | [Survival_Info_Fire.pdf](guides/Survival_Info_Fire.pdf) |
| 10 | Radio & Communications | 31 | [Survival_Info_Radio.pdf](guides/Survival_Info_Radio.pdf) |
| 11 | Food Preservation & Storage | 40 | [Survival_Info_Preservation.pdf](guides/Survival_Info_Preservation.pdf) |
| 12 | Hunting, Trapping & Fishing | 34 | [Survival_Info_Hunting.pdf](guides/Survival_Info_Hunting.pdf) |
| 13 | Defense & Security | 33 | [Survival_Info_Defense.pdf](guides/Survival_Info_Defense.pdf) |
| 14 | Navigation & Travel | 32 | [Survival_Info_Navigation.pdf](guides/Survival_Info_Navigation.pdf) |
| 15 | Weather & Natural Disasters | 31 | [Survival_Info_Weather.pdf](guides/Survival_Info_Weather.pdf) |
| 16 | Gardening & Seed Saving | 34 | [Survival_Info_Gardening.pdf](guides/Survival_Info_Gardening.pdf) |
| 17 | Livestock & Small Animals | 30 | [Survival_Info_Livestock.pdf](guides/Survival_Info_Livestock.pdf) |
| 18 | Medicine & Remedies | 73 | [Survival_Info_Medicine.pdf](guides/Survival_Info_Medicine.pdf) |
| 19 | Chemistry | 45 | [Survival_Info_Chemistry.pdf](guides/Survival_Info_Chemistry.pdf) |
| | **Total** | **816** | |
| | Series index | 12 | [Survival_Info_Index.pdf](guides/Survival_Info_Index.pdf) |

Most guides end with a US-patent appendix, sorted from simple hand-built devices to workshop and industrial equipment, with key drawings shown full width. All of those patents have expired. Illustrations are drawn in code as SVG; plant photographs in the Food and Medicine guides come from Wikimedia Commons and are credited in the text.

The guides do not cover explosives, weapons, chemical weapons, or controlled-substance synthesis. Nothing in them is medical advice.

## Sources

Every source cited in a guide is saved, when the site allowed, as a PDF. Those source archives are **not stored in git**. They are attached to this repository's [Releases](https://github.com/BurtonRider17/Survival-Guide/releases) page as per-guide zip files (`Sources_<Guide>.zip`, or `Sources_<Guide>_partN.zip` when a single archive would be larger than about 23 MiB).

Bunkers source zips are not published here.

## Rebuilding

Build scripts live in [`build/`](build/). Each guide has a `build-<short>/` directory with a `build.py` that writes HTML and renders a letter-size PDF through headless Chrome, using the shared helper [`build/_common/guidekit.py`](build/_common/guidekit.py). After a rebuild, [`build/build-xref/xref.py`](build/build-xref/xref.py) replaces the companion-guides page rather than stacking a new one. [`build/split_guides.py`](build/split_guides.py) and [`build/pack_sources.py`](build/pack_sources.py) can produce phone-sized split parts and source zips. Patent appendices are added with [`build/patents/add_patents.py`](build/patents/add_patents.py) and [`build/patents/pipeline.sh`](build/patents/pipeline.sh).

Some scripts still use a local working-directory path (`/workspace/survival-info`) and may need that path adjusted to this repository layout. The series index is rebuilt from [`build/build-index/build.py`](build/build-index/build.py).
