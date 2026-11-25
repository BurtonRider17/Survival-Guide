import sys, glob
from PIL import Image
d, out, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
files = {int(f.split('-')[-1][:-4]): f for f in glob.glob(d + '/p-*.png')}
for gi in range(0, len(pages), 2):
    ims = [Image.open(files[p]) for p in pages[gi:gi+2]]
    W = sum(i.width for i in ims) + 10; H = max(i.height for i in ims)
    s = Image.new('RGB', (W, H), 'gray'); x = 0
    for i in ims: s.paste(i, (x, 0)); x += i.width + 10
    s.save(f'{out}{gi//2}.png')
