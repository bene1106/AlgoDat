# Abgabe 06
# Aufgabe 2b
# Bene

# Laptop version

class TrieNode:
    def __init__(self):
        # Initialisiert ein TrieNode-Objekt mit einem leeren Dictionary für Kindknoten
        # und einem Flag, das anzeigt, ob der Knoten das Ende eines Worts darstellt.
        self.children = {}  # Dictionary: Mapping von Zeichen zu Kindknoten {'a': <TrieNode>} oder {'t': <TrieNode>, 'l': <TrieNode>}

        self.is_end_of_word = False  # Gibt an, ob der Knoten das Ende eines Worts ist
        
        # ein Knoten wird hier als ein dictionary dargestellt

def insert_word(root, word):
    # Fügt ein Wort in den Trie ein, beginnend beim Wurzelknoten.
    node = root
    for char in word:
        # Für jedes Zeichen im Wort: Wenn das Zeichen nicht in den Kindern des aktuellen Knotens ist,
        # füge einen neuen Knoten hinzu.
        if char not in node.children:
            node.children[char] = TrieNode()
            
            print(node.children , '1')
        
        # Gehe zum Kindknoten weiter.
        node = node.children[char]
        print(node.children , '2')
    # Markiere den letzten Knoten als Ende eines Worts.
    node.is_end_of_word = True
    print(node.children , '3')

def traverse_trie(root):
    # Initialisiert einen Stack für die Tiefensuche und ein Set zur Verfolgung besuchter Kanten.
    stack = [(root, "")]
    visited_edges = set()  # Set, um besuchte Kanten zu verfolgen
    
    while stack:
        # Nimm das oberste Element vom Stack.
        current_node, current_word = stack.pop()
        
        # Wenn der aktuelle Knoten das Ende eines Worts ist, drucke das aktuelle Wort.
        if current_node.is_end_of_word:
            print(current_word)
        
        # Für jedes Kind des aktuellen Knotens:
        for char, child_node in current_node.children.items():
            # Erstelle eine Kante als Tupel des aktuellen Knotens und seines Kindknotens.
            edge = (current_node, child_node)
            # Wenn die Kante nicht bereits besucht wurde oder weniger als zweimal besucht wurde,
            # füge den Kindknoten und das erweiterte Wort zum Stack hinzu und markiere die Kante als besucht.
            if edge not in visited_edges or visited_edges.count(edge) < 2:
                stack.append((child_node, current_word + char))
                visited_edges.add(edge)

# Beispiel zur Verwendung
root = TrieNode()
words = ["apple", "banana", "app", "bat", "batman"]
for word in words:
    insert_word(root, word)

traverse_trie(root)
