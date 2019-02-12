han=open('121.txt')

for line in han:
    line=line.rstrip()
    words=line.split()
    print("words: ", words)
    # Guardian statement:
    if len(words)<1:
        continue
    # Continue to work
    if words[0] != 'The' :
        continue
        print(words[2])
