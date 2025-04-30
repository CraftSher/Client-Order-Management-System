speakers_file = open('speakers.txt', 'r', encoding= 'utf-8')
data = speakers_file.read()
print(data)
speakers_file.close()