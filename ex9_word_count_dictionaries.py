name=input('enter file:')
try:
    handle=open(name)

    counts=dict()
    for line in handle:
        words=line.split()
        for word in words:
            counts[word]=counts.get(word,0)+1
        ##or we can write our syntax like below:
                # if word in counts:
                #   counts[word]=counts[word]+1
                # else:
                #   counts[word]=1


    bigcount=None
    bigword=None
    for word,count in counts.items():
        if bigcount is None or count>bigcount:
            bigword=word
            bigcount=count
    print(bigword,bigcount)

except:
    print('no such file!')
