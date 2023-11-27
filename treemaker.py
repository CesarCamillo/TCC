from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from Bio import Phylo
import csv
from ete3 import Tree

def matrixmaker(path, nword):
    languages=["pt","en","es","fr","it","gl","ro"]
    distances = [[0 for _ in range(7)] for _ in range(7)]

    for i in range(len(languages)):
        for j in range(i + 1, len(languages)):
            input_csv_file = path+languages[i]+'_'+languages[j]+".csv"
            with open(input_csv_file, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                total = 0.0
                sizeL1 = 0
                sizeL2 = 0
                headers = next(csv_reader)  # Lê o cabeçalho do CSV

                for row in csv_reader:
                    total += float(row[2])
                
                distances[j][i] = total/nword
    lowtri = [
            [distances[0][0]],
            [distances[1][0], distances[1][1]],
            [distances[2][0], distances[2][1], distances[2][2]],
            [distances[3][0], distances[3][1], distances[3][2], distances[3][3]],
            [distances[4][0], distances[4][1], distances[4][2], distances[4][3], distances[4][4]],
            [distances[5][0], distances[5][1], distances[5][2], distances[5][3], distances[5][4], distances[5][5]],
            [distances[5][0], distances[6][1], distances[6][2], distances[6][3], distances[6][4], distances[6][5], distances[1][6]]
        ]
    
    distance_matrix = DistanceMatrix(
        names = languages,
        matrix = lowtri
    )

    return distance_matrix           

if __name__ == "__main__":
    csv_directory = "resultados1200/"

    distance_matrix = matrixmaker(csv_directory, 1192)

    # Use o construtor de árvore de distância para criar a árvore filogenética
    constructor = DistanceTreeConstructor()
    utree = constructor.upgma(distance_matrix)

    # Salve a árvore em um arquivo no formato Newick
    output_tree_file = "phylogenetic1200_utree.xml"
    Phylo.write(utree, output_tree_file, "nexml")
    
    tree = Phylo.read("phylogenetic1200_utree.xml", "nexml")
    tree.ladderize() 
    Phylo.draw(tree)

    njtree = constructor.nj(distance_matrix)

    output_tree_file = "phylogenetic1200_njtree.xml"
    Phylo.write(njtree, output_tree_file, "nexml")

    tree = Phylo.read("phylogenetic1200_njtree.xml", "nexml")
    tree.ladderize()  
    Phylo.draw(tree)
