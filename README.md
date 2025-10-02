# Starbucks Location Analysis on Demographic and Health Data

## Overview
This project analyzes whether **Starbucks considers demographic and health factors when choosing store locations in Los Angeles**. We combined Starbucks location data with U.S. Census and CDC datasets to examine correlations between store density, socioeconomic characteristics, and community health outcomes at the ZIP-code level.

## Data Sources
- **Starbucks Locations**: Scraped and aggregated by ZIP code  
- **Demographics**: U.S. Census Bureau (income, education, population density)  
- **Health**: CDC PLACES dataset (obesity, diabetes, physical inactivity rates)  

## Methodology
1. Scraped Starbucks store locations and aggregated counts per ZIP code  
2. Collected and cleaned Census and CDC datasets  
3. Merged datasets into a unified analysis table  
4. Conducted correlation and regression analyses  
5. Visualized results using statistical plots and geographic mapping  

## Results
- **Strong correlation with demographics**  
  - Median household income: r ≈ 0.72  
  - Population density: r ≈ 0.65  
  - Education level: r ≈ 0.60  

- **Minimal correlation with health factors**  
  - Obesity rate: r ≈ –0.15  
  - Diabetes prevalence: r ≈ –0.10  
  - Physical inactivity: r ≈ –0.12  

- **Regression analysis**  
  - Demographics explained ~55% of variance in Starbucks density (R² ≈ 0.55)  
  - Health indicators explained <5%  

**Key Insight**: Starbucks expansion is influenced primarily by **socioeconomic potential** rather than community health outcomes.

## Visualizations
- Correlation heatmap of Starbucks density, demographics, and health indicators

<img src="starbucks%20correlation%20matrix.png" alt="Starbucks Correlation Matrix" width="800"/>

- Scatter plot: Starbucks density vs. median income  
- Choropleth map: Starbucks store density by ZIP code  

## Tools & Technologies
- **Python**: pandas, numpy, matplotlib, seaborn  
- **Jupyter Notebook** for data analysis  
- **GitHub** for version control  

## Repository Structure
```
├── data/
│ ├── raw/ # Original datasets
│ ├── interim/ # Cleaned datasets
│ └── final/ # Final merged dataset
├── analysis/
│ └── starbucks_analysis.ipynb # Main notebook for analysis
└── README.md
```


## Author
**HaYoung (Clara) Son**  
- Master’s in Applied Data Science, USC Viterbi School of Engineering  
- [Portfolio](https://www.notion.so/Welcome-to-Clara-s-Portfolio-27caee11431780948e93e8b2dd405509) | [GitHub](https://github.com/clarason14)
- [Live Streamlit App](https://starbuckslocationanalysisondemographicandhealthdata-7gbzvjhmuy.streamlit.app)
