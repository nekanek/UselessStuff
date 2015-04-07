from datetime import date, datetime
import Piece


def read_pieces(pieces=[]):
    with open('pieces', 'r') as f:
        for line in f:
            p = line.split(",")
            des = p[0]
            tags = p[1:-1]
            tags_f =[]
            for t in tags:
                tag = t[t.index("'")+1:t.rfind("'")]
                tags_f.append(tag)
            d = p[-1].strip()
            piece = Piece.LearnedPiece(des, tags_f, d)
            pieces.append(piece)
    return pieces


def parse_input(pieces, delay=0, agenda=[]):
    today = date.today()
    repeats = [1, 7, 30, 181]
    for p in pieces:
        str_date = p.date
        d = datetime.strptime(str_date, "%Y-%m-%d").date()
        diff = (today - d).days - delay
        if diff in repeats:
            agenda.append(p)
    return agenda

if __name__ == "__main__":
    pcs = read_pieces()
    ag = parse_input(pcs)
    for a in ag:
        print a.desc