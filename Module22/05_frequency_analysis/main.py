with open('text.txt', 'r') as text:
    text_r = text.read().lower()
    analysis_text = {}
    total_count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for sym in text_r:
        if sym in alphabet:
            total_count += 1
            if not sym in analysis_text:
                analysis_text[sym] = 1
            else:
                analysis_text[sym] += 1
    for key, value in analysis_text.items():
        share = round(value / total_count, 3)
        analysis_text[key] = share
sorted_items = sorted(analysis_text.items(), key=lambda item: (-item[1], item[0]))
for key, value in sorted_items:
    print(f'{key} {value}')

with open('analysis.txt', 'w', encoding= 'utf-8') as analysis:
    for i, (key, value) in enumerate(sorted_items):
        analysis.write(f'{key} {value:.3f}\n')

