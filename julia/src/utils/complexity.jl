using BenchmarkTools, Plots

"""
    measure_complexity(func, input_generator, sizes)

Misst die Zeitkomplexität einer Funktion für verschiedene Eingabegrößen.
"""
function measure_complexity(func, input_generator, sizes)
    times = Float64[]
    
    for n in sizes
        input_data = input_generator(n)
        
        # Mehrere Messungen für Genauigkeit
        time = @belapsed $func($input_data)
        push!(times, time)
        
        # Progress feedback
        println("Size $n: $(time)s")
    end
    
    return times
end

"""
    plot_complexity(sizes, times, algorithm_name; theoretical=nothing)

Plottet gemessene vs. theoretische Komplexität.
"""
function plot_complexity(sizes, times, algorithm_name; theoretical=nothing)
    p = plot(sizes, times, 
            marker=:circle, 
            label="Measured", 
            xlabel="Input Size", 
            ylabel="Time (seconds)",
            title="$algorithm_name Complexity")
    
    if theoretical !== nothing
        theoretical_times = [theoretical(n) for n in sizes]
        # Normalisierung auf gemessene Zeiten
        scale_factor = times[end] / theoretical_times[end]
        theoretical_times .*= scale_factor
        
        plot!(p, sizes, theoretical_times, 
              label="Theoretical", 
              linestyle=:dash)
    end
    
    return p
end

# Theoretische Komplexitätsfunktionen
O_1(n) = 1
O_log_n(n) = log2(n)
O_n(n) = n
O_n_log_n(n) = n * log2(n)
O_n2(n) = n^2
O_2n(n) = 2.0^n