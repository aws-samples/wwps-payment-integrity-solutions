# Identify improper payments with machine learning techiniques

## Introduction

Many government agencies employ rules-based systems to identify improper payments. Improper payments are those that either should not be made, or are made in the incorrect amount, due to fraud or other errors. Rules-based techniques involve manually researching, understanding, and identifying patterns and heuristics that are then applied as business rules to flag potential issues. However, this approach increases the amount of time taken to identify improper payments due to the heavy dependence on continuously adding and updating rules based on ever changing and newly emerging patterns. In addition, traditional techniques fail to capture emerging threats such as synthetic ID fraud.

In synthetic ID fraud, a fraudster applies for government benefits or services using a real Social Security number combined with fake transaction information and an address or a bank account where they can receive funds. To mitigate this type of fraud, agencies need to complement their rules-based improper payment detection systems with machine learning (ML) techniques. By using ML on a large number of disparate but related data sources, including social media, agencies can formulate a more comprehensive risk score for each individual or transaction to help investigators identify improper payments efficiently.


## Content

This GitHub repo includes multiple folders according to different content creation projects. All projects are related to identify improper payments for public sector customers using machine learning techniques.

- Machine Learning folder listed various ways including unsupervised (Random Cut Forest) and supervised (Random Forest, XgBoost, Graph Neural Network) approaches to detect fraud. It also includes bias and model explainability analysis. Together with Data Preparation folder, they are related to blog "[How public sector agencies can identify improper payments with machine learning](https://aws.amazon.com/blogs/publicsector/how-public-sector-agencies-identify-improper-payments-machine-learning/)". 

- Federated-Learning folder provides an example of running federated learning on Amazon SageMaker in some situation that data cannot be centralizaed into one account (e.g., due to security and privacy regulations), which is common for public sector customers. It uses improper payments identification as an example, and is related to blog "Machine Learning with Decentralized Training Data using Federated Learning on Amazon SageMaker"

- reinvent_2022_workshop folder is a builder's session created for AWS ReInvent 2022. The goal of this workshop is to introduce you to ML techniques that help identify fraud. It includes two labs to accomplish this objective.


## Dataset

The datsset used in Data Preparation folder comes from the Centers for Medicare & Medicaid Services dataset: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service

Both Federated-Learning and reinvent_2022_workshop use a recurated dataset coming from the above mentioned dataset.
    
## License

The contents of this workshop are licensed under the [Apache 2.0 License](./LICENSE).