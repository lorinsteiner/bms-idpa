# About this project

This repository contains the code for our **IDPA** (_interdisziplinäre Projektarbeit_), an interdisciplinary research paper required for the Swiss vocational baccalaureate (_Berufsmaturität_). The paper combines **computer science** and **mathematics** and is written in German. Team: Levin, Lorin and Tobias, apprentices in application development.

## Research goal

We run an **ablation study** on a fully connected neural network. Starting from a fixed baseline model, we change **one factor at a time** and measure how it affects classification performance:

| Factor                                   | Baseline          |
| ---------------------------------------- | ----------------- |
| Activation function                      | ReLU              |
| Weight initialization                    | He initialization |
| Network depth (hidden layers)            | 2                 |
| Network width (neurons per hidden layer) | 128               |
| Optimizer                                | Adam              |

For each factor we compare the baseline with two variants, which gives 11 configurations in total. All other settings stay as constant as possible.

## Dataset

[Fashion-MNIST](https://www.kaggle.com/datasets/zalando-research/fashionmnist) (Xiao, Rasul & Vollgraf, 2017): 60,000 training and 10,000 test images (28 × 28 pixels, grayscale) in 10 clothing categories, MIT license. We use a fixed split into training, validation and test data.

## Method

- Each configuration is trained **5 times with documented random seeds** so we can estimate run-to-run variation.
- During training we record loss and accuracy for every epoch.
- We evaluate:
  - final **classification accuracy** on the test set
  - **learning speed**: the number of epochs needed to reach a learning target defined before the main experiments
  - **variation** of the results across repeated runs
- We analyse the results with descriptive statistics (mean, standard deviation, min/max) and visualize them as learning curves and comparison plots.

## Scope and limitations

Our results apply only to the chosen dataset, architecture and experimental settings. They do not generalize to other datasets or network types. When we change network depth or width, the number of trainable parameters changes too, and we account for this when interpreting the results.

## Timeline

Final submission: **16 February 2027**
