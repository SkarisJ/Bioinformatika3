from Bio.Blast import NCBIXML, NCBIWWW


def read_files(file):
    Lines = file.readlines()
    seq = []
    for line in Lines:
        seq.append(line)

    return seq


def blastSearch(seq):
    resultHandle = NCBIWWW.qblast(
        "blastn", "nt", seq, alignments=1, hitlist_size=1, entrez_query='bacteria (taxid:2)')
    records = NCBIXML.parse(resultHandle)
    for rec in records:
        for alignment in rec.alignments:
            return alignment.hit_def


if __name__ == "__main__":
    seq1 = []
    seq2 = []
    seq3 = []
    result = []
    file1 = open("peak1Seq.txt", "r")
    file2 = open("peak2Seq.txt", "r")
    file3 = open("peak3Seq.txt", "r")
    file4 = open("blastedSequences.txt", "a")

    seq1 = read_files(file1)
    seq2 = read_files(file2)
    seq3 = read_files(file3)

    for x in seq1:
        result.append(blastSearch(x))
        # result.append("\n")
    result.append("\n")
    for x in seq2:
        result.append(blastSearch(x))
        # result.append("\n")
    result.append("\n")
    for x in seq3:
        result.append(blastSearch(x))
        # result.append("\n")

    for x in result:
        file4.write(str(x))
