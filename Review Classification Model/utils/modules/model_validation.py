import json
import pickle
import logging
import os
import warnings

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix, 
                             ConfusionMatrixDisplay, precision_recall_fscore_support, 
                             precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

warnings.filterwarnings("ignore")


class ModelValidation:
    def __init__(self, df:pd.DataFrame, processed_text:str = None, ids_col:str = None, labels_col:str = None):
        self.df = df
        self.X = df[processed_text]
        self.y = df[ids_col]
        uniqueLabel = df[[ids_col, labels_col]].drop_duplicates()
        self.idx2label = dict(zip(uniqueLabel[ids_col], uniqueLabel[labels_col]))


    def fit_transform(self):
        count_vectorizer = CountVectorizer()
        self.X_vectorized = count_vectorizer.fit_transform(self.X)
        #save count vectorizer for data preprocessing in the main app (deploy)
        #joblib.dump(count_vectorizer, 'data/data_processed/count_vectorizer.pkl')
        #print("count vectorizer trained successfully")
        
    def transform_tfidf(self):
        tfidf_transformer = TfidfTransformer()
        self.X_tfidf = tfidf_transformer.fit_transform(self.X_vectorized)
        # joblib.dump(X_tfidf, 'data/data_processed/X_tfidf.pkl')
        # print("X_tfidf trained successfully stored")

    def split_train_test(
        self, test_size: float = 0.3, random_state: int = 42
    ):
        """
        This function splits the data into train and test
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X_tfidf, self.y, test_size=test_size, random_state=random_state
        )


    
    def model_fit(
        self,
        model:object
    ):
        self.model = model
        self.model.fit(self.X_train, self.y_train)


    
    def display_classification_report(
        self,
        use_cv = False
    ):
        """
        This function display the classification report
        """
        
    
        # empty list to store the metrics
        metric = []
        y_train_pred_proba = self.model.predict_proba(self.X_train)
        y_test_pred_proba = self.model.predict_proba(self.X_test)
        roc_auc_score_train = round(
            roc_auc_score(
                self.y_train, y_train_pred_proba, average="weighted", multi_class="ovr"
            ),
            2,
        )
        roc_auc_score_test = round(
            roc_auc_score(
                self.y_test, y_test_pred_proba, average="weighted", multi_class="ovr"
            ),
            2,
        )
    
        print("ROC AUC Score Train:", roc_auc_score_train)
        print("ROC AUC Score Test:", roc_auc_score_test)
        
        # adding the metrics to the list
        metric.extend([roc_auc_score_train, roc_auc_score_test])
    
    
        y_train_pred = self.model.predict(self.X_train)
        y_test_pred = self.model.predict(self.X_test)
    
        (
            precision_train,
            recall_train,
            fscore_train,
            support_train,
        ) = precision_recall_fscore_support(self.y_train, y_train_pred, average="weighted")
        (
            precision_test,
            recall_test,
            fscore_test,
            support_test,
        ) = precision_recall_fscore_support(self.y_test, y_test_pred, average="weighted")
    
        print("precision_train", precision_train)
        print("precision_test", precision_test)
        print("recall_train", recall_train)
        print("recall_test", recall_test)
            
        try:
            if use_cv:
                best_params = self.model.best_params_
            else:
                best_params = self.model.get_params()
    
        except AttributeError as e:
            print(f"Error: {e}")
    
        acc_score_train = round(accuracy_score(self.y_train, y_train_pred), 2)
        acc_score_test = round(accuracy_score(self.y_test, y_test_pred), 2)
    
        metric.extend(
            [
                acc_score_train,
                acc_score_test,
                round(precision_train, 2),
                round(precision_test, 2),
                round(recall_train, 2),
                round(recall_test, 2),
                round(fscore_train, 2),
                round(fscore_test, 2),
            ]
        )
    
        print("Train Accuracy: ", acc_score_train)
        print("Test Accuracy: ", acc_score_test)
    
        model_report_train = classification_report(self.y_train, y_train_pred)
        model_report_test = classification_report(self.y_test, y_test_pred)
    
        print("Classification Report for Train:\n", model_report_train)
        print("Classification Report for Test:\n", model_report_test)
    
        # Plot the confusion matrix
        fig, ax = plt.subplots(figsize=(12, 8))
    
        # Create the confusion matrix with labels decoded
        decoded_y_test_pred = [self.idx2label[idx] for idx in y_test_pred]
        decoded_y_test = [self.idx2label[idx] for idx in self.y_test]
    
        cm = confusion_matrix(decoded_y_test, decoded_y_test_pred)
        cmp = ConfusionMatrixDisplay(cm, display_labels=list(self.idx2label.values()))
        cmp.plot(ax=ax)
    
        plt.xticks(rotation=80)
        plt.show()
    
        # return metric
    
    
    def print_best_score_params(model):
        """
        This functions print best score and best hyperparameters for baselines models
        """
        print("Best Score: ", model.best_score_)
        print("Best Hyperparameters: ", model.best_params_)