finn = input("Bemeneti fájl neve: ")
foutn = input("Kimeneti fájl neve: ")

with open(finn, 'r', encoding="utf8") as fin:
    with open(foutn, 'w', encoding="utf8") as fout:
        tr = str.maketrans("íÍöÖóÓőŐüÜúÚűŰáÁéÉ", "iIoOoOoOuUuUuUaAeE")
        for line in fin:
            fout.write(line.translate(tr))
