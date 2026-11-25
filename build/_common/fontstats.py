import fitz, sys, collections
d = fitz.open(sys.argv[1]); c = collections.Counter()
for p in d:
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if s['text'].strip(): c[round(s['size'], 1)] += len(s['text'])
tot = sum(c.values())
print(len(d), 'pages; chars by size (pt):', sorted(((k, round(100*v/tot,1)) for k, v in c.items()), key=lambda x: x[0])[:14])
print('share < 8pt: %.1f%%  < 9pt: %.1f%%' % (100*sum(v for k,v in c.items() if k<8)/tot, 100*sum(v for k,v in c.items() if k<9)/tot))
