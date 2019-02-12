name=input('enter file:')
handle=open(name)

# count the word frequencies of the file；
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

# figure out the most frequent word:
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print('the most frequent word is: ',bigword,'the frequency is: ',bigcount)

# create a list containing all the tuples in counts:
lst=list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)

# sorted the list in reverse order:
lst=sorted(lst,reverse=True)

# print out the five most frequent words:
print('the five most frequent words are: ')
for key,val in lst[:5]:
    print(key,val)
