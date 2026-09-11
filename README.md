# A01 — California Housing Boxplot

A small project that loads the California Housing dataset and produces a boxplot of median house value, as part of OPIM 5512 Assignment 01.

## Data

This project uses the **California Housing dataset**, loaded directly via `sklearn.datasets.fetch_california_housing`. No manual download is needed — the script fetches it automatically on first run.

## How to run

1. Clone this repo and open a terminal in the project root:
```
   git clone https://github.com/OPIM5512-qyj25002/A01.git
   cd A01
```
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Run the script from the repo root:

   **Mac/Linux:**
```
   python3 src/boxplot.py
```

   **Windows:**
```
   python src/boxplot.py
```

## Expected output

The script saves a boxplot image to:

```
figs/boxplot.png
```

The plot shows the distribution of median house value across the dataset, including the median, interquartile range, and outliers.

## How I built this

- Created a new repository named `A01` on GitHub.
- Cloned it locally using GitHub Desktop.
- Created a `dev` branch to keep my changes separate from `main`.
- Opened the project in VS Code and built a `src/boxplot.py` script using the California Housing dataset.
- Wrote code to generate three separate boxplots — median income, house age, and median house value.
- Created a `requirements.txt` file listing the libraries needed to run the script (pandas, matplotlib, scikit-learn).
- Ran the script from the terminal using `python3` since I'm on a Mac, which generated three boxplot images inside a `figs/` folder.
- Staged and committed the changes, then pushed the `dev` branch to GitHub.
- Opened a pull request comparing `dev` into `main`.
- Merged the PR once everything looked good.