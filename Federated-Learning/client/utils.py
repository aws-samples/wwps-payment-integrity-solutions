from typing import Tuple, Union
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os
import joblib


XY = Tuple[np.ndarray, np.ndarray]
Dataset = Tuple[XY, XY]
LogRegParams = Union[XY, Tuple[np.ndarray]]


def get_model_parameters(model: LogisticRegression) -> LogRegParams:
    """Returns the paramters of a sklearn LogisticRegression model."""
    if model.fit_intercept:
        params = [
            model.coef_,
            model.intercept_,
        ]
    else:
        params = [
            model.coef_,
        ]
    return params


def set_model_params(model: LogisticRegression, params: LogRegParams) -> LogisticRegression:
    """Sets the parameters of a sklean LogisticRegression model."""
    model.coef_ = params[0]
    if model.fit_intercept:
        model.intercept_ = params[1]
    return model


def set_initial_params(model: LogisticRegression):
    """Sets initial parameters as zeros Required since model params are
    uninitialized until model.fit is called.

    But server asks for initial parameters from clients at launch. Refer
    to sklearn.linear_model.LogisticRegression documentation for more
    information.
    """
    n_classes = 2  # fraud vs non-fraud
    n_features = 49  # Number of features in dataset
    model.classes_ = np.array([i for i in range(n_classes)])

    model.coef_ = np.zeros((n_classes, n_features))
    if model.fit_intercept:
        model.intercept_ = np.zeros((n_classes,))


def load_data(train_path, train_file, test_path, test_file) -> Dataset:
    """Load the dataset"""
    train_df = pd.read_csv(os.path.join(train_path, train_file), header=None)
    test_df = pd.read_csv(os.path.join(test_path, test_file), header=None)
    X_train = train_df[train_df.columns[1:]]
    X_test = test_df[test_df.columns[1:]]
    y_train = train_df[train_df.columns[0]]
    y_test = test_df[test_df.columns[0]]    
    return (X_train, y_train), (X_test, y_test)


def save_model(model_path, model):
    """Save trained model"""
    path = os.path.join(model_path, "model.joblib")
    joblib.dump(model, path)
    print("model persisted at " + path)
