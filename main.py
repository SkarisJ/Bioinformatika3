from Bio import SeqIO
import matplotlib.pyplot as plt


def countCandG(sequence, frequencies):
    freq = round(
        ((sequence.count("C") + sequence.count("G")) / len(sequence)), 2)
    frequencies.append(freq)


def read_file(sequences, frequencies):
    array = []
    for seq_record in SeqIO.parse(file_name, "fastq"):
        sequences.append(seq_record.id)
        sequences.append(seq_record.seq)
        array.append(countCandG(seq_record.seq, frequencies))


def analyze_c_g():
    for i in range(0, 100):
        x.append(i / 100)
    for z in x:
        y.append(frequencies.count(z))
    plt.plot(x, y)
    plt.xlabel('C/G nukletidų dalis read’o sekoje')
    plt.ylabel('read’ų skaičius')
    plt.show()


def peakSearch(frequencies, peak, sequences):
    count = 0
    ids = []
    seq = []
    for value in frequencies:
        if float(value) == peak:
            if count < 5:
                ids.append(sequences[(frequencies.index(value) * 2)])
                ids.append("\n")
                seq.append(sequences[(frequencies.index(value) * 2)+1])
                seq.append("\n")
                sequences.pop(frequencies.index(value) * 2)
                sequences.pop(frequencies.index(value) * 2)
                frequencies.remove(value)
                count = count + 1
    seq.append("\n")

    return ids, seq


if __name__ == "__main__":
    file_name = "reads_for_analysis.fastq"
    sequences = []
    frequencies = []
    x = []
    y = []
    peak1Id = []
    peak1Seq = []
    peak2Id = []
    peak2Seq = []
    peak3Id = []
    peak3Seq = []
    read_file(sequences, frequencies)
    analyze_c_g()

    first = 0.34
    second = 0.54
    third = 0.70

    peak1Id, peak1Seq = peakSearch(frequencies, first,  sequences)
    peak2Id, peak2Seq = peakSearch(frequencies, second,  sequences)
    peak3Id, peak3Seq = peakSearch(frequencies, third,  sequences)

    file1 = open("peak1Id.txt", "a")
    file2 = open("peak1Seq.txt", "a")
    file3 = open("peak2Id.txt", "a")
    file4 = open("peak2Seq.txt", "a")
    file5 = open("peak3Id.txt", "a")
    file6 = open("peak3Seq.txt", "a")

    for x in peak1Id:
        file1.write(str(x))

    for x in peak1Seq:
        file2.write(str(x))

    for x in peak2Id:
        file3.write(str(x))

    for x in peak2Seq:
        file4.write(str(x))

    for x in peak3Id:
        file5.write(str(x))

    for x in peak3Seq:
        file6.write(str(x))
