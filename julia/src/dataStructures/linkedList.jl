"""
    ListNode{T}

Ein einzelner Knoten in einer verketteten Liste.

# Felder
- `data::T`: Die gespeicherten Daten vom Typ T
- `next::Union{ListNode{T}, Nothing}`: Verweis auf den nächsten Knoten oder `nothing` für das Ende

# Beispiel
```julia
node = ListNode{Int}(42)  # Erstellt einen Knoten mit dem Wert 42
```
"""
mutable struct ListNode{T}
    data::T                               # Die eigentlichen Daten dieses Knotens
    next::Union{ListNode{T}, Nothing}     # Zeiger zum nächsten Knoten (oder nothing am Ende)

    # Inner constructor: Initialisiert einen Knoten ohne Nachfolger
    ListNode{T}(data::T) where T = new{T}(data, nothing)
end

"""
    LinkedList{T}

Eine einfach verkettete Liste (Singly Linked List) mit Elementen vom Typ T.

# Felder
- `head::Union{ListNode{T}, Nothing}`: Verweis auf den ersten Knoten
- `size::Int`: Anzahl der Elemente in der Liste

# Konstruktor
```julia
list = LinkedList{Int}()  # Erstellt eine leere Liste für Integer
```

# Unterstützte Operationen
- `push!(list, item)`: Fügt Element am Anfang hinzu (O(1))
- `pop!(list)`: Entfernt und gibt das erste Element zurück (O(1))
- `length(list)`: Gibt die Anzahl der Elemente zurück (O(1))
- `isempty(list)`: Prüft ob die Liste leer ist (O(1))

# Beispiel
```julia
list = LinkedList{String}()
push!(list, "World")
push!(list, "Hello")
println(list)  # LinkedList{String}(["Hello", "World"])
```
"""
mutable struct LinkedList{T}
    head::Union{ListNode{T}, Nothing}     # Kopf der Liste (erstes Element oder nothing)
    size::Int                             # Anzahl der Elemente (für O(1) length())

    # Inner constructor: Erstellt eine leere Liste
    LinkedList{T}() where T = new{T}(nothing, 0)
end

"""
    push!(list::LinkedList{T}, data::T) where T

Fügt ein neues Element am Anfang der Liste hinzu (Prepend-Operation).

# Argumente
- `list`: Die LinkedList, in die eingefügt wird
- `data`: Das einzufügende Element

# Zeitkomplexität
O(1) - Konstante Zeit, da nur am Anfang eingefügt wird

# Beispiel
```julia
list = LinkedList{Int}()
push!(list, 10)
push!(list, 20)  # Liste: [20, 10]
```
"""
function Base.push!(list::LinkedList{T}, data::T) where T
    # Neuen Knoten mit den Daten erstellen
    new_node = ListNode{T}(data)

    # Den neuen Knoten an den Anfang setzen:
    # Sein "next" zeigt auf den bisherigen Kopf
    new_node.next = list.head

    # Der neue Knoten wird zum neuen Kopf
    list.head = new_node

    # Größe aktualisieren
    list.size += 1

    return list
end

"""
    pop!(list::LinkedList{T}) where T

Entfernt und gibt das erste Element der Liste zurück.

# Argumente
- `list`: Die LinkedList, aus der entfernt wird

# Rückgabe
Das entfernte Element

# Fehler
Wirft `BoundsError` wenn die Liste leer ist

# Zeitkomplexität
O(1) - Konstante Zeit, da nur vom Anfang entfernt wird

# Beispiel
```julia
list = LinkedList{Int}()
push!(list, 10)
push!(list, 20)
val = pop!(list)  # val = 20, Liste: [10]
```
"""
function Base.pop!(list::LinkedList{T}) where T
    # Fehler wenn Liste leer ist
    if list.head === nothing
        throw(BoundsError(list, 1))
    end

    # Daten des ersten Knotens speichern
    data = list.head.data

    # Kopf auf den nächsten Knoten verschieben
    # (Der alte Kopf wird vom Garbage Collector entfernt)
    list.head = list.head.next

    # Größe aktualisieren
    list.size -= 1

    return data
end

"""
    length(list::LinkedList)

Gibt die Anzahl der Elemente in der Liste zurück.

# Zeitkomplexität
O(1) - Konstante Zeit, da die Größe gespeichert wird
"""
Base.length(list::LinkedList) = list.size

"""
    isempty(list::LinkedList)

Prüft ob die Liste leer ist.

# Rückgabe
`true` wenn die Liste keine Elemente enthält, sonst `false`

# Zeitkomplexität
O(1) - Konstante Zeit
"""
Base.isempty(list::LinkedList) = list.size == 0

"""
    show(io::IO, list::LinkedList{T}) where T

Formatierte Ausgabe der Liste für die REPL.

# Zeitkomplexität
O(n) - Muss alle Elemente durchlaufen

# Beispiel
```julia
list = LinkedList{Int}()
push!(list, 1)
push!(list, 2)
println(list)  # Ausgabe: LinkedList{Int64}([2, 1])
```
"""
function Base.show(io::IO, list::LinkedList{T}) where T
    # Typ und öffnende Klammer ausgeben
    print(io, "LinkedList{$T}([")

    # Durch alle Knoten iterieren
    current = list.head
    first = true

    while current !== nothing
        # Komma zwischen Elementen (aber nicht vor dem ersten)
        if !first
            print(io, ", ")
        end

        # Aktuellen Wert ausgeben
        print(io, current.data)

        # Zum nächsten Knoten gehen
        current = current.next
        first = false
    end

    # Schließende Klammer
    print(io, "])")
end