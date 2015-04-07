import sys
import getopt
import time
from datetime import date, timedelta

from Piece import LearnedPiece


def add_piece(topic, *tags):
    piece = LearnedPiece(topic, tags)
    pieces.append(piece)


def add_past_piece(n, topic, *tags):
    piece = LearnedPiece(topic, tags, date.today() - timedelta(days=n))
    pieces.append(piece)


def add_y_piece(topic, *tags):
    add_past_piece(1, topic, *tags)


def write_to_file():
    p = ""
    for s in pieces:
        p += str(s) + '\n'
    f = open('pieces', 'a')
    f.write(p) 
    f.close()


if __name__ == "__main__":
    pieces = []
    usage = """
ERROR!!  >.<
use as
add.py <-y> <-p days> "Learned piece description" <optional tags>
e.g.
add.py "Learned today piece" web js py cs
add.py -y "Learned yesterday" hh java
add.py -p 3 "Smth learned 3 days ago without tags"
          """
    if len(sys.argv) < 2:
        print usage
        time.sleep(0.1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:y")
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    opt_dic = dict(opts)
    for opt in opt_dic.keys():
        if opt in ("-y", "--yesterday"):
            add_y_piece(*args)
            break
        elif opt in ("-p", "--past"):
            d = int(opt_dic.get(opt))
            add_past_piece(d, *args)
            break
    if len(opts) == 0:
        add_piece(*args)

    write_to_file()
