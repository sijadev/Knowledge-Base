# Lehrplan: Algorithmen und Datenstrukturen mit Julia & VS Code

## Setup: VS Code + Julia Entwicklungsumgebung

### Installation und Konfiguration:
```bash
# 1. Julia installieren (https://julialang.org/downloads/)
# 2. VS Code installieren
# 3. Julia Extension in VS Code installieren
# 4. Wichtige Packages installieren:
```


### VS Code Julia-Workflow:
- **Julia REPL integriert:** `Ctrl+Shift+P` → "Julia: Start REPL"
- **Code ausführen:** `Ctrl+Enter` (aktuelle Zeile), `Shift+Enter` (Block)
- **Plots anzeigen:** Automatisch im Plot-Panel
- **Debugging:** Eingebauter Julia-Debugger
- **Package-Management:** Direkt im REPL

## Phase 1: Julia-Grundlagen und Komplexitätsanalyse (2-3 Wochen)

### Woche 1: Julia-Grundlagen und Komplexitätsanalyse
**Lernziele:**
- Julia-Syntax und 1-based indexing verstehen
- Multiple dispatch kennenlernen
- Big-O Notation mit BenchmarkTools messen
- Zeitkomplexität vs. Speicherkomplexität

**Julia-spezifische Themen:**
- Arrays: `Vector{Int}`, `Matrix{Float64}`
- Funktionsdefinition und Multiple dispatch
- Type annotations für Performance
- @time, @benchmark Makros für Messung

**Praktische Übungen:**
```julia
using BenchmarkTools, Plots

# Komplexitätsanalyse visuell
function measure_complexity(func, input_sizes)
    times = Float64[]
    for n in input_sizes
        data = rand(1:1000, n)  # 1-based indexing!
        time = @belapsed $func($data)
        push!(times, time)
    end
    return times
end

# Verschiedene Algorithmen vergleichen
function linear_search(arr::Vector{Int}, target::Int)
    for i in 1:length(arr)  # 1-based!
        if arr[i] == target
            return i
        end
    end
    return nothing
end

# Plot erstellen
sizes = [100, 500, 1000, 2000, 5000]
times = measure_complexity(linear_search, sizes)
plot(sizes, times, label="Linear Search", xlabel="Input Size", ylabel="Time (s)")
```

### Woche 2: Rekursion und Performance in Julia
**Lernziele:**
- Rekursion vs. Iteration mit Julia-Performance
- Type stability für Optimierung
- Debugging mit VS Code Julia-Extension
- Memoization in Julia

**Julia-spezifische Themen:**
- `@memoize` macro oder Dict-basierte Memoization
- Type annotations für Performance: `::Int64`
- `@code_warntype` für Type stability
- `@profile` für Performance-Analyse

**Praktische Übungen:**
```julia
using Memoization

# Naive Rekursion - langsam
function fib_naive(n::Int)::Int
    if n ≤ 2
        return 1
    end
    return fib_naive(n-1) + fib_naive(n-2)
end

# Memoized Version - schnell
@memoize function fib_memo(n::Int)::Int
    if n ≤ 2
        return 1
    end
    return fib_memo(n-1) + fib_memo(n-2)
end

# Iterative Version - speichersparend
function fib_iterative(n::Int)::Int
    if n ≤ 2
        return 1
    end
    a, b = 1, 1
    for i in 3:n
        a, b = b, a + b
    end
    return b
end

# Performance-Vergleich visualisieren
function compare_fibonacci_methods()
    ns = 1:35
    times_naive = [@elapsed fib_naive(n) for n in ns[1:25]]  # Nur bis 25, sonst zu langsam
    times_memo = [@elapsed fib_memo(n) for n in ns]
    times_iter = [@elapsed fib_iterative(n) for n in ns]
    
    plot(ns[1:25], times_naive, label="Naive Recursion", yscale=:log10)
    plot!(ns, times_memo, label="Memoized")
    plot!(ns, times_iter, label="Iterative")
    xlabel!("n")
    ylabel!("Time (seconds)")
    title!("Fibonacci Performance Comparison")
end
```

## Phase 2: Datenstrukturen in Julia (4-5 Wochen)

### Woche 3: Julia Arrays und Custom Types
**Arrays und Vektoren:**
- `Vector{T}` vs. `Array{T,N}` verstehen
- Broadcasting mit `.` Operator
- Views vs. Copies: `@view arr[1:10]`
- Memory-effiziente Operationen

**Custom Types definieren:**
```julia
# Eigene LinkedList mit Julia Types
mutable struct ListNode{T}
    data::T
    next::Union{ListNode{T}, Nothing}
    
    ListNode{T}(data::T) where T = new{T}(data, nothing)
end

mutable struct LinkedList{T}
    head::Union{ListNode{T}, Nothing}
    size::Int
    
    LinkedList{T}() where T = new{T}(nothing, 0)
end

# Multiple dispatch für verschiedene Operationen
function Base.push!(list::LinkedList{T}, data::T) where T
    new_node = ListNode{T}(data)
    new_node.next = list.head
    list.head = new_node
    list.size += 1
    return list
end

function Base.length(list::LinkedList)
    return list.size
end

# Visualisierung der Liste
function visualize_list(list::LinkedList{T}) where T
    if list.head === nothing
        println("Empty list")
        return
    end
    
    current = list.head
    elements = T[]
    while current !== nothing
        push!(elements, current.data)
        current = current.next
    end
    
    # ASCII Darstellung
    println(join(elements, " -> "), " -> NULL")
end
```

**Praktische Übungen:**
- Eigene LinkedList implementieren mit Generics
- Array vs. LinkedList Performance-Vergleich
- Memory allocation profiling mit `@allocated`

