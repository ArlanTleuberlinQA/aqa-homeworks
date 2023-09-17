symbols = input("Input any symbols: ")
item_counts = {}
for i in symbols:
    item_counts[i] = item_counts.get(i, 0)+1
result = " ".join(f"{i},{count}" for i, count in item_counts.items())
print(result)
