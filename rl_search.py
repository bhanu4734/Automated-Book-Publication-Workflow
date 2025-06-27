from storage import retrieve_similar

def rl_search(query: str):
    results = retrieve_similar(query)
    print("Top Relevant Versions:")
    for i, doc in enumerate(results[0], 1):
        print(f"\n--- Version {i} ---\n{doc[:500]}...\n")
