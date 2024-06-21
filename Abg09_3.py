# Bene
# AlgoDat Aufgabe 8.3
# Rabin-Karp

# a) Implementieren Sie den naiven Algorithmus und den Algorithmus von RabinKarp zur Suche in Zeichenketten. Finden Sie dann heraus, wie oft das Wort
# whale in Moby Dick vorkommt (ignorieren Sie dabei Groß- und Kleinschreibung). Wie schneiden Ihre Implementierungen im Vergleich ab?
# Hinweis: Den Roman Moby Dick finden Sie unter
# http://www.gutenberg.org/files/2701/2701-0.txt.


# Implementierung Rabin-Karp

# Wählen:               p = 7
# suche:                Whale ODER whale
# Länge des Fensters:   l = 5
# Basis:                b = 256 (da 256 ASCII-Zeichen)

# Text bekommen von der Seite:
import requests
response = requests.get('http://www.gutenberg.org/files/2701/2701-0.txt')
if response.status_code == 200:
    text = response.text.lower()  # Text in kleinbuchstaben umwandeln
    print("Text eingelesen")
else:
    print("Text konnte nicht eingelesen werden")
    exit()

# text = "whaleewahalewhalewhale".lower()

# Werte initialisieren:
p = 7
search = "whale"
l = len(search)
b = 256


# berechnung von Faktor des Subtrahend b^(l-1) mod p:
# m = (b ** l-1) % p
m = pow(b, l-1, p)

# Rabin-Karp-Hasfunktion:
def h(string):
    ret = 0
    for i in range(l):
        ret = ret + ((ord(string[i]) * (b**i)) % p)
        # oder: ret = (ret * b + ord(string[i])) % p
    return ret

# Hash-Wert des Musters bestimmen:
patternHash = h(search)

# Hash-Wert des 1. Abschnitts bestimmen:
exerptHash = h(text[:l])

# anfangen:
counter = 0
for i in range(len(text)-l+1):
    # i = 0
    # Fall 1: Hashes matchen
    if exerptHash == patternHash:
        if text[i:i+l] == search:
            counter += 1

    # Fall 2: Hashes matchen nicht
    else:  # weiter gehen:
        # Hash des neuen Excerpts berechnen:
        exerptHash = b * (exerptHash - ord(text[i]) * m) + ord(text[i+1]) % p
        # i += 1

print(f"Das Wort '{search}' kommt {counter} mal vor.")



# -----------------------------------------------------------------------------------
# Naiver Suchalgorithmus:
def naiveSearch(text, searchpattern):
    count = 0
    for i in range(len(text) - len(searchpattern)+1):
        if text[i::i+len(searchpattern)] == searchpattern:
            count += 1
    return count


# b)
# Man kann  den Rabin-Karp-Algorithmus leicht auf mehrere Suchmuster erweitern, indem man
# am Anfang die Hashes aller Suchmuster bestimmt und dann in Fall1 des Algorithmus durch Veroderung den exerptHash mit 
# jedem möglichen SuchHash vergleicht.
# Die erste Stelle i, an der True geliefert wird ist die gesuchte Stelle:

counter = 0
for i in range(len(text)-l+1):
    # i = 0
    # Fall 1: Hashes matchen
    if exerptHash == pattern1Hash or exerptHash == pattern2Hash or exerptHash == pattern3Hash:  # ect
        if text[i:i+l] == search1 or text[i:i+l] == search2 or text[i:i+l] == search3:
            counter += 1

    # Fall 2: Hashes matchen nicht: bleibt so
    else:  # weiter gehen:
        # Hash des neuen Excerpts berechnen:
        exerptHash = b * (exerptHash - ord(text[i]) * m) + ord(text[i+1]) % p
        # i += 1
