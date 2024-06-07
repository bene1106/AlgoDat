// Abgabe 06
// Aufgabe 1b)
// Bene

// Implementieren Sie in Scala eine einfach verkettete Liste mit Hashreferenzen.
// In den Knoten der einfach verketteten Liste sollen String-Objekte gespeichert
// werden. Verwenden Sie dazu eine kryptographische Hashfunktion wie in (a).

class LinkedNodesStack[A]: 

    private class Node(val hash: String, val data: A, val next: Node)

    // Header:
    private var root : Node = null
    private var _size : Int = 0
    
    def push(data: A) : Unit =
        // Hash errechnen aus Vorgängerdaten und Vorgängerhash:
        val hash: String = if (root != null) sha256Hash(root.hash + root.data) else sha256Hash("initial")
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