### Woche 4: Stack und Queue in Julia
**Stack (LIFO) Implementation:**
```julia
mutable struct Stack{T}
    items::Vector{T}
    
    Stack{T}() where T = new{T}(T[])
end

function Base.push!(stack::Stack{T}, item::T) where T
    push!(stack.items, item)
end

function Base.pop!(stack::Stack{T}) where T
    if isempty(stack.items)
        error("Stack is empty")
    end
    return pop!(stack.items)
end

function Base.isempty(stack::Stack)
    return isempty(stack.items)
end

# Visualisierung des Stacks
function visualize_stack(stack::Stack{T}) where T
    if isempty(stack)
        println("Empty stack")
        return
    end
    
    println("Top")
    for i in length(stack.items):-1:1
        println("│ $(stack.items[i]) │")
    end
    println("└─────┘")
    println("Bottom")
end
```

**Queue (FIFO) mit Circular Buffer:**
```julia
mutable struct Queue{T}
    buffer::Vector{Union{T, Nothing}}
    head::Int
    tail::Int
    size::Int
    capacity::Int
    
    function Queue{T}(capacity::Int) where T
        buffer = Vector{Union{T, Nothing}}(nothing, capacity)
        new{T}(buffer, 1, 1, 0, capacity)
    end
end

function enqueue!(queue::Queue{T}, item::T) where T
    if queue.size == queue.capacity
        error("Queue is full")
    end
    
    queue.buffer[queue.tail] = item
    queue.tail = queue.tail % queue.capacity + 1
    queue.size += 1
end

function dequeue!(queue::Queue{T}) where T
    if queue.size == 0
        error("Queue is empty")
    end
    
    item = queue.buffer[queue.head]
    queue.buffer[queue.head] = nothing
    queue.head = queue.head % queue.capacity + 1
    queue.size -= 1
    return item
end
```

**Praktische Anwendungen:**
```julia
# Expression Evaluator mit Stack
function evaluate_postfix(expression::Vector{String})
    stack = Stack{Float64}()
    
    for token in expression
        if token in ["+", "-", "*", "/"]
            b = pop!(stack)
            a = pop!(stack)
            result = if token == "+"
                a + b
            elseif token == "-"
                a - b
            elseif token == "*"
                a * b
            else  # "/"
                a / b
            end
            push!(stack, result)
        else
            push!(stack, parse(Float64, token))
        end
    end
    
    return pop!(stack)
end

# BFS Vorbereitung mit Queue
function level_order_numbers(max_level::Int)
    queue = Queue{Tuple{Int, Int}}(100)  # (value, level)
    result = Vector{Vector{Int}}()
    
    enqueue!(queue, (1, 1))
    current_level = 1
    current_level_nums = Int[]
    
    while queue.size > 0
        value, level = dequeue!(queue)
        
        if level > current_level
            push!(result, copy(current_level_nums))
            current_level_nums = Int[]
            current_level = level
        end
        
        if level <= max_level
            push!(current_level_nums, value)
            if level < max_level
                enqueue!(queue, (value * 2, level + 1))
                enqueue!(queue, (value * 2 + 1, level + 1))
            end
        end
    end
    
    if !isempty(current_level_nums)
        push!(result, current_level_nums)
    end
    
    return result
end
```

### Woche 5: Hash Tables und Dictionaries in Julia
**Hash-Funktionen und Kollisionsbehandlung:**
```julia
using Plots, StatsBase

# Eigene Hash Table Implementation
mutable struct HashTable{K, V}
    buckets::Vector{Vector{Pair{K, V}}}
    size::Int
    capacity::Int
    
    function HashTable{K, V}(capacity::Int = 16) where {K, V}
        buckets = [Pair{K, V}[] for _ in 1:capacity]
        new{K, V}(buckets, 0, capacity)
    end
end

# Einfache Hash-Funktion
function simple_hash(key::String, capacity::Int)
    hash_value = 0
    for char in key
        hash_value = (hash_value * 31 + Int(char)) % capacity
    end
    return hash_value + 1  # 1-based indexing
end

function Base.setindex!(ht::HashTable{K, V}, value::V, key::K) where {K, V}
    index = simple_hash(string(key), ht.capacity)
    bucket = ht.buckets[index]
    
    # Update existing key
    for i in 1:length(bucket)
        if bucket[i].first == key
            bucket[i] = key => value
            return ht
        end
    end
    
    # Add new key-value pair
    push!(bucket, key => value)
    ht.size += 1
    
    # Rehash if load factor too high
    if ht.size > 0.75 * ht.capacity
        rehash!(ht)
    end
    
    return ht
end

function Base.getindex(ht::HashTable{K, V}, key::K) where {K, V}
    index = simple_hash(string(key), ht.capacity)
    bucket = ht.buckets[index]
    
    for pair in bucket
        if pair.first == key
            return pair.second
        end
    end
    
    throw(KeyError(key))
end

function rehash!(ht::HashTable{K, V}) where {K, V}
    old_buckets = ht.buckets
    ht.capacity *= 2
    ht.buckets = [Pair{K, V}[] for _ in 1:ht.capacity]
    ht.size = 0
    
    for bucket in old_buckets
        for pair in bucket
            ht[pair.first] = pair.second
        end
    end
end

# Hash-Verteilung visualisieren
function visualize_hash_distribution(ht::HashTable)
    bucket_sizes = [length(bucket) for bucket in ht.buckets]
    
    histogram(bucket_sizes, 
             title="Hash Table Bucket Distribution",
             xlabel="Items per Bucket", 
             ylabel="Number of Buckets",
             bins=0:maximum(bucket_sizes)+1)
end

# Performance-Vergleich: Custom vs. Built-in Dict
function compare_hash_performance()
    n_operations = 10000
    
    # Custom HashTable
    custom_ht = HashTable{String, Int}()
    time_custom = @elapsed begin
        for i in 1:n_operations
            custom_ht["key_$i"] = i
        end
        for i in 1:n_operations
            _ = custom_ht["key_$i"]
        end
    end
    
    # Built-in Dict
    builtin_dict = Dict{String, Int}()
    time_builtin = @elapsed begin
        for i in 1:n_operations
            builtin_dict["key_$i"] = i
        end
        for i in 1:n_operations
            _ = builtin_dict["key_$i"]
        end
    end
    
    println("Custom HashTable: $(time_custom)s")
    println("Built-in Dict: $(time_builtin)s")
    println("Speedup factor: $(time_custom / time_builtin)")
end
```

