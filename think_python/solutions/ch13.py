import string
import collections

def read_file(filename, skip_header=True):
    hist = collections.Counter()

    with open(filename, encoding="utf8") as fin:
        if skip_header:
                skip_gutenberg_header(fin)
        for line in fin:
            hist.update([word.strip(string.punctuation + string.whitespace).lower() for word in line.replace('-', ' ').split()])

    return hist
	
def skip_gutenberg_header(fp):
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break
                    
def freq_and_rank(hist):
    freq = list(hist.values())
    freq.sort(reverse=True)
    rank = 1
    for f in freq:
        yield rank, f
        rank += 1

def main():
    hist = read_file('emma.txt')
    for rank, freq in freq_and_rank(hist):
        print (rank, freq)	

main()
