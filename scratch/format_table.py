import json

bench = json.load(open('artifacts/benchmark_results.json', encoding='utf-8'))
for r in bench['results']:
    q_short = r['question'][:32] + '...' if len(r['question']) > 32 else r['question']
    passed_str = 'Yes' if r['passed'] else 'No'
    ft = r['failure_type'] or '-'
    print(f"| {r['id']} | {q_short} | {r['context_recall']:.3f} | {r['context_precision']:.3f} | {r['faithfulness']:.3f} | {r['relevance']:.3f} | {r['completeness']:.3f} | {r['overall']:.3f} | {passed_str} | {ft} |")

print("\n--- Summary ---")
s = bench['summary']
print(f"Overall pass rate: {s['pass_rate']*100:.1f}%")
print(f"Avg Context Recall: {s['avg_context_recall']:.3f}")
print(f"Avg Context Precision: {s['avg_context_precision']:.3f}")
print(f"Avg Faithfulness: {s['avg_faithfulness']:.3f}")
print(f"Avg Relevance: {s['avg_relevance']:.3f}")
print(f"Avg Completeness: {s['avg_completeness']:.3f}")
print(f"Failure type distribution: {s['failure_types']}")

print("\n--- 3 Lowest ---")
sorted_res = sorted(bench['results'], key=lambda x: x['overall'])
for i, r in enumerate(sorted_res[:3], 1):
    print(f"{i}. ID: {r['id']} | Score: {r['overall']:.3f} | Failure type: {r['failure_type']}")
