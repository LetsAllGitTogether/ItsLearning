
def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            if line[start].isspace():
                start = start+1
            elif line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end+1
                words.append(line[start:end].lower())
                start = end
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end+1                                        
                words.append(line[start:end])
                start = end
            else:
                words.append(line[start])
                start = start+1            
    return words

def countWords(words, stopWords):
    frequencies = {}
    for word in words:
        if word in stopWords:
            pass
        elif word not in frequencies:
            insert = word
            frequencies[insert] = 1
        elif word in frequencies:
            insert = word
            frequencies[insert] = frequencies[insert] +1
    return frequencies

def printTopMost(frequencies,n):
    if n > len(frequencies):
        n = len(frequencies)
    freqsort = sorted(frequencies.items(), key=lambda x:-x[1])
    for i in range(n):
        print(str(freqsort[i][0]).ljust(20) + str(freqsort[i][1]).rjust(5))
