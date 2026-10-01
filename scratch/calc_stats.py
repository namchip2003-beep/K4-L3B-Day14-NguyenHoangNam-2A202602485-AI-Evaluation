import json

bench = json.load(open('artifacts/benchmark_results.json', encoding='utf-8'))
results = bench['results']
good = [r for r in results if r['overall'] >= 0.8]
needs_work = [r for r in results if 0.6 <= r['overall'] < 0.8]
sig_issues = [r for r in results if r['overall'] < 0.6]

print(f"Good (>=0.8): {len(good)} ({', '.join(r['id'] for r in good)})")
print(f"Needs Work (0.6-0.8): {len(needs_work)} ({', '.join(r['id'] for r in needs_work)})")
print(f"Significant Issues (<0.6): {len(sig_issues)} ({', '.join(r['id'] for r in sig_issues)})")

print("\n--- Failure Types ---")
for ft in ['hallucination', 'irrelevant', 'incomplete', 'off_topic', 'refusal']:
    cnt = sum(1 for r in results if r['failure_type'] == ft)
    pct = cnt / len(results) * 100
    print(f"| {ft} | {cnt} | {pct:.1f}% |")
