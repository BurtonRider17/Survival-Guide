CSS = r"""
@page { size: Letter; margin: 0.55in 0.65in 0.7in 0.65in;
  @bottom-left { content: "Survival Info · Vol. 1 · Electricity & Fuel"; font: 8pt 'IBM Plex Sans'; color:#7a8691; }
  @bottom-right { content: counter(page); font: 600 9pt 'IBM Plex Sans'; color:#1f4e5f; }
}
@page cover { margin: 0; @bottom-left { content: none } @bottom-right { content: none } }
* { box-sizing: border-box; }
body { font-family: 'IBM Plex Sans', sans-serif; font-size: 9.2pt; line-height: 1.36; color: #1f2a33; margin: 0; }
.cover { page: cover; width: 8.5in; height: 11in; background: #12313d; color: #fff; position: relative; overflow: hidden; break-after: page; }
.cover .band { position:absolute; left:0; right:0; top: 0; height: 0.32in; background: #e69b00; }
.cover .series { position:absolute; left: 0.8in; top: 1.0in; font: 600 13pt 'Barlow Condensed'; letter-spacing: 4px; color:#e6b54a; text-transform: uppercase; }
.cover h1 { position:absolute; left: 0.8in; top: 1.35in; margin:0; font: 800 54pt/0.95 'Barlow Condensed'; color:#fff; letter-spacing: 0.5px; }
.cover .sub { position:absolute; left:0.8in; top: 3.95in; width: 6.6in; font: 400 13.5pt/1.45 'IBM Plex Sans'; color:#cfe0e6; }
.cover .art { position:absolute; left: 0.6in; right: 0.6in; top: 5.2in; }
.cover .foot { position:absolute; left:0.8in; right:0.8in; bottom: 0.7in; font-size: 9pt; color:#9fb6bf; border-top: 1px solid #3c6070; padding-top: 10px; }
h1.part { font: 800 30pt/1 'Barlow Condensed'; color: #fff; background: #1f4e5f; margin: 0 0 14px 0; padding: 16px 18px 14px; border-left: 10px solid #e69b00; break-before: page; }
h1.part small { display:block; font: 600 11pt 'Barlow Condensed'; letter-spacing: 3px; color:#e6c27a; margin-bottom: 4px; text-transform: uppercase; }
h2 { font: 700 17pt/1.15 'Barlow Condensed'; color: #1f4e5f; margin: 16px 0 6px; padding-bottom: 3px; border-bottom: 2px solid #e69b00; break-after: avoid; }
h3 { font: 700 12.5pt/1.2 'Barlow Condensed'; color: #8a4b08; margin: 11px 0 4px; break-after: avoid; letter-spacing: 0.2px; }
p { margin: 0 0 6px; }
ul, ol { margin: 2px 0 7px; padding-left: 18px; }
li { margin-bottom: 2px; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 8.2pt; break-inside: avoid; }
th { background: #1f4e5f; color: #fff; text-align: left; padding: 4px 6px; font-weight: 600; }
td { padding: 2.5px 5px; border-bottom: 1px solid #d5dde2; vertical-align: top; }
tr:nth-child(even) td { background: #f3f7f9; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
td.bad { color:#b0b8bf; }
.box { border-radius: 6px; padding: 8px 11px 6px 40px; margin: 8px 0 10px; position: relative; break-inside: avoid; font-size: 9.2pt; }
.box::before { position:absolute; left: 10px; top: 7px; font: 800 15pt 'Barlow Condensed'; width: 22px; text-align:center; }
.box b.t { display:block; font: 700 11pt 'Barlow Condensed'; letter-spacing: .4px; text-transform: uppercase; margin-bottom: 2px; }
.danger { background: #fdecea; border: 1.5px solid #c0392b; } .danger::before { content: "!"; color:#fff; background:#c0392b; border-radius: 50%; height: 22px; line-height: 22px; font-size: 13pt; }
.danger b.t { color: #a52a1f; }
.caution { background: #fff6e0; border: 1.5px solid #e69b00; } .caution::before { content: "⚠"; color:#b97800; }
.caution b.t { color: #8a5a00; }
.tip { background: #e8f3fb; border: 1.5px solid #2f7fbf; } .tip::before { content: "i"; color:#fff; background:#2f7fbf; border-radius: 50%; height: 22px; line-height: 22px; font-size: 12pt; font-family: Georgia, serif; font-style: italic; }
.tip b.t { color: #1d5d8f; }
.formula { background: #f2f5f7; border-left: 4px solid #1f4e5f; padding: 7px 12px; margin: 7px 0 9px; font-size: 9.4pt; break-inside: avoid; }
.formula .eq { font: 600 12pt 'IBM Plex Mono', monospace; color:#12313d; display:block; margin: 2px 0; }
.check { border: 1.5px solid #2e7d32; background: #f1f8f1; border-radius: 6px; padding: 7px 11px 4px; margin: 8px 0 10px; break-inside: avoid; }
.check b.t { display:block; font: 700 11pt 'Barlow Condensed'; color: #2e7d32; text-transform: uppercase; letter-spacing: .4px; margin-bottom: 3px; }
.check ul { list-style: none; padding-left: 2px; margin: 0 0 4px; }
.check li::before { content: "☐"; color: #2e7d32; font-size: 11pt; margin-right: 6px; }
.cols2 { column-count: 2; column-gap: 18px; }
.cols2 > * { break-inside: avoid; }
figure { margin: 6px auto 10px; max-width: 88%; break-inside: avoid; text-align: center; }
figure svg { display:block; width:100%; height:auto; border: 1px solid #d5dde2; border-radius: 4px; }
figcaption { font-size: 8.4pt; color: #4b5a66; margin-top: 4px; text-align: left; }
figcaption b { color:#1f4e5f; }
.toc { margin-top: 6px; }
.toc a { color: inherit; text-decoration: none; }
.toc .tp { display:flex; font: 700 13pt 'Barlow Condensed'; color:#1f4e5f; margin: 10px 0 3px; border-bottom: 1.5px solid #e69b00; }
.toc .ts { display:flex; font-size: 9.6pt; margin: 2px 0 2px 14px; }
.toc .dots { flex: 1; border-bottom: 1px dotted #9aa7b0; margin: 0 6px 4px; }
.toc .pg { font-variant-numeric: tabular-nums; min-width: 18px; text-align: right; }
.region { border: 1px solid #c9d4da; border-radius: 6px; margin: 0 0 10px; break-inside: avoid; overflow: hidden; }
.region .rh { padding: 5px 10px; font: 700 12.5pt 'Barlow Condensed'; color:#12313d; display:flex; align-items:center; gap: 8px; }
.region .rh .n { background:#fff; border: 1.5px solid #12313d; border-radius: 50%; width: 22px; height: 22px; text-align:center; line-height: 19px; font-size: 10.5pt; }
.region .rb { padding: 5px 10px 6px; font-size: 8.9pt; }
.region .rb p { margin: 0 0 3px; }
.region .rb b { color:#1f4e5f; }
.legend { display:grid; grid-template-columns: repeat(3, 1fr); gap: 3px 12px; font-size: 8.6pt; margin: 4px 0 8px; }
.legend span.c { display:inline-block; width: 12px; height: 10px; border: 1px solid #78909c; margin-right: 5px; vertical-align: -1px; }
.small { font-size: 8.4pt; color: #4b5a66; }
.src li { margin-bottom: 4px; font-size: 8.8pt; }
.src a { color:#1d5d8f; text-decoration:none; word-break: break-all; }
.kpi { display:flex; gap: 8px; margin: 6px 0 10px; }
.kpi div { flex:1; background:#12313d; color:#fff; border-radius: 6px; padding: 7px 9px; font-size: 8.4pt; }
.kpi div b { display:block; font: 700 15pt 'Barlow Condensed'; color:#e6b54a; }
.pb { break-before: page; }
.nobreak { break-inside: avoid; }

.regions { display: grid; grid-template-columns: 1fr 1fr; gap: 9px 12px; }
.regions .region { break-inside: avoid; margin: 0; }
.regions .rb { font-size: 8.3pt; line-height: 1.36; }
.srccols { column-count: 2; column-gap: 18px; }
.srccols h3 { break-after: avoid; }
.srccols li { break-inside: avoid; }
table.brk { break-inside: auto; }
"""
