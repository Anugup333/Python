def answer():
    s = input("Enter a string: ")
    
    # 1. check input string 
    if len(s) == 0:
        print("Invalid Input")
        return 
    
    # 2. calculate the frequency and track first occurance indices
    
    freq = {}
    freqindex = {}
    for index,i in enumerate(s):
        freq[i] = freq.get(i,0) +1
        if i not in freqindex:
            freqindex[i] = index
    
    # 3. find the non repeting character 
    # print(freq)
    nonrepch = ''
    nonrep = False
    for i in freq:
        if freq[i] == 1:
            nonrepch = i
            nonrep = True
            break

    
    # 4. most repeating charcater 
    maxfreq = max(freq.values())
    maxfreqch = ''
    indexmaxfreqch = len(s)
    for i in freq:
        if freq[i] == maxfreq:
            index = freqindex[i]
            if index < indexmaxfreqch:
                indexmaxfreqch = index 
                maxfreqch = i
    
    # 5. first repeated Charcter
    
    firstrepch = ''
    firstrep = False
    for i in freq:
        if freq[i] >1:
            firstrepch = i
            firstrep = True
            break
    
    # 6. print accordingly
    if not nonrep:
        print("None")
        if firstrep:
            print(firstrepch)
    else:
        print("First Non-Repeating Character: ",nonrepch)
        print(f"Most Repeated Character: {maxfreqch} (appears {maxfreq} times)")
    
answer()