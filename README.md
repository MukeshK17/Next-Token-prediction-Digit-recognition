# Repository for Machine Learning Assignments (ES335, 2024-25)

This repository was created as part of the assignments for the course **ES335: Machine Learning (2024-25)** at the **Indian Institute of Technology Gandhinagar**.

## Contributors
- Mukesh  
- Rahul  
- Srajan  
- Tanuj  

Special thanks to our instructor, **Prof. Nipun Batra**, for designing these engaging and insightful assignments.

---

## Overview

This repository contains models and their outputs for two tasks:  
1. **Next-Token Prediction**  
2. **Digit Recognition**

---

## Digit Recognition Task

The digit recognition task was performed using three different models, trained on the MNIST dataset:  
1. **Multilayer Perceptron (MLP)**  
2. **Multiclass Logistic Regression**  
3. **Random Forest Classifier (RF)**  

### Key Observations
#### Accuracy Comparison
- **MLP** and **Random Forest (RF)** achieved almost identical and very high accuracy, demonstrating their effectiveness in learning the data.  
- **Multiclass Logistic Regression** achieved an accuracy of approximately **92%**, which is good but lower compared to MLP and RF.  
  - This difference is likely due to the large number of neurons in the MLP and the numerous trees in the RF, both of which enhance their ability to capture patterns in the data.

#### Fashion MNIST Results
- When the **MLP model** was used to train and predict outputs for the **Fashion MNIST dataset**, the accuracy dropped to approximately **85%**, reflecting the increased complexity of the dataset.  
- These results highlight the need for more sophisticated architectures to handle complex datasets like Fashion MNIST.

---

## Additional Insights
- **t-SNE Plots:**  
  The t-SNE visualizations for both the MNIST and Fashion MNIST datasets using the same MLP model illustrate the differences in complexity between the datasets. These plots further emphasize the challenges in achieving higher accuracy on more complex datasets like Fashion MNIST.

---

## Model Evaluation
Each model was compared based on the following metrics:  
- **F1-Score**  
- **Confusion Matrix**  
- **Accuracy**  

These comparisons provide valuable insights into the performance of each model and their suitability for specific tasks.

---

Feel free to explore the repository to review the models, code, and results.

---
