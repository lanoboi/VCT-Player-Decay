# Valorant Match Outcome Prediction

## Project Overview

This project uses machine learning to predict the outcome of professional Valorant Champions Tour matches. The goal is to predict whether Team A will win or lose a match based on historical team performance and match context features.

The project is framed as a binary classification task:

- `1` = Team A wins
- `0` = Team A loses

The project was completed for COMP 3608 and follows the B-rank project structure, using three yearly Kaggle data subsets and comparing multiple machine learning algorithms.

## Problem Statement

In professional Valorant, match outcomes are influenced by several factors such as team form, historical win rate, map performance, match stakes, and draft related variables. This project investigates whether these historical and contextual features can be used to predict match outcomes before the match is played.

The main research question is:

**Can historical team performance and match context features be used to predict Valorant Champions Tour match outcomes?**

## Dataset

The project uses data from the Kaggle Valorant Champions Tour dataset. The analysis focuses on three recent VCT seasons:

| Dataset | Season | Description |
|---|---:|---|
| D1 | 2023 | First yearly subset used for training and analysis |
| D2 | 2024 | Second yearly subset used for training and validation |
| D3 | 2025 | Most recent yearly subset used for final testing |

The data was cleaned, aggregated, and transformed into a master dataset for modelling.

## Features Used

The model uses pre-match features only, meaning the features are based on information available before the match takes place. This helps avoid data leakage.

Some of the main engineered features include:

- Historical win rate
- Historical average team rating
- Historical map win percentage
- Win rate difference between Team A and Team B
- Rating difference between Team A and Team B
- Map win percentage difference
- Match stakes
- Elimination match indicator
- Grand final indicator
- Draft related indicators

Differential features were especially important because match prediction depends heavily on the relative strength between both teams.

## Models Used

The project compares the following models:

1. Majority Class Baseline
2. Logistic Regression
3. Random Forest
4. XGBoost

The Majority Class Baseline was used as a simple reference point. The three main machine learning algorithms were compared to evaluate their strengths, weaknesses, and tradeoffs.

## Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix

ROC AUC was especially important because it shows how well the model separates likely winners from likely losers across different thresholds.

## Experimental Design

A chronological training and testing approach was used to make the experiment more realistic.

The main setup was:

- Train on 2023 and 2024 data
- Test on 2025 data

Walk-forward validation was also used:

| Fold | Training Data | Testing Data |
|---|---|---|
| Fold 1 | 2023 | 2024 |
| Fold 2 | 2023 and 2024 | 2025 |

This setup prevents the model from learning from future data and better reflects a real match prediction scenario.

## Key Findings

The results showed that historical team performance features can predict Valorant match outcomes better than random guessing.

Main findings:

- Logistic Regression achieved the strongest ROC AUC and was the most interpretable model.
- XGBoost achieved the strongest F1 score on the final test set.
- Random Forest captured nonlinear patterns but performed weaker than the other main models.
- Differential features such as historical win rate difference, rating difference, and map win percentage difference were among the most useful predictors.
- The Majority Class Baseline had a misleadingly high F1 score because it predicted the same class repeatedly, but its ROC AUC showed no real predictive ability.
