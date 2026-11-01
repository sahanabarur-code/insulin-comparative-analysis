from Bio import SeqIO

print("Species    Length  Cysteines  Hydrophobic%")

   for record in SeqIO.parse("insulin.fasta", "fasta")
    seq = str(record.seq)
    length = len(seq)

    cysteines = seq.count("C")

    hydro_count = 0
    for letter in "AVLIMFW":
        hydro_count = hydro_count + seq.count(letter)

    hydro_percent = hydro_count / length * 100

    print(f"{record.id:<10} {length:<7} {cysteines:<10} {hydro_percent:.1f}")
