with open('voyna_i_mir.txt', 'r', encoding= 'utf-8') as voyna_i_mir:
    full_text = voyna_i_mir.read()
    analysis_text = {}
    #total_letters = 0
    for sym in full_text:
        if sym.isalpha():
            #total_letters += 1
            if not sym in analysis_text:
                analysis_text[sym] = 1
            else:
                analysis_text[sym] += 1
    #for key, value in analysis_text.items():
        #share = round(value / total_letters, 5)
        #analysis_text[key] = share
sorted_letters = sorted(analysis_text.items(), key=lambda item: (item[1], item[0]))
for key, value in sorted_letters:
    print(f'{key} {value}')

with open('analysis.txt', 'w', encoding= 'utf-8') as analysis:
    for i, (key, value) in enumerate(sorted_letters):
        #analysis.write(f'{key} {value:.3f}\n')
        analysis.write(f'{key} {value}\n')

