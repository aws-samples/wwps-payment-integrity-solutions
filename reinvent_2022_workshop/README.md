# Identify improper payments with analytics and machine learning

## Introduction

Many government agencies employ rules-based systems to identify improper payments. Improper payments are those that either should not be made, or are made in the incorrect amount, due to fraud or other errors. Rules-based techniques involve manually researching, understanding, and identifying patterns and heuristics that are then applied as business rules to flag potential issues. However, this approach increases the amount of time taken to identify improper payments due to the heavy dependence on continuously adding and updating rules based on ever changing and newly emerging patterns. In addition, traditional techniques fail to capture emerging threats such as synthetic ID fraud.

In synthetic ID fraud, a fraudster applies for government benefits or services using a real Social Security number combined with fake transaction information and an address or a bank account where they can receive funds. To mitigate this type of fraud, agencies need to complement their rules-based improper payment detection systems with machine learning (ML) techniques. By using ML on a large number of disparate but related data sources, including social media, agencies can formulate a more comprehensive risk score for each individual or transaction to help investigators identify improper payments efficiently.

The goal of this workshop is to introduce you to ML techniques that help identify fraud. We will work through two labs to accomplish this objective:

- [Lab1: Supervised Learning using SageMaker Built-in Algorithm XGBoost with a Real-Time Endpoint](./classification-lab1.ipynb)
- [Lab2: Supervised Learning using open source Random Forest Algorithm with Batch Transform](./classification-lab2.ipynb)

## Getting started

Coming Soon...  

You can run this workshop in all commercial AWS regions where Amazon SageMaker is available.

## Datasets

The curated dataset used for this lab comes from the following Centers for Medicare & Medicaid Services dataset: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service
    
## License

The contents of this workshop are licensed under the [Apache 2.0 License](./LICENSE).

## Authors
[Sherry Ding](https://www.linkedin.com/): Sr. AI/ML Solutions Architect
<br />
[Nate Haynes](https://www.linkedin.com/): Sr. Solutions Architect
<br />
[Sanjeev Pulapaka](https://www.linkedin.com/): Sr. Solutions Architect
<br />
[Bill Screen](https://www.linkedin.com/): Sr. Solutions Architect
<br />
[Aaron Sengstacken](https://www.linkedin.com/): Sr. AI/ML Solutions Architect
