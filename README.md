# Global Climate Change Analysis

[![Live Site](https://img.shields.io/badge/Live%20Site-GitHub%20Pages-blue?logo=github)](https://sriramchow.github.io/Global-Climate-Change-Analysis/)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20Presentation-red?logo=youtube)](https://youtu.be/kJt0P61GdxQ)
[![View Notebook](https://img.shields.io/badge/Notebook-nbviewer-orange?logo=jupyter)](https://nbviewer.org/github/sriramchow/Global-Climate-Change-Analysis/blob/main/Final_Project_SDV/Project_Notebook.ipynb)

A data analysis project exploring global land temperature trends (2000–2015) using Python and Tableau. Covers data cleaning, feature engineering, static and interactive visualizations, and regional climate comparisons.

🌐 **Live Site:** [https://sriramchow.github.io/Global-Climate-Change-Analysis/](https://sriramchow.github.io/Global-Climate-Change-Analysis/)

---

## Video Presentation

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20Presentation-red?logo=youtube)](https://youtu.be/kJt0P61GdxQ)

---

## Project Structure

```
Final_Project_SDV/
├── Project_Notebook.ipynb          # Main analysis notebook
├── Report_SDV.pdf                  # Full project report
├── Final_ppt.pptx                  # Presentation slides
├── methodology.drawio              # Methodology diagram
├── visualisations.twbx             # Tableau workbook
├── data/
│   ├── GlobalTemperatures.csv
│   ├── GlobalLandTemperaturesByCountry.csv
│   ├── GlobalLandTemperaturesByState.csv
│   ├── GlobalLandTemperaturesByMajorCity.csv
│   └── GlobalLandTemperaturesByCity.csv    ← download separately (509 MB)
└── Images/                         # Visualization screenshots

Global Land Temperature Change.docx # Additional documentation
Report_SDV.pdf                      # Summary report
```

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Tableau |
| Notebook | Jupyter Notebook |
| Design | Draw.io |

---

## Dataset

Data sourced from the **Berkeley Earth Surface Temperature Dataset** on Kaggle:

> [https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)

> **Note:** `GlobalLandTemperaturesByCity.csv` (~509 MB) is excluded from this repository due to GitHub's file size limit. Download it from the Kaggle link above and place it in `Final_Project_SDV/data/`.

---

## Key Visualizations

| Chart | Description |
|-------|-------------|
| Temperature Distribution | Box plots showing spread by country |
| Avg Temp Over Time (India) | Year-wise trend line for India |
| Temp vs Uncertainty | Scatter analysis of measurement confidence |
| World Map | Average temperature by country |
| Frequency Distribution | Global temp histogram |

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/sriramchow/Global-Climate-Change-Analysis.git
cd Global-Climate-Change-Analysis

# 2. Download the full dataset from Kaggle and place CSVs in:
#    Final_Project_SDV/data/

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# 4. Launch the notebook
jupyter notebook Final_Project_SDV/Project_Notebook.ipynb
```

---

## Author

**SriRam** — [GitHub](https://github.com/sriramchow)