**Praktische Anwendungen:**
```julia
# Word frequency counter
function count_words(text::String)
    words = split(lowercase(text), r"[^a-zA-Z]+")
    word_count = Dict{String, Int}()
    
    for word in words
        if !isempty(word)
            word_count[word] = get(word_count, word, 0) + 1
        end
    end
    
    return word_count
end

# LRU Cache Implementation
mutable struct LRUCache{K, V}
    capacity::Int
    cache::Dict{K, V}
    order::Vector{K}
    
    LRUCache{K, V}(capacity::Int) where {K, V} = new{K, V}(capacity, Dict{K, V}(), K[])
end

function Base.get!(cache::LRUCache{K, V}, key::K, default::V) where {K, V}
    if haskey(cache.cache, key)
        # Move to end (most recent)
        filter!(x -> x != key, cache.order)
        push!(cache.order, key)
        return cache.cache[key]
    end
    
    # Add new item
    if length(cache.cache) >= cache.capacity
        # Remove least recently used
        lru_key = popfirst!(cache.order)
        delete!(cache.cache, lru_key)
    end
    
    cache.cache[key] = default
    push!(cache.order, key)
    return default
end
```

### Woche 6-7: Binary Trees und BST in Julia
**Binary Tree Struktur:**
```julia
using Plots, GraphRecipes

# Tree Node Definition
mutable struct TreeNode{T}
    data::T
    left::Union{TreeNode{T}, Nothing}
    right::Union{TreeNode{T}, Nothing}
    
    TreeNode{T}(data::T) where T = new{T}(data, nothing, nothing)
end

# Binary Search Tree
mutable struct BST{T}
    root::Union{TreeNode{T}, Nothing}
    size::Int
    
    BST{T}() where T = new{T}(nothing, 0)
end

# Insert with multiple dispatch
function Base.insert!(bst::BST{T}, data::T) where T
    if bst.root === nothing
        bst.root = TreeNode{T}(data)
        bst.size += 1
        return bst
    end
    
    insert_node!(bst.root, data)
    bst.size += 1
    return bst
end

function insert_node!(node::TreeNode{T}, data::T) where T
    if data < node.data
        if node.left === nothing
            node.left = TreeNode{T}(data)
        else
            insert_node!(node.left, data)
        end
    elseif data > node.data
        if node.right === nothing
            node.right = TreeNode{T}(data)
        else
            insert_node!(node.right, data)
        end
    end
    # Ignore duplicates
end

# Search operation
function Base.in(data::T, bst::BST{T}) where T
    return search_node(bst.root, data)
end

function search_node(node::Union{TreeNode{T}, Nothing}, data::T) where T
    if node === nothing
        return false
    elseif data == node.data
        return true
    elseif data < node.data
        return search_node(node.left, data)
    else
        return search_node(node.right, data)
    end
end

# Tree Traversals
function inorder_traversal(node::Union{TreeNode{T}, Nothing}) where T
    result = T[]
    inorder_helper!(node, result)
    return result
end

function inorder_helper!(node::Union{TreeNode{T}, Nothing}, result::Vector{T}) where T
    if node !== nothing
        inorder_helper!(node.left, result)
        push!(result, node.data)
        inorder_helper!(node.right, result)
    end
end

function preorder_traversal(node::Union{TreeNode{T}, Nothing}) where T
    result = T[]
    preorder_helper!(node, result)
    return result
end

function preorder_helper!(node::Union{TreeNode{T}, Nothing}, result::Vector{T}) where T
    if node !== nothing
        push!(result, node.data)
        preorder_helper!(node.left, result)
        preorder_helper!(node.right, result)
    end
end

# Tree Visualization
function visualize_tree(bst::BST{T}) where T
    if bst.root === nothing
        println("Empty tree")
        return
    end
    
    # Create adjacency list for plotting
    nodes, edges = tree_to_graph(bst.root)
    
    # Plot mit GraphRecipes
    graphplot(edges, 
             names=nodes,
             nodesize=0.3,
             nodecolor=:lightblue,
             nodeshape=:circle,
             title="Binary Search Tree")
end

function tree_to_graph(root::TreeNode{T}) where T
    nodes = T[]
    edges = Vector{Tuple{Int, Int}}()
    node_map = Dict{TreeNode{T}, Int}()
    
    function traverse(node, parent_idx=0)
        if node === nothing
            return
        end
        
        push!(nodes, node.data)
        current_idx = length(nodes)
        node_map[node] = current_idx
        
        if parent_idx > 0
            push!(edges, (parent_idx, current_idx))
        end
        
        traverse(node.left, current_idx)
        traverse(node.right, current_idx)
    end
    
    traverse(root)
    return nodes, edges
end

# Tree Height and Balance
function tree_height(node::Union{TreeNode{T}, Nothing}) where T
    if node === nothing
        return 0
    end
    return 1 + max(tree_height(node.left), tree_height(node.right))
end

function is_balanced(node::Union{TreeNode{T}, Nothing}) where T
    if node === nothing
        return true
    end
    
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    
    return abs(left_height - right_height) <= 1 && 
           is_balanced(node.left) && 
           is_balanced(node.right)
end

# Tree Statistics
function tree_stats(bst::BST{T}) where T
    if bst.root === nothing
        return (size=0, height=0, balanced=true)
    end
    
    height = tree_height(bst.root)
    balanced = is_balanced(bst.root)
    
    return (size=bst.size, height=height, balanced=balanced)
end
```

