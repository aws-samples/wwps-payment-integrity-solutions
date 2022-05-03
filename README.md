## This repo contains code for payment integrity solutions in Public Sector

Solutions are organized by folders as follows:

1. Machine Learning - The folder contains all Machine Learning related code that predicts fraudulent medicare providers from a PUF Medicare Data Set from CMS. Code in each folder can be run independently.

- Anomaly Detection with Random Cut Forest
- Anomaly Detection using Auto Encoders
- Classification with XGBoost
- Classification with GNN using DGL (MXnet)
- Classification with GNN using Neptune ML

2. Data Preparation - This folder contains sample code to process the PUF Meducare Data Set from CMS and prepare the data for ML

Please open the data_load.ipynb file for instructions on using this solution. 


## AWS SageMaker Service Limits 
A number of notebooks may need a potential increase in Service Limits. Please ensure you get approval for the following at a minimum:
ml.r5.xlarge for endpoint usage - 2 
ml.p3.2xlarge for training job usage - 2 
ml.r5.large for processing job usage - 2
ml.r5.24xlarge for processing job usage - 3
ml.r5.24xlarge for endpoint usage - 3 
ml.g4dn.xlarge - 1

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

