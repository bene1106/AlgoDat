import scala.compiletime.ops.double
// Abgabe 06
// Aufgabe 1c)
// Bene

// Fügen Sie zu den Knoten Ihrer einfach verketteten Liste jeweils ein Nonce
// hinzu, und stellen Sie sicher, dass die Hashwerte in den Referenzen alle mit
// acht Nullen (in der Binärdarstellung) aufhören. Wie viele Versuche sind dazu
// im Durchschnitt nötig?

// -> in push-Methode: Nonce zu gültigem Hashwert mit Schleife finden


class LinkedNodesStack[A]: 

    private class Node(val hash: String, val data: A, val next: Node)

    // Header:
    private var root : Node = null
    private var _size : Int = 0
    



    def push(data: A) : Unit =
		// Fall abfangen: leere Blockchain
		val prevhash: String = if (root != 0) root.hash else "initial"
		val prevdata: A = if (root != 0) root.data else null.asInstanceOf(A)

		// Nonce initialisieren:
		var nonce = 0
		// leeren Hashwert initialisieren:
		var hash = ""

		// Bedingung für Hashwert: Enden mit 8 Nullen
		// -> Hashwert solange erhöhen und Hashwert ausrechnen,
		// bis Hashwert mit 8 Nullen endet:

		do
			// Hashwert berechnen aus vorherigem Hash, vorherigen Daten und geratenem Nonce:
			hash = sha256Hash(prevhash + prevdata + nonce)
			// Nonce erhähen für nächsten Versuch:
			nonce += 1
		// prüfen, ob Hashwert mit 8 Nullen endet:
		while hash.last == '0'  // Quelle von .last: Stackoverflow

        // neuen Knoten oben auf den Stack pushen mit errechnetem Hash:
        root = Node(hash, data, root)
        _size = _size + 1





    def pop() : A =
        if !isEmpty then
            val result: A = root.data
            // If the top node was simultaneously the last node
            // in the chain, root becomes null:
            root = root.next
            _size = _size - 1
            result
        else throw Exception("Stack is empty")

    def top : A =
        if !isEmpty then root.data
        else throw Exception("Stack is empty")

    // If the stack is empty, than its size is 0 and
    // the root is just null.
    def isEmpty : Boolean = root == null
    def size : Int = _size 

// Hashfunktion anwenden: Quelle: StackOverflow
import java.security.MessageDigest
import java.nio.charset.StandardCharsets

def sha256Hash(text: String): String = 
    val digest = MessageDigest.getInstance("SHA-256")
    val hashBytes = digest.digest(text.getBytes(StandardCharsets.UTF_8))
    hashBytes.map("%02x".format(_)).mkString
    
@main
def main(): Unit =
    val stack: LinkedNodesStack[String] = new LinkedNodesStack[String]
    stack.push("hello")
    stack.push("hi")
    stack.push("hai")