**Praktische Übungen:**
```julia
# BST Performance vs. Array
function compare_search_performance()
    sizes = [100, 500, 1000, 5000, 10000]
    bst_times = Float64[]
    array_times = Float64[]
    
    for n in sizes
        # Create data
        data = shuffle(1:n)
        
        # BST
        bst = BST{Int}()
        for x in data
            insert!(bst, x)
        end
        
        # Array
        arr = sort(data)
        
        # Measure search times
        search_keys = sample(data, min(100, n), replace=false)
        
        bst_time = @elapsed begin
            for key in search_keys
                key in bst
            end
        end
        
        array_time = @elapsed begin
            for key in search_keys
                searchsorted(arr, key) |> !isempty
            end
        end
        
        push!(bst_times, bst_time)
        push!(array_times, array_time)
    end
    
    plot(sizes, bst_times, label="BST Search", marker=:circle)
    plot!(sizes, array_times, label="Array Binary Search", marker=:square)
    xlabel!("Data Size")
    ylabel!("Search Time (seconds)")
    title!("BST vs Array Search Performance")
    yscale!(:log10)
end

# Tree balancing demonstration
function demonstrate_balance_importance()
    # Balanced tree
    balanced_data = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]
    balanced_bst = BST{Int}()
    for x in balanced_data
        insert!(balanced_bst, x)
    end
    
    # Unbalanced tree (sorted insertion)
    unbalanced_data = 1:11
    unbalanced_bst = BST{Int}()
    for x in unbalanced_data
        insert!(unbalanced_bst, x)
    end
    
    println("Balanced Tree Stats: ", tree_stats(balanced_bst))
    println("Unbalanced Tree Stats: ", tree_stats(unbalanced_bst))
    
    # Search performance comparison
    search_keys = 1:11
    
    balanced_time = @elapsed begin
        for key in search_keys
            key in balanced_bst
        end
    end
    
    unbalanced_time = @elapsed begin
        for key in search_keys
            key in unbalanced_bst
        end
    end
    
    println("Balanced search time: $balanced_time")
    println("Unbalanced search time: $unbalanced_time")
end
```

## Phase 3: Grundlegende Algorithmen (4-5 Wochen)

## Phase 3: Algorithmen in Julia (4-5 Wochen)

