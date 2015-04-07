import sys
from today import read_pieces, parse_input


if __name__ == "__main__":
    usage = """
usage: agenda.py <shift in days> (0 by default)
e.g. to get reminder for yesterday:
agenda.py -1
e.g. to get reminder for the day after tomorrow:
agenda.py 2
          """
    delay = 0
    if len(sys.argv) > 1:
        delay = - int(sys.argv[1])
    else:
        print usage
    pcs = read_pieces()
    ag = parse_input(pcs, delay)

    for a in ag:
        print a.desc