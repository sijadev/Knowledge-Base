module algoLearning

# Re-export wichtige Funktionen
using Random
using BenchmarkTools
using Plots
using DataStructures
using StatsBase
using Test

# Submodule
include("dataStructures/LinkedList.jl")
# include("DataStructures/Stack.jl")
# include("DataStructures/Queue.jl")
# include("DataStructures/HashTable.jl")

# include("Algorithms/Sorting.jl")
# include("Algorithms/Searching.jl")

include("utils/Complexity.jl")
# include("utils/Visualization.jl")

# Exports
export
    # Data Structures
    LinkedList, # push!, pop!, length,
    # Stack, Queue,
    # HashTable,

    # Algorithms
    # bubble_sort!, merge_sort!, quick_sort!,
    # binary_search, linear_search,

    # Utils
    measure_complexity, plot_complexity
    # visualize_algorithm

end # module