### Woche 8: Sortierungsalgorithmen mit Julia Performance
**Sortierungs-Suite mit Visualisierung:**
```julia
using BenchmarkTools, Plots, Random

# Abstract type für alle Sortieralgorithmen
abstract type SortingAlgorithm end

struct BubbleSort <: SortingAlgorithm end
struct SelectionSort <: SortingAlgorithm end
struct InsertionSort <: SortingAlgorithm end
struct MergeSort <: SortingAlgorithm end
struct QuickSort <: SortingAlgorithm end

# Multiple dispatch für verschiedene Algorithmen
function sort!(arr::Vector{T}, ::BubbleSort) where T
    n = length(arr)
    swaps = 0
    comparisons = 0
    
    for i in 1:n-1
        swapped = false
        for j in 1:n-i
            comparisons += 1
            if arr[j] > arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = true
            end
        end
        if !swapped
            break
        end
    end
    
    return (swaps=swaps, comparisons=comparisons)
end

function sort!(arr::Vector{T}, ::MergeSort) where T
    comparisons = Ref(0)
    merge_sort_recursive!(arr, 1, length(arr), comparisons)
    return (swaps=0, comparisons=comparisons[])  # Merge sort doesn't swap, it copies
end

function merge_sort_recursive!(arr::Vector{T}, left::Int, right::Int, comparisons::Ref{Int}) where T
    if left < right
        mid = (left + right) ÷ 2
        merge_sort_recursive!(arr, left, mid, comparisons)
        merge_sort_recursive!(arr, mid + 1, right, comparisons)
        merge!(arr, left, mid, right, comparisons)
    end
end

function merge!(arr::Vector{T}, left::Int, mid::Int, right::Int, comparisons::Ref{Int}) where T
    # Create temporary arrays
    left_arr = arr[left:mid]
    right_arr = arr[mid+1:right]
    
    i = j = 1
    k = left
    
    while i <= length(left_arr) && j <= length(right_arr)
        comparisons[] += 1
        if left_arr[i] <= right_arr[j]
            arr[k] = left_arr[i]
            i += 1
        else
            arr[k] = right_arr[j]
            j += 1
        end
        k += 1
    end
    
    # Copy remaining elements
    while i <= length(left_arr)
        arr[k] = left_arr[i]
        i += 1
        k += 1
    end
    
    while j <= length(right_arr)
        arr[k] = right_arr[j]
        j += 1
        k += 1
    end
end

function sort!(arr::Vector{T}, ::QuickSort) where T
    comparisons = Ref(0)
    swaps = Ref(0)
    quicksort_recursive!(arr, 1, length(arr), comparisons, swaps)
    return (swaps=swaps[], comparisons=comparisons[])
end

function quicksort_recursive!(arr::Vector{T}, low::Int, high::Int, 
                             comparisons::Ref{Int}, swaps::Ref{Int}) where T
    if low < high
        pivot_idx = partition!(arr, low, high, comparisons, swaps)
        quicksort_recursive!(arr, low, pivot_idx - 1, comparisons, swaps)
        quicksort_recursive!(arr, pivot_idx + 1, high, comparisons, swaps)
    end
end

function partition!(arr::Vector{T}, low::Int, high::Int, 
                   comparisons::Ref{Int}, swaps::Ref{Int}) where T
    pivot = arr[high]
    i = low - 1
    
    for j in low:high-1
        comparisons[] += 1
        if arr[j] <= pivot
            i += 1
            if i != j
                arr[i], arr[j] = arr[j], arr[i]
                swaps[] += 1
            end
        end
    end
    
    if i + 1 != high
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[] += 1
    end
    
    return i + 1
end

# Performance Benchmark Suite
function benchmark_sorting_algorithms()
    algorithms = [
        ("Bubble Sort", BubbleSort()),
        ("Selection Sort", SelectionSort()),
        ("Insertion Sort", InsertionSort()),
        ("Merge Sort", MergeSort()),
        ("Quick Sort", QuickSort()),
        ("Julia Built-in", :builtin)
    ]
    
    sizes = [100, 500, 1000, 2000, 5000]
    results = Dict()
    
    for (name, algo) in algorithms
        times = Float64[]
        
        for size in sizes
            # Generate random data
            data = rand(1:1000, size)
            
            if algo == :builtin
                time = @elapsed sort(data)
            else
                test_data = copy(data)
                time = @elapsed sort!(test_data, algo)
            end
            
            push!(times, time)
        end
        
        results[name] = times
    end
    
    # Plot results
    p = plot(title="Sorting Algorithm Performance", 
             xlabel="Input Size", 
             ylabel="Time (seconds)",
             yscale=:log10)
    
    for (name, times) in results
        plot!(p, sizes, times, label=name, marker=:circle)
    end
    
    return p
end

# Visualize sorting process (for small arrays)
mutable struct SortingVisualizer{T}
    steps::Vector{Vector{T}}
    comparisons::Int
    swaps::Int
    
    SortingVisualizer{T}() where T = new{T}(Vector{T}[], 0, 0)
end

function visualize_bubble_sort(arr::Vector{T}) where T
    visualizer = SortingVisualizer{T}()
    n = length(arr)
    arr_copy = copy(arr)
    
    push!(visualizer.steps, copy(arr_copy))
    
    for i in 1:n-1
        for j in 1:n-i
            visualizer.comparisons += 1
            if arr_copy[j] > arr_copy[j+1]
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                visualizer.swaps += 1
                push!(visualizer.steps, copy(arr_copy))
            end
        end
    end
    
    return visualizer
end

function animate_sorting(visualizer::SortingVisualizer{T}) where T
    n_steps = length(visualizer.steps)
    
    anim = @animate for i in 1:n_steps
        bar(visualizer.steps[i], 
            title="Bubble Sort - Step $i/$n_steps",
            xlabel="Position",
            ylabel="Value",
            legend=false,
            color=:lightblue)
    end
    
    return anim
end

# Complexity analysis with actual measurements
function analyze_complexity()
    println("=== Sorting Algorithm Complexity Analysis ===")
    
    # Test different input types
    input_types = [
        ("Random", n -> rand(1:1000, n)),
        ("Sorted", n -> collect(1:n)),
        ("Reverse Sorted", n -> collect(n:-1:1)),
        ("Nearly Sorted", n -> begin
            arr = collect(1:n)
            # Swap a few random elements
            for _ in 1:max(1, n÷20)
                i, j = rand(1:n, 2)
                arr[i], arr[j] = arr[j], arr[i]
            end
            arr
        end)
    ]
    
    algorithms = [MergeSort(), QuickSort()]
    size = 1000
    
    for (input_name, generator) in input_types
        println("\n$input_name Input:")
        data = generator(size)
        
        for algo in algorithms
            test_data = copy(data)
            result = @timed sort!(test_data, algo)
            
            algo_name = typeof(algo) |> string
            println("  $algo_name: $(result.time)s, $(result.bytes) bytes allocated")
        end
    end
end
```

### Woche 9: Suchalgorithmen in Julia
**Binary Search mit Multiple Dispatch:**
```julia
# Generic binary search
function binary_search(arr::Vector{T}, target::T) where T
    left, right = 1, length(arr)  # 1-based indexing!
    
    while left <= right
        mid = (left + right) ÷ 2
        
        if arr[mid] == target
            return mid
        elseif arr[mid] < target
            left = mid + 1
        else
            right = mid - 1
        end
    end
    
    return nothing
end

# Find first/last occurrence
function find_first(arr::Vector{T}, target::T) where T
    result = -1
    left, right = 1, length(arr)
    
    while left <= right
        mid = (left + right) ÷ 2
        
        if arr[mid] == target
            result = mid
            right = mid - 1  # Continue searching left
        elseif arr[mid] < target
            left = mid + 1
        else
            right = mid - 1
        end
    end
    
    return result > 0 ? result : nothing
end

# Search in rotated array
function search_rotated(arr::Vector{T}, target::T) where T
    left, right = 1, length(arr)
    
    while left <= right
        mid = (left + right) ÷ 2
        
        if arr[mid] == target
            return mid
        end
        
        # Left half is sorted
        if arr[left] <= arr[mid]
            if arr[left] <= target < arr[mid]
                right = mid - 1
            else
                left = mid + 1
            end
        # Right half is sorted
        else
            if arr[mid] < target <= arr[right]
                left = mid + 1
            else
                right = mid - 1
            end
        end
    end
    
    return nothing
end
```

