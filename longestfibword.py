def encodelist(inputlist):
#takes in a list of numbers or strings
#outputs a list of lists with a special encoding, the secret sauce if you will
#an input list of ['a','b','a','b','c'] will yield [[0,2],[1,3],[0,2],[1,3],[4]]
    return [[i for i,x in enumerate(inputlist) if x==l] for l in inputlist]

def sortandlistize(filename):
#takes in a word-list file
#outputs a sorted (from longest to shortest) list of lists of letters [of each word]
    wordlist = [line.strip() for line in open(filename)]
    sort_key = lambda s: (-len(s))
    return sorted([list(word) for word in wordlist],key=sort_key)

def fibseq(ndigits):
#ouputs a list of fibonacci numbers in string form, with the last number of length ndigits
    current_length = 1
    a,b=0,1
    fibsequence = [str(a),str(b)]
    while current_length < ndigits:
        a,b=b,a+b
        newnumber = str(b)
        fibsequence.append(newnumber)
        current_length = current_length+1
    return fibsequence
        
def permute(arg):
#takes in a string of numbers (ie. '123')
#outputs a list of lists of permuted strings of numbers (ie. [['1','2','3'],['12','3'],['1','23']])
    def build(arg,combo,outputlist):
        if arg: #if not at the end
            newcombo = combo + [arg[0]]
            build(arg[1:],newcombo,outputlist)
            if len(arg)>=2 and int(arg[0:2])<=25:
                    newcombo = combo + [arg[0:2]]
                    build(arg[2:],newcombo,outputlist)
        else: #reached end
            outputlist.append(combo)
    outputlist = []
    return build(arg,[],outputlist)
    

filename = "wordlist2.txt"
wordlist = sortandlistize(filename) #list of lists of letters [which concatenate to form words]
n = len(wordlist[0]) #longest word
fibnumbas = fibseq(2*n) #twice longest word (theoretical maximum)

#encode fibonacci numbers:
encodedfibnums = [encodelist(x) for x in fibnumbas]

foundbefore = False
l = n
for word in wordlist:
    encodedword = encodelist(word)
    found = [i for i,x in enumerate(encodedfibnums) if x==encodedword]
    if found:
        if foundbefore==False: #in case there's a tie b/w more than 1 word of the same length
            l = len(word)
            foundbefore = True
            print 'yay!'
        if len(word)<l:
            break
        print ''.join(word)
        for i in found: #to account for the possibility that a word has multiple fib number
            print(fibnumbas[i])

print 'the end'