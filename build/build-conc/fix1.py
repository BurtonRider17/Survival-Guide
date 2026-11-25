s = open('cdiag.py').read()
rep = [
 ('["lime putty", "sand"]', '["putty", "sand"]'),
 ('"lime putty": LIME,', '"putty": LIME,'),
 ('unit = 34; x0 = 210', 'unit = 30; x0 = 205'),
 ('b += lead(cx + 70, cy + 160, cx + 92, cy + 96) + t(cx + 30, cy + 172, "concrete 75–100 mm (3–4 in)", 9.5)',
  'b += lead(250, 48, 231, 84) + t(240, 44, "concrete wall 75–100 mm", 9.5)'),
 ('b += dim(545, 230, 545, 300, "", vertical=True) + t(556, 262, "T ≥ wall thickness", 9.5) + t(556, 275, "(min 6–8 in)", 9.5)',
  'b += dim(560, 230, 560, 300, "", vertical=True) + t(566, 300, "T", 10, weight="700")'),
 ('"W ≈ 2 × wall thickness (min 12 in / 300 mm)"', '"W ≈ 2 × wall thickness (min 12 in / 300 mm);  T ≥ wall thickness (min 6–8 in)"'),
 ('b += t(240, 222, "keyway (optional)", 8.8)', 'b += t(395, 242, "keyway (optional)", 8.8)'),
 ('b += t(600, 250, "2–3 #4 (½ in) bars", 9.8) + t(600, 263, "≥ 3 in (75 mm) cover", 9.8) + t(600, 276, "on stone/brick chairs", 9.8) + lead(598, 258, 466, 276)',
  'b += t(585, 245, "2–3 #4 (½ in) bars,", 9.8) + t(585, 258, "≥ 3 in (75 mm) cover,", 9.8) + t(585, 271, "on stone/brick chairs", 9.8) + lead(583, 254, 466, 276)'),
 ('arcs = [(-75, -15), (15, 75), (105, 165), (195, 255)]', 'arcs = [(-58, -24), (24, 58), (122, 156), (204, 238)]'),
 ("x0, y0 = cx + R * 1.2 * math.cos(r0), cy + R * 0.95 * math.sin(r0)", "x0, y0 = cx + R * 1.55 * math.cos(r0), cy + R * math.sin(r0)"),
 ("x1, y1 = cx + R * 1.2 * math.cos(r1), cy + R * 0.95 * math.sin(r1)", "x1, y1 = cx + R * 1.55 * math.cos(r1), cy + R * math.sin(r1)"),
 ('A{R*1.2},{R*0.95} 0 0 1', 'A{R*1.55},{R} 0 0 1'),
 ('X, Y = 30, 50\n    iw, ih = 80, 40', 'X, Y = 55, 50\n    iw, ih = 75, 40'),
 ("b += f'<ellipse cx=\"55\" cy=\"0\" rx=\"18\" ry=\"12\" transform=\"translate({X2},{yy-4})\" fill=\"{CLAY}\" stroke=\"{INK}\"/>' + arrow(X2 + 55, yy - 16, X2 + 55, yy + 8, RED, 1.4, \"arr\")",
  "b += f'<ellipse cx=\"{X2+55}\" cy=\"{yy+12}\" rx=\"20\" ry=\"10\" fill=\"{CLAY}\" stroke=\"{INK}\"/>' + arrow(X2 + 55, yy - 14, X2 + 55, yy + 2, RED, 1.4, \"arr\")"),
 ('b += t(X + 120, 82, "loose cover of old brick / iron sheet;", 8.6, "middle") + t(X + 120, 50, "gaps adjusted to control draft", 8.6, "middle")',
  'b += t(X + 120, 50, "loose cover of old brick / iron sheet;", 8.6, "middle") + t(X + 120, 63, "gaps adjusted to control draft", 8.6, "middle")'),
 ('X, Y = 60, 50; W, H = 24 * s, 20 * s', 'X, Y = 50, 50; W, H = 24 * s, 20 * s'),
 ('"≈ 13 × 19 ft"', '"≈ 14 × 20 ft inside"'), ('"≈ 9½ × 11 ft"', '"≈ 9½ × 12 ft"'),
 ('R = 560; Lx = 10', 'R = 545; Lx = 10'),
 ('"Reinforced concrete bond beam: 2 #4", "bars continuous around the whole house"', '"Concrete bond beam: 2 #4 bars,", "continuous around the house"'),
 ('"Metal roofing on purlins; overhang", "≥ 18–24 in (more for earth walls)"', '"Metal roofing; overhang ≥ 18–24 in", "(more for earth walls)"'),
 ('"Rafter tied to plate with steel straps", "(hurricane ties) — see House Building"', '"Rafter strapped to plate (hurricane", "ties) — see House Building vol."'),
 ('"Wood plate on ½ in anchor bolts every", "4–6 ft, within 12 in of corners"', '"Plate on ½ in anchor bolts every", "4–6 ft, ≤ 12 in from corners"'),
 ('"Vertical #4 bar in grouted cells at", "corners, jambs and ≤ 4 ft apart"', '"Vertical #4 bar in grouted cells:", "corners, jambs, ≤ 4 ft apart"'),
 ('"Slab 4 in on vapor barrier, rigid", "insulation and 4–6 in compacted gravel"', '"Slab 4 in on vapor barrier, rigid", "insulation, 4–6 in gravel"'),
 ('    return svg(720, 362, b, "Rammed earth formwork")', '    return svg(720, 442, shifted(b, 80), "Rammed earth formwork")'),
 ('    return svg(720, 475, b.replace(\'y="-\', \'y="-\'), "Masonry wall cross-section")', '    return svg(720, 515, shifted(b, 40), "Masonry wall cross-section")'),
 ('for i, (n, red) in enumerate(notes): b += t(Lx, Y + 8 * s + i * 13, n, 9.2', 'for i, (n, red) in enumerate(notes): b += t(Lx, Y + 7 * s + i * 13, n, 9'),
]
for a, b in rep:
    assert a in s, a[:70]
    s = s.replace(a, b)
old = s[s.index('    notes = [("Walls: 8 in grouted block'):s.index('    for i, (n, red) in enumerate(notes)')]
new = '''    notes = [("Walls: 8 in grouted block,", 0), ("12 in brick/stone, or", 0), ("18 in rammed earth", 0), ("", 0),
             ("● vertical rebar at corners,", 1), ("both sides of openings,", 1), ("and ≤ 4 ft apart", 1), ("", 0),
             ("Openings ≥ 2 ft from corners;", 0), ("total ≤ ⅓ of wall length", 0), ("", 0),
             ("Larger windows on the south", 0), ("for winter sun; small on", 0), ("north and west", 0)]
'''
s = s.replace(old, new)
s = s.replace('def rect(x, y, w, h', 'def shifted(b, dy): return f\'<g transform="translate(0,{dy})">{b}</g>\'\n\ndef rect(x, y, w, h', 1)
open('cdiag.py', 'w').write(s)