**String-Suche Algorithmen:**
```julia
# Naive String Matching
function naive_string_search(text::String, pattern::String)
    matches = Int[]
    n, m = length(text), length(pattern)
    
    for i in 1:n-m+1
        if text[i:i+m-1] == pattern
            push!(matches, i)
        end
    end
    
    return matches
end

# KMP Algorithm (vereinfacht)
function compute_lps(pattern::String)
    m = length(pattern)
    lps = zeros(Int, m)
    len = 0
    i = 2
    
    while i <= m
        if pattern[i] == pattern[len+1]
            len += 1
            lps[i] = len
            i += 1
        else
            if len != 0
                len = lps[len]
            else
                lps[i] = 0
                i += 1
            end
        end
    end
    
    return lps
end

function kmp_search(text::String, pattern::String)
    n, m = length(text), length(pattern)
    lps = compute_lps(pattern)
    matches = Int[]
    
    i = j = 1
    while i <= n
        if pattern[j] == text[i]
            i += 1
            j += 1
        end
        
        if j > m
            push!(matches, i - j + 1)
            j = lps[j-1] + 1
        elseif i <= n && pattern[j] != text[i]
            if j != 1
                j = lps[j-1] + 1
            else
                i += 1
            end
        end
    end
    
    return matches
end
```

### Woche 10-11: Graph-Algorithmen in Julia
**Graph-Datenstruktur:**
```julia
using DataStructures

# Adjacency List Graph
mutable struct Graph{T}
    vertices::Set{T}
    adj_list::Dict{T, Vector{T}}
    
    Graph{T}() where T = new{T}(Set{T}(), Dict{T, Vector{T}}())
end

function add_vertex!(g::Graph{T}, v::T) where T
    push!(g.vertices, v)
    if !haskey(g.adj_list, v)
        g.adj_list[v] = T[]
    end
end

function add_edge!(g::Graph{T}, u::T, v::T, directed::Bool=false) where T
    add_vertex!(g, u)
    add_vertex!(g, v)
    
    push!(g.adj_list[u], v)
    if !directed
        push!(g.adj_list[v], u)
    end
end

# DFS Implementation
function dfs(g::Graph{T}, start::T) where T
    visited = Set{T}()
    result = T[]
    
    function dfs_recursive(vertex::T)
        if vertex in visited
            return
        end
        
        push!(visited, vertex)
        push!(result, vertex)
        
        for neighbor in g.adj_list[vertex]
            dfs_recursive(neighbor)
        end
    end
    
    dfs_recursive(start)
    return result
end

# BFS Implementation
function bfs(g::Graph{T}, start::T) where T
    visited = Set{T}([start])
    queue = Queue{T}()
    result = T[]
    
    enqueue!(queue, start)
    
    while !isempty(queue)
        vertex = dequeue!(queue)
        push!(result, vertex)
        
        for neighbor in g.adj_list[vertex]
            if neighbor ∉ visited
                push!(visited, neighbor)
                enqueue!(queue, neighbor)
            end
        end
    end
    
    return result
end

# Shortest Path (BFS for unweighted)
function shortest_path(g::Graph{T}, start::T, target::T) where T
    if start == target
        return [start]
    end
    
    visited = Set{T}([start])
    queue = Queue{Tuple{T, Vector{T}}}()
    enqueue!(queue, (start, [start]))
    
    while !isempty(queue)
        vertex, path = dequeue!(queue)
        
        for neighbor in g.adj_list[vertex]
            if neighbor == target
                return vcat(path, [neighbor])
            end
            
            if neighbor ∉ visited
                push!(visited, neighbor)
                enqueue!(queue, (neighbor, vcat(path, [neighbor])))
            end
        end
    end
    
    return T[]  # No path found
end
```

### Woche 12: Dynamic Programming in Julia
**Memoization Patterns:**
```julia
# Coin Change Problem
function coin_change(coins::Vector{Int}, amount::Int)
    dp = fill(-1, amount + 1)
    dp[1] = 0  # 1-based: dp[1] represents amount 0
    
    for i in 2:amount+1  # 1-based indexing
        current_amount = i - 1
        for coin in coins
            if coin <= current_amount && dp[current_amount - coin + 1] != -1
                if dp[i] == -1
                    dp[i] = dp[current_amount - coin + 1] + 1
                else
                    dp[i] = min(dp[i], dp[current_amount - coin + 1] + 1)
                end
            end
        end
    end
    
    return dp[amount + 1] == -1 ? -1 : dp[amount + 1]
end

# Longest Common Subsequence
function lcs_length(s1::String, s2::String)
    m, n = length(s1), length(s2)
    dp = zeros(Int, m + 1, n + 1)
    
    for i in 2:m+1
        for j in 2:n+1
            if s1[i-1] == s2[j-1]
                dp[i, j] = dp[i-1, j-1] + 1
            else
                dp[i, j] = max(dp[i-1, j], dp[i, j-1])
            end
        end
    end
    
    return dp[m+1, n+1]
end

# 0/1 Knapsack Problem
function knapsack_01(weights::Vector{Int}, values::Vector{Int}, capacity::Int)
    n = length(weights)
    dp = zeros(Int, n + 1, capacity + 1)
    
    for i in 2:n+1
        for w in 1:capacity+1
            item_weight = weights[i-1]
            item_value = values[i-1]
            
            if item_weight <= w - 1  # w-1 because of 1-based indexing
                dp[i, w] = max(dp[i-1, w], 
                              dp[i-1, w - item_weight] + item_value)
            else
                dp[i, w] = dp[i-1, w]
            end
        end
    end
    
    return dp[n+1, capacity+1]
end
```

## Julia-spezifische Entwicklungsumgebung

### VS Code Setup Optimierung:
```julia
# .vscode/settings.json für das Projekt
{
    "julia.enableTelemetry": false,
    "julia.execution.resultDisplay.enabled": true,
    "julia.format.indent": 4,
    "julia.lint.run": true,
    "julia.packageServer": "",
    "files.associations": {
        "*.jl": "julia"
    }
}
```

### Projekt-Initialisierung:
```bash
# Neues Julia-Projekt erstellen
mkdir AlgoLearningJulia
cd AlgoLearningJulia

# Julia Package-Umgebung initialisieren
julia --project=. -e 'using Pkg; Pkg.activate(".")'
```

