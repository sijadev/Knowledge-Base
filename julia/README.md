# Algorithm Learning with Julia

A comprehensive collection of algorithm implementations and learning materials using the Julia programming language.

## Overview

This repository contains implementations of various algorithms and data structures, along with lecture notes for learning computational concepts in Julia.

## Structure

```
algoLearning/
├── lectures/           # Lecture notes and documentation
│   └── Introduction.md # Introduction to Julia setup and basics
├── src/               # Source code
│   └── lectures/      # Lecture implementations
│       └── lecture_1.jl
└── README.md          # This file
```

## Getting Started

### Prerequisites

1. Install Julia from [https://julialang.org/downloads/](https://julialang.org/downloads/)
2. Install VS Code with Julia extension

### Setup

1. Clone this repository:
```bash
git clone https://github.com/[your-username]/algoLearning.git
cd algoLearning
```

2. Open Julia REPL and install required packages (press `]` for package mode):
```julia
add BenchmarkTools     # Performance measurement
add Plots             # Visualization
add PlotlyJS          # Interactive plots
add StatsBase         # Statistical functions
add DataStructures    # Advanced data structures
add GraphPlot         # Graph visualization
add Colors            # Color palettes for plots
add Random            # Random numbers
add Profile           # Code profiling
add Revise            # Hot-reloading for development
```

## Usage

### Running Code

In VS Code:
- Press `Shift + Command + P` and select "Julia: Start REPL"
- Execute code blocks with `Shift + Enter`

### Julia REPL Modes

- `]` → Package mode (pkg>)
- `?` → Help mode (help?>)
- `;` → Shell mode (shell>)
- `Backspace` → Back to Julia mode (julia>)

## Documentation

- Julia Documentation: [https://docs.julialang.org/en/v1/](https://docs.julialang.org/en/v1/)
- See `/lectures` folder for detailed notes and tutorials

## License

This project is for educational purposes.

## Author

Simon Janke