import wordfreq
import sys
import urllib.request

def check(kolla):
    text = []
    if kolla[:7] == 'http://' or kolla[:8] == 'https://':
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        response.close()
        text = lines
    else:
        f2 = open(sys.argv[2], encoding="utf-8")
        for line in f2:
            text.append(line.strip())
        f2.close()
    return text

def main():
    f1 = open(sys.argv[1], encoding="utf-8")
    stops = []
    for line in f1:
        stops.append(line.strip())
    f1.close()
    text = check(sys.argv[2])
    tokenz = wordfreq.tokenize(text)
    freks = wordfreq.countWords(tokenz, stops)
    wordfreq.printTopMost(freks, int(sys.argv[3]))

main()
