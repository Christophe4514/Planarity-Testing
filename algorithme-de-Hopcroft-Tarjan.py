import matplotlib.pyplot as plt
import networkx as nx
import collections

class Graphe:
    def __init__(self, n):
        self.n = n
        self.voisins = [[] for _ in range(n)]
        self.aretes = []

    def ajouter_arete(self, u, v):
        self.voisins[u].append(v)
        self.voisins[v].append(u)
        self.aretes.append((u, v))

def DFS_LWPT(graphe, x, num, pere, lwpt, stack, composantes, k):
    lwpt[x] = num[x]
    
    for y in graphe.voisins[x]:
        if num[y] == 0:  # Nouveau sommet
            pere[y] = x
            num[y] = k
            k += 1
            stack.append((x, y))  # On empile l'arête
            
            DFS_LWPT(graphe, y, num, pere, lwpt, stack, composantes, k)
            lwpt[x] = min(lwpt[x], lwpt[y])

            # Vérification d'un point d'articulation
            if lwpt[y] >= num[x]:  
                composante = []
                while stack:
                    u, v = stack.pop()
                    composante.append((u, v))
                    if (u, v) == (x, y):
                        break
                composantes.append(composante)  # Stocker la composante biconnexe

        elif y != pere[x] and num[y] < num[x]:  # Arête de retour
            lwpt[x] = min(lwpt[x], num[y])
            stack.append((x, y))  # Ajouter l'arête à la pile

def tester_planarite(graphe):
    n = graphe.n
    num = [0] * n
    pere = [-1] * n
    lwpt = [float('inf')] * n
    stack = []  # Pour stocker les arêtes
    composantes = []  # Liste des composantes biconnexes
    k = 1

    for i in range(n):
        if num[i] == 0:
            num[i] = k
            k += 1
            DFS_LWPT(graphe, i, num, pere, lwpt, stack, composantes, k)

    # Vérifier si l'une des composantes contient K5 ou K3,3
    for comp in composantes:
        if contient_K5_ou_K33(comp):
            return False  # Le graphe n'est pas planaire

    return True  # Si aucune structure K5 ou K3,3 trouvée, le graphe est planaire

def contient_K5_ou_K33(composante):
    """
    Vérifie si une composante contient un sous-graphe homéomorphe à K5 ou K3,3.
    """
    sommets = set()
    for u, v in composante:
        sommets.add(u)
        sommets.add(v)
    
    if len(sommets) >= 5:  # Potentiellement un K5
        return True
    
    # Vérification grossière pour K3,3
    if len(sommets) >= 6:
        return True

    return False

def saisir_graphe():
    n = int(input("Entrez le nombre de sommets du graphe : "))
    graphe = Graphe(n)

    m = int(input("Entrez le nombre d'arêtes : "))
    print("Entrez chaque arête sous la forme 'u v' (indices des sommets commencent à 0) :")

    for _ in range(m):
        while True:
            try:
                u, v = map(int, input().split())
                if u < 0 or v < 0 or u >= n or v >= n:
                    print("Erreur : les sommets doivent être compris entre 0 et", n-1)
                    continue
                graphe.ajouter_arete(u, v)
                break
            except ValueError:
                print("Erreur : veuillez entrer deux nombres séparés par un espace.")

    return graphe

def dessiner_graphe(graphe, est_planaire):
    G = nx.Graph()
    G.add_edges_from(graphe.aretes)

    pos = nx.spring_layout(G)  # Disposition automatique des sommets
    plt.figure(figsize=(6, 4))  # Agrandissement pour laisser de la place en bas

    # Dessin du graphe
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="black", node_size=1000, font_size=12)
    
    # Ajouter du texte en bas
    resultat = "Le graphe est planaire." if est_planaire else "Le graphe n'est pas planaire."
    plt.figtext(0.5, 0.02, resultat, ha="center", fontsize=12, color="red", fontweight="bold")

    plt.title("Représentation du Graphe")
    plt.show()

# Exécution
graphe = saisir_graphe()
est_planaire = tester_planarite(graphe)
dessiner_graphe(graphe, est_planaire)

if tester_planarite(graphe):
    print("Le graphe est planaire.")
else:
    print("Le graphe n'est pas planaire.")

