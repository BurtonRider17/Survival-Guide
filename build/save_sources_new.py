import sys
sys.path.insert(0, '/workspace/survival-info')
import save_sources as S
S.PROFILE.mkdir(parents=True, exist_ok=True)
cache = {}
for name in sys.argv[1:]:
    s, f, notes = S.process_list(S.ROOT / f"sources-{name.lower()}.txt", name, cache)
    print("SUMMARY", name, "saved", s, "failed", f, notes, flush=True)
