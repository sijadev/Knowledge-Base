# This file sets up the environment for the Julia curriculum project.

using Pkg

# Activate the project environment
Pkg.activate("..")

# Add necessary packages
Pkg.add("DataFrames")
Pkg.add("CSV")
Pkg.add("Plots")
Pkg.add("Jupyter")
Pkg.add("Markdown")

# Precompile the packages
Pkg.precompile()