import warnings
import flwr as fl
import numpy as np
import os
import argparse

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss

import utils


class FlowerClient(fl.client.NumPyClient):
    """Client interface"""
    def get_parameters(self, config):  
        return utils.get_model_parameters(model)

    def fit(self, parameters, config): 
        utils.set_model_params(model, parameters)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X_train, y_train)
#         print(f"Training finished for round {config['server_round']}")
        return utils.get_model_parameters(model), len(X_train), {}

    def evaluate(self, parameters, config):
        utils.set_model_params(model, parameters)
        loss = log_loss(y_test, model.predict_proba(X_test))
        accuracy = model.score(X_test, y_test)
        return loss, len(X_test),  {"accuracy": accuracy}


if __name__ == "__main__":

    print("extracting arguments")
    parser = argparse.ArgumentParser()

    """Hyperparameters sent by the client"""
    # Algorithm related hyperparameters
    parser.add_argument("--penalty", type=str, default="l2")
    parser.add_argument("--max-iter", type=int, default=3)
    
    # Server ip address that client talks to
    parser.add_argument("--server-address", type=str, default="0.0.0.0:8080")  # "0.0.0.0:8080" for running on same machine

    # Data, model, and output directories
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--test", type=str, default=os.environ.get("SM_CHANNEL_TEST"))
    
    parser.add_argument("--train-file", type=str, default="cms_payment_train.csv")
    parser.add_argument("--test-file", type=str, default="cms_payment_validation.csv")    

    args, _ = parser.parse_known_args()

    # Load data
    (X_train, y_train), (X_test, y_test) = utils.load_data(args.train, args.train_file, args.train, args.test_file)
    print("Data Loaded", X_train.shape)
    
    """Initialize and train model on the client"""
    model = LogisticRegression(
        penalty = args.penalty,
        max_iter = args.max_iter,  
        warm_start = True,  # prevent refreshing weights when fitting
    )
    
    utils.set_initial_params(model)
    print("parameters : ", utils.set_initial_params(model))
    fl_client = FlowerClient()
    print(fl_client)
    fl.client.start_numpy_client(
        server_address = args.server_address, 
        client = fl_client
    )  
    
    utils.save_model(args.model_dir, model)