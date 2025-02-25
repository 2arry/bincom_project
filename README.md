# Bincom Project

This repository contains various Python scripts for different tasks.

## Files

- `bincom_dev.py`: Extracts table content from `bincom.html` and creates a dictionary.
- `bincom.html`: HTML file containing the table data.
- `generate_random_binary.py`: Generates a random 4-digit binary number and converts it to base 10.
- `mean_color.py`: Analyzes the color data and calculates various statistics.
- `recursive_search.py`: Implements a recursive search algorithm.
- `sum_fibonacci.py`: Sums the first 50 Fibonacci numbers.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/2arry/bincom_project.git
   cd bincom_project
   ```

2. Install the required Python packages:
   ```sh
   pip install beautifulsoup4 psycopg2
   ```

## Running the Scripts

### `bincom_dev.py`
This script extracts table content from `bincom.html` and creates a dictionary.
```sh
python bincom_dev.py
```

### `generate_random_binary.py`
This script generates a random 4-digit binary number and converts it to base 10.
```sh
python generate_random_binary.py
```

### `mean_color.py`
This script analyzes the color data and calculates various statistics.
```sh
python mean_color.py
```

### `recursive_search.py`
This script implements a recursive search algorithm.
```sh
python recursive_search.py
```

### `sum_fibonacci.py`
This script sums the first 50 Fibonacci numbers.
```sh
python sum_fibonacci.py
```

## Version Control

### Add and commit the files
```sh
git add .
git commit -m "Initial commit with all project files"
```

### Push the changes to GitHub
```sh
git push origin main
```

## Final Directory Structure
```
bincom_project/
├── bincom_dev.py
├── bincom.html
├── generate_random_binary.py
├── mean_color.py
├── recursive_search.py
├── sum_fibonacci.py
├── README.md
```

