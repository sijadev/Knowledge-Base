# 1.0 Introduction

## 1.1 Pkg - Package

1. Julia installieren https://julialang.org/downloads/
Julia Dokumentation: https://docs.julialang.org/en/v1/
<br>
2. In VS Code: Shift + Command + P : julia: start repl 
<br>
3. Modis in Julia:
   - __]__ → Package Modus (pkg>)
   - __?__ → Help Modus (help?>)
   - __;__ → Shell Modus (shell>)
   - __Backspace__ → Zurück zum Julia Modus (julia>)
<br>
  
1. Short Cuts:
- ___opt + j + d___ (Hover over Command) --> Documentations 


1. In Julia REPL (Pkg-Modus mit ']'):

```julia
add BenchmarkTools     # Performance-Messung
add Plots             # Visualisierung
add PlotlyJS          # Interaktive Plots
add StatsBase         # Statistische Funktionen
add DataStructures    # Erweiterte Datenstrukturen
add GraphPlot         # Graph-Visualisierung
add Colors            # Farbpaletten für Plots
add Random            # Zufallszahlen
add Profile           # Code-Profiling
add Revise            # Hot-Reloading für Entwicklung
```
<br>
6. Codeblock:
  
```julia
#%% 
println("Hello")
println("there!")
#%% 
```
<br>
7. Variablen
   
```julia
my_name = "simon"
my_favourite_number = 23
print(my_name)
```
<br>
8. Stylistic Conventions
<br>
While Julia imposes few restrictions on valid names, it has become useful to adopt the following conventions:

- Names of variables are in lower case.
- Word separation can be indicated by underscores ('_'), but use of underscores is discouraged unless the name would be hard to read otherwise.
- Names of Types and Modules begin with a capital letter and word separation is shown with upper camel case instead of underscores.
- Names of functions and macros are in lower case, without underscores.
- Functions that write to their arguments have names that end in !. These are sometimes called "mutating" or "in-place" functions because they are intended to produce changes in their arguments after the function is called, not just return a value.



