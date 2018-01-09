from makeGraph.creaGrafo import mkGraph
from medOfNode.medNode import medNode


def mostNodes(grafo):
    """
    :param grafo:
    :return:
    """
    listNode = grafo.getNodes()
    maxMed = [[None, 0]]
    for node in listNode:
        if len(grafo.getAdj(node.id)) == 1:
            continue
        else:
            med = medNode(grafo, node)
            maxMed = findBetterNode(med, node, maxMed)
    return maxMed


def findBetterNode(numMed, node, savedNode):
    """
    :param numMed:
    :return:
    """
    if savedNode[0][0] == None or savedNode[0][1] < numMed:
        savedNode = [[node, numMed]]
    elif savedNode[0][1] == numMed:
        savedNode.append([node, numMed])
    return savedNode


if __name__ == '__main__':
    g = mkGraph(20, "rand", 5)
    listaNodi = mostNodes(g)

    print("Nodo/i medi per piu' volte:\n")

    for elem in listaNodi:
        print("Nodo {} medio per {} volte.\n".format(elem[0].id, elem[1]))
