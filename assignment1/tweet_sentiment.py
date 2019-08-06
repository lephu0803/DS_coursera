import sys

def hw():
    print('Hello, world!')

def lines(fp):
    print (str(len(fp.readlines())))

def build_dict(affin_file):
    score = dict()
    with open(str(affin_file)) as f:
        for line in f.readlines():
            term, score = line.split('\t')
            print(type(term))
            print(score)
            score['a'] = int(score)
    print(score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    # lines(sent_file)
    # lines(tweet_file)
    build_dict(sys.argv[1])

if __name__ == '__main__':
    main()
