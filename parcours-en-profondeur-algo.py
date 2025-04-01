import collections

def dfs_lwpt(graph):
    """
    Implémente l'algorithme de parcours en profondeur (DFS) et calcule les valeurs lwpt.

    Args:
        graph: Un dictionnaire représentant le graphe sous forme de listes d'adjacence.
                    Par exemple: {'A':, 'B': ['A', 'D'], 'C': ['A', 'E'], 'D':, 'E': ['C']}

    Returns:
        Un tuple contenant :
            - pere: Un dictionnaire stockant le parent de chaque sommet dans l'arbre DFS.
            - num: Un dictionnaire stockant le numéro de découverte (temps de découverte) de chaque sommet.
            - lwpt: Un dictionnaire stockant la valeur lwpt de chaque sommet.
    """
    n = len(graph)
    sommets = list(graph.keys())
    num = {sommet: 0 for sommet in sommets}
    lwpt = {sommet: 0 for sommet in sommets}
    pere = {sommet: None for sommet in sommets}
    k = 1

    def dfslwpt_recursive(x):
        nonlocal k
        lwpt[x] = num[x]
        for y in graph[x]:
            if num[y] == 0:
                pere[y] = x
                num[y] = k
                k += 1
                dfslwpt_recursive(y)
                lwpt[x] = min(lwpt[y], lwpt[x])
            elif y != pere[x]:  # Condition pour éviter de considérer l'arête vers le parent comme une arête de retour dans ce contexte
                lwpt[x] = min(num[y], lwpt[x])

    # Choisir un sommet de départ arbitraire (le premier de la liste)
    if sommets:
        start_node = sommets[0] # Correction : utiliser le premier élément de la liste
        num[start_node] = k
        k += 1
        dfslwpt_recursive(start_node)

    return pere, num, lwpt

# Exemples de graphes pour le test

# Exemple 1: Un graphe planaire simple (un cycle)
graph_planaire_cycle = {
    'A':[],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D':[],
    'E': ['C', 'D']
}

# # Exemple 2: Un graphe planaire (K4)
# graph_planaire_k4 = {
#     '1': ['2', '3', '4'],
#     '2': ['1', '3', '4'],
#     '3': ['1', '2', '4'],
#     '4': ['1', '2', '3']
# }

# # Exemple 3: Un graphe non planaire (K5 - incomplet ici pour démonstration)
# graph_non_planaire = {
#     'A': [],
#     'B': ['A', 'C', 'E'],
#     'C': [],
#     'D': ['A', 'C', 'E'],
#     'E': []}

# Tester l'algorithme sur les exemples
print("Résultats pour le graphe planaire (cycle):")
pere_cycle, num_cycle, lwpt_cycle = dfs_lwpt(graph_planaire_cycle)
print("Parent:", pere_cycle)
print("Numéro DFS:", num_cycle)
print("LWPT:", lwpt_cycle)
print("-" * 30)

# print("Résultats pour le graphe planaire (K4):")
# pere_k4, num_k4, lwpt_k4 = dfs_lwpt(graph_planaire_k4)
# print("Parent:", pere_k4)
# print("Numéro DFS:", num_k4)
# print("LWPT:", lwpt_k4)
# print("-" * 30)

# print("Résultats pour le graphe non planaire (K5 incomplet):")
# pere_non_planaire, num_non_planaire, lwpt_non_planaire = dfs_lwpt(graph_non_planaire)
# print("Parent:", pere_non_planaire)
# print("Numéro DFS:", num_non_planaire)
# print("LWPT:", lwpt_non_planaire)
# print("-" * 30)

# # Exemple de graphe plus complexe (tiré d'un exemple de parcours DFS)
# graph_complexe = {
#     '0': ['1', '2'],
#     '1': ['0', '3', '4'],
#     '2': ['0', '5'],
#     '3': ['1', '6'],
#     '4': ['1', '6'],
#     '5': ['2', '6'],
#     '6': ['3', '4', '5']
# }

# print("Résultats pour le graphe complexe:")
# pere_complexe, num_complexe, lwpt_complexe = dfs_lwpt(graph_complexe)
# print("Parent:", pere_complexe)
# print("Numéro DFS:", num_complexe)
# print("LWPT:", lwpt_complexe)
# print("-" * 30)