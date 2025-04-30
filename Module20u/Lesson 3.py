scores = [54, 67, 48, 99, 27]
for name, score in enumerate(scores):
    scores[name] += 10
    print(name, score)
print(scores)