#!/bin/bash

# Render Jupyter notebooks to HTML format
jupyter nbconvert --to html notebooks/*.ipynb

# Optionally, render notebooks in the examples directory
jupyter nbconvert --to html notebooks/examples/*.ipynb

# Notify user of completion
echo "Notebooks have been rendered to HTML format."