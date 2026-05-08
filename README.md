# Predicting Valorant Champions Tour Match Outcomes

## Project Overview
This project presents a comparative machine learning approach to predicting match outcomes in the **Valorant Champions Tour (VCT)**. It was developed as a B-Rank Mission for COMP 3608 - Machine Learning.

Done by: Delano Augustus, Kriston Latoo, Isaiah Hedley

The study uses three chronological slices of VCT professional match data (2023, 2024, and 2025) to train and evaluate models, simulating a real-world predictive environment where historical data is used to forecast future results.

## Repository Structure
- `vct_team_prediction.ipynb`: The main Jupyter notebook containing the full analysis, modeling, and evaluation.
- `aggregated/cleaned_master.csv`: The primary dataset used for training and testing (generated via preprocessing).
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Key Sections
1. **Problem Identification**: Formulating the match prediction as a binary classification problem.
2. **Datasets & Feature Engineering**: Temporal slicing (2023-2024 for training, 2025 for testing) and creation of 13 pre-match features.
3. **Exploratory Data Analysis (EDA)**: Examining class balance, feature correlations, and distributions.
4. **Algorithm Selection**: Using Logistic Regression, Random Forest, and XGBoost compared against a Majority Class Baseline.
5. **Implementation & Training**: Pipeline setup with scaling and hyperparameter tuning.
6. **Evaluation & Comparative Results**: Analyzing Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
7. **Sensitivity Analysis**: Testing model robustness to hyperparameter changes.
8. **Discussion & Conclusion**: Interpretability vs. Performance trade-offs.

## Model Results Summary
Based on the experimental results:
- **Best for Interpretability**: Logistic Regression (provides transparent feature weights).
- **Best for Raw Performance (F1)**: XGBoost.
- **Baseline**: Majority Class Baseline provides the performance floor.

## Installation & Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `vct_team_prediction.ipynb` in a Jupyter environment to run the analysis.