### Projektstruktur:
```
AlgoLearningJulia/
├── Project.toml                 # Package dependencies
├── Manifest.toml               # Exact package versions
├── src/
│   ├── AlgoLearning.jl        # Main module
│   ├── DataStructures/
│   │   ├── LinkedList.jl
│   │   ├── Stack.jl
│   │   ├── Queue.jl
│   │   ├── HashTable.jl
│   │   └── Trees.jl
│   ├── Algorithms/
│   │   ├── Sorting.jl
│   │   ├── Searching.jl
│   │   ├── GraphAlgorithms.jl
│   │   └── DynamicProgramming.jl
│   └── Visualization/
│       ├── Plotting.jl
│       └── Animation.jl
├── test/
│   ├── runtests.jl
│   ├── test_datastructures.jl
│   ├── test_algorithms.jl
│   └── benchmarks.jl
├── notebooks/                   # Pluto.jl notebooks
│   ├── Week01_Complexity.jl
│   ├── Week02_Recursion.jl
│   └── ...
└── examples/
    ├── sorting_demo.jl
    ├── graph_analysis.jl
    └── performance_comparison.jl
```

## Phase 4: Fortgeschrittene Datenstrukturen (3-4 Wochen)

### Woche 13: Heaps und Priority Queues
**Binary Heaps:**
- Min-Heap und Max-Heap
- Heap Operations (Insert, Extract, Heapify)
- Heap Sort Implementation
- Heap als Priority Queue

**Praktische Übungen:**
- Heap von Grund auf implementieren
- Top K Elements Probleme
- Median Finding

### Woche 14: Balancierte Bäume
**AVL Trees:**
- Rotation Operationen
- Balance Factor
- Automatic Balancing

**Red-Black Trees (Überblick):**
- Eigenschaften und Invarianten
- Vergleich mit AVL Trees

**Praktische Übungen:**
- AVL Tree Implementierung
- Performance-Vergleiche mit normalen BST

### Woche 15-16: Fortgeschrittene Graph-Strukturen
**Shortest Path Algorithmen:**
- Dijkstra's Algorithm
- Bellman-Ford Algorithm
- Floyd-Warshall (All Pairs)

**Minimum Spanning Tree:**
- Kruskal's Algorithm
- Prim's Algorithm
- Union-Find Datenstruktur

**Praktische Übungen:**
- Navigation System simulieren
- Network Design Probleme
- Union-Find Optimierungen

## Phase 5: Fortgeschrittene Algorithmen (3-4 Wochen)

### Woche 17: Erweiterte Dynamische Programmierung
**Fortgeschrittene DP-Patterns:**
- Matrix Chain Multiplication
- Edit Distance
- Palindrome Partitioning
- DP on Trees

**Praktische Übungen:**
- Komplexe DP-Probleme lösen
- State Space Design
- Bottom-up vs. Top-down Ansätze

### Woche 18: Greedy Algorithmen
**Greedy-Strategie:**
- Activity Selection Problem
- Huffman Coding
- Job Scheduling
- Greedy vs. DP Entscheidungen

**Praktische Übungen:**
- Greedy-Algorithmen implementieren
- Korrektheitsbeweis führen
- Gegenbeispiele für falsche Greedy-Ansätze

### Woche 19: Backtracking
**Backtracking-Template:**
- N-Queens Problem
- Sudoku Solver
- Subset Generation
- Permutations und Combinations

**Praktische Übungen:**
- Verschiedene Backtracking-Probleme
- Pruning-Strategien
- Iterative vs. Rekursive Implementierung

### Woche 20: String-Algorithmen
**Erweiterte String-Verarbeitung:**
- KMP-Algorithmus (detailliert)
- Rabin-Karp Algorithm
- Trie-Datenstruktur
- Suffix Arrays (Einführung)

**Praktische Übungen:**
- Text-Editor Funktionen
- Auto-Complete System
- Pattern Matching Optimierungen

## Phase 6: Spezielle Themen (2-3 Wochen)

### Woche 21: Bit-Manipulation
**Bit-Operationen:**
- Bitwise Operators
- Bit Masks
- Counting Set Bits
- Power of 2 Checks

**Praktische Übungen:**
- Bit-basierte Algorithmen
- Space-effiziente Lösungen
- Bit-Manipulation Tricks

### Woche 22: Geometrische Algorithmen (Optional)
**Computational Geometry:**
- Convex Hull
- Line Intersection
- Closest Pair of Points
- Point in Polygon

### Woche 23: Revision und Interview-Vorbereitung
**Zusammenfassung:**
- Häufige Interview-Patterns
- Code-Optimization Techniken
- Trade-off Analysen
- System Design Grundlagen

## Bewertung und Meilensteine - Julia Edition

### Wöchentliche Assessments:
- **Theoretische Fragen:** Big-O Analyse mit `@benchmark` Verifikation
- **Praktische Aufgaben:** Julia-Implementation mit Type stability
- **Performance Analysis:** `@time`, `@allocated`, `@profile` verwenden
- **Code Review:** Multiple dispatch und Type-Annotationen optimieren

### Monatliche Julia-Projekte:
- **Monat 1:** Eigene DataStructures.jl Library mit Visualisierung
- **Monat 2:** Sorting & Searching Suite mit Performance Benchmarks
- **Monat 3:** Graph-Algorithmus Package mit Plots.jl Integration
- **Monat 4:** Dynamic Programming Solver mit interaktiven Notebooks
- **Monat 5:** Comprehensive Algorithm Analysis Dashboard

### Julia-spezifische Bewertungskriterien:
- **Type Stability:** Code sollte type-stable sein (`@code_warntype`)
- **Performance:** Vergleich mit Julia Base-Implementierungen
- **Multiple Dispatch:** Elegante Nutzung von Julia's Dispatch-System
- **Memory Efficiency:** Minimale Allokationen bei Performance-kritischem Code
- **Documentation:** Docstrings für alle öffentlichen Funktionen

