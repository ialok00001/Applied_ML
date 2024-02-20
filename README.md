# Applied_ML


This is my submission to the Assignments in the Applied Machine Learning course.


## Assignment 1

It involves working on a spam classification dataset, where we have to preprocess on this dataset, create train, validation and test dataset from it and apply Machine Learning models on them to create a spam classifier, i.e., classifying whether a message is spam or a ham (not spam). This involves fitting three models to it.

#### Naive Bayes
#### Logistic Regression
#### Random Forest Classifier

Then, a grid search is applied (wherever necessary) for the f1 score (to optimize both precision and recall).

At the end, models are compared based on accuracy and f1 score. Sometimes where there these metrics are similar, the decision metric goes to precision. This is because in spam classification, marking a ham as spam is more expensive as in this case the reciever might not get an important message. Hence we need to minimize False Positives, i.e, maximize Precision.

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
