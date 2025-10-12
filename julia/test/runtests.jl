using Test
using algoLearning

@testset "algoLearning Tests" begin
    
    @testset "LinkedList Tests" begin
        list = LinkedList{Int}()
        
        @test isempty(list)
        @test length(list) == 0
        
        push!(list, 1)
        push!(list, 2)
        push!(list, 3)
        
        @test length(list) == 3
        @test !isempty(list)
        
        @test pop!(list) == 3
        @test pop!(list) == 2
        @test length(list) == 1
    end
    
    @testset "Complexity Measurement" begin
        # Test mit einfacher Funktion
        linear_func(n) = sum(1:n)
        sizes = [100, 200, 400]
        times = measure_complexity(linear_func, identity, sizes)
        
        @test length(times) == length(sizes)
        @test all(t -> t > 0, times)
    end
end