## Julia-Ressourcen und Tools

### Empfohlene Bücher:
- "Think Julia" (Ben Lauwens) - Einsteiger-freundlich
- "Julia High Performance" (Avik Sengupta) - Performance-Optimierung
- "Hands-On Design Patterns and Best Practices with Julia" - Fortgeschritten

### Online-Ressourcen:
- **Julia Documentation:** docs.julialang.org
- **Julia Academy:** juliaacademy.com (kostenlose Kurse)
- **JuliaHub:** juliahub.com (Package-Suche)
- **Discourse Forum:** discourse.julialang.org
- **GitHub Julia:** github.com/JuliaLang/julia

### Julia-spezifische Übungsplattformen:
- **Exercism Julia Track:** exercism.org/tracks/julia
- **Project Euler in Julia:** Mathematische Probleme
- **JuliaBox:** juliabox.com (Online-Umgebung)
- **Pluto.jl Notebooks:** GitHub Beispiele

### Performance und Debugging Tools:
```julia
# Wichtige Packages für Entwicklung
using Pkg
Pkg.add([
    "BenchmarkTools",    # @benchmark, @belapsed
    "Profile",           # @profile
    "ProfileView",       # GUI für Profile-Daten
    "Traceur",          # Performance-Hints
    "Debugger",         # Interaktiver Debugger
    "Revise",           # Code Hot-Reloading
    "Test",             # Unit Testing
    "Documenter"        # Documentation
])
```

## Praktischer Startleitfaden

### Tag 1: Setup und erste Schritte
1. **Julia installieren:** Von julialang.org/downloads
2. **VS Code Setup:** Julia Extension installieren
3. **Erstes Projekt:** Projektordner und Package-Umgebung erstellen
4. **Hello World:** Erste Julia-Datei mit REPL-Integration testen

### Woche 1 Aufgaben:
```julia
# 1. Komplexitäts-Messungen
function time_algorithm(f, inputs)
    times = []
    for input in inputs
        t = @elapsed f(input)
        push!(times, t)
    end
    return times
end

# 2. Erste Visualisierung
using Plots
sizes = [10, 50, 100, 500, 1000]
times = time_algorithm(sort, [rand(n) for n in sizes])
plot(sizes, times, marker=:circle, title="Sorting Performance")

# 3. Type-System verstehen
function typed_function(x::Int)::Float64
    return sqrt(x)
end

# @code_warntype typed_function(4) # Prüfen auf Type-Stability
```

### Lern-Workflow mit VS Code:
1. **Code schreiben** in .jl Dateien
2. **REPL nutzen** für interaktive Tests (`Ctrl+Shift+P` → "Julia: Start REPL")
3. **Code ausführen** mit `Ctrl+Enter` (Zeile) oder `Shift+Enter` (Block)
4. **Plots anzeigen** im integrierten Plot-Panel
5. **Debuggen** mit eingebautem Julia-Debugger
6. **Performance messen** mit `@time` und `@benchmark`

### Typische Entwicklungssession:
```julia
# 1. Package-Umgebung aktivieren
# ] activate .

# 2. Packages laden
using BenchmarkTools, Plots

# 3. Code entwickeln und testen
function my_algorithm(data)
    # Implementation hier
end

# 4. Performance testen
@benchmark my_algorithm(test_data)

# 5. Visualisieren
result = my_algorithm(test_data)
plot(result)

# 6. Tests schreiben
using Test
@test my_algorithm([1,2,3]) == expected_result
```

## Erfolgsmetriken - Julia Edition

### Wöchentlich:
- **5+ Probleme** verschiedener Schwierigkeitsgrade implementieren
- **Performance-Vergleich** mit Julia Base-Funktionen durchführen
- **Type-stable Code** schreiben (`@code_warntype` grün)
- **Visualisierung** für jeden neuen Algorithmus erstellen

### Monatlich:
- **Projekt-Package** mit Tests und Dokumentation
- **Performance-Optimierung:** 2x+ Speedup gegenüber naiver Implementation
- **Multiple Dispatch:** Elegante generische Funktionen
- **Interaktive Notebooks:** Pluto.jl für Algorithmus-Exploration

### Endziel (nach 6 Monaten):
- **Julia-Expertise:** Idiomatischer, performanter Julia-Code
- **Algorithmus-Bibliothek:** Wiederverwendbare, gut getestete Implementierungen
- **Performance-Bewusstsein:** Verstehen von Memory-Allokation und Optimierung
- **Visualization-Skills:** Algorithmen anschaulich erklären können
- **Package-Entwicklung:** Eigenes Julia-Package auf GitHub veröffentlichen

### Bonus-Ziele:
- **Contribution:** Pull Request zu einem Julia-Package
- **Blog/Tutorial:** Algorithmus-Artikel mit Julia-Beispielen
- **JuliaCon Talk:** Präsentation über entwickeltes Package
- **Mentoring:** Anderen beim Julia-Lernen helfen

## Nächste Schritte

1. **Sofort starten:**
   - Julia installieren und VS Code einrichten
   - Erstes "Hello World" mit REPL ausprobieren
   - BenchmarkTools installieren und ersten Performance-Test machen

2. **Diese Woche:**
   - Phase 1 des Lehrplans beginnen
   - Erstes Git-Repository für das Projekt anlegen
   - Mit Big-O Analyse und praktischen Messungen starten

3. **Nächsten Monat:**
   - Grundlegende Datenstrukturen in Julia implementieren
   - Performance-Vergleiche mit eingebauten Strukturen
   - Erste Visualisierungen mit Plots.jl erstellen

**Viel Erfolg beim Algorithmus-Lernen mit Julia! 🚀**