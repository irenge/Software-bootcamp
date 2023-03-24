sample = "google.com"
freq = {}

for s in sample:
    if s in freq:
        freq[s] += 1
    else:
        freq[s] = 1

    
print(freq)
