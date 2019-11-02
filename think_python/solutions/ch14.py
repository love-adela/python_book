#-------------------14.1-------------------
def sed(pattern, replace, input, output):
    fin = open(input, 'r')
    fout = open(output, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    sed('p', 'q', 'words.txt', 'output.txt')

main()

#-------------------14.2-------------------
import shelve
import sys

from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()

def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []

def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))

main(*sys.argv)


#---------------14.3---------------------
import os

def walk(dirname):
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')

d = compute_checksums(dirname='.', suffix='.py')
print_duplicates(d)

