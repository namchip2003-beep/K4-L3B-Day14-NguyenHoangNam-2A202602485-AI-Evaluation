import json

bench = json.load(open('artifacts/benchmark_results.json', encoding='utf-8'))
actuals = json.load(open('artifacts/actual_answers.json', encoding='utf-8'))['answers']
gold = json.load(open('golden_dataset.json', encoding='utf-8'))['qa_pairs']

actual_map = {a['id']: a for a in actuals}
gold_map = {g['id']: g for g in gold}

for tid in ['M02', 'M06', 'H04']:
    br = next(r for r in bench['results'] if r['id'] == tid)
    act = actual_map[tid]
    g = gold_map[tid]
    print(f"=== {tid} ===")
    print("Question:", g['question'])
    print("Expected Answer:", g['expected_answer'])
    print("Gold Contexts:", [c['source_doc'] for c in g['contexts']])
    print("Actual Answer:", act['actual_answer'][:300])
    print("Scores:", f"Recall: {br['context_recall']:.3f} | Precision: {br['context_precision']:.3f} | Faithfulness: {br['faithfulness']:.3f} | Relevance: {br['relevance']:.3f} | Completeness: {br['completeness']:.3f} | Overall: {br['overall']:.3f}")
    print("Failure Type:", br['failure_type'])
    print("Retrieved Chunks:", [(c['source_doc'], c['score'], c['chunk_id']) for c in act['retrieved_contexts']])
    print()
