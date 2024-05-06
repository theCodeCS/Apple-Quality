# Apple Quality Dataset

## Overview
The Apple Quality dataset is a comprehensive collection of data pertaining to various attributes of apples, meticulously curated for the purpose of understanding the factors influencing apple quality. This dataset encompasses a wide range of characteristics such as color, weight, size, surface texture, presence of defects, and an overall quality rating assigned to each apple sample.

## Motivation
The motivation behind compiling this dataset is to facilitate research and analysis aimed at improving the quality assessment process of apples. By investigating the relationships between different apple attributes and their quality ratings, researchers and practitioners can gain insights into the key factors that contribute to the overall desirability of apples in commercial and consumer markets.

## Context
Apples are among the most widely consumed fruits globally, prized for their nutritional value and diverse culinary applications. However, assessing the quality of apples can be a complex task influenced by numerous factors such as appearance, texture, taste, and nutritional content. Understanding the multidimensional nature of apple quality is essential for growers, distributors, and retailers to optimize production, storage, and marketing strategies.

## Data Collection
The data in this dataset was collected through meticulous observation and measurement of individual apples across various farms and orchards. Each apple was examined for its color, weighed for its mass, categorized based on its size, evaluated for surface texture, inspected for the presence of defects, and ultimately assigned a quality rating by trained assessors.

## Content
The dataset comprises the following attributes:

- **Color**: The visual appearance of the apple's skin, categorized into distinct color categories (e.g., Red, Green, Yellow).
- **Weight**: The mass of the apple measured in grams.
- **Size**: The dimensional classification of the apple, ranging from Small to Large based on standardized criteria.
- **Surface**: The tactile quality of the apple's skin surface, characterized as Smooth or Rough.
- **Defects**: Indication of any visible imperfections or abnormalities present on the apple's surface (e.g., bruises, blemishes).
- **Quality**: An ordinal rating assigned to each apple indicating its overall quality, typically ranging from 1 (lowest) to 5 (highest).

## Approach
In this notebook, we have utilized various tabular predictive models for our Binary Classification Dataset. Models like XGBoost, Catboost, and a Voting Classifier with an ensemble of various linear and non-linear models were ensembled together. Then we implemented our deep neural network with PyTorch, learning to create our own custom classes for the model, dataset, training, and validation loops. 

## Optimization
From there, we further optimized our models based on the hyperparameter tuning library - Optuna, with the goal of reaching a high AUROC score for our binary classification dataset.

## Results
Our end results were impressive: we achieved an average accuracy of 91% for our voting classifier, and our PyTorch (DNN) model averaged an accuracy of 89% with an outstanding 96% AUC.

## Insights
Through this exploration, we learned that the appropriate models needed for binary classification datasets require understanding the underlying features of our data. Given that tabular data can be challenging for a DNN to predict, more refined predictive models are well-designed for such tasks.