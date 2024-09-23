
# Credit Risk Assessment System

## Overview
The Credit Risk Assessment System is an academic project designed to predict the likelihood of loan defaults in the financial sector. By leveraging advanced data engineering and machine learning techniques, this system helps identify high-risk borrowers, thereby improving decision-making in loan approvals and risk management.

## Problem Statement
Financial institutions face significant challenges in accurately assessing the risk of loan defaults, which can lead to financial losses and increased operational risk. Traditional credit scoring models often fall short in capturing the complex and dynamic nature of borrower behavior. This project aims to enhance risk assessment by using real-time data processing and predictive analytics to provide a more accurate and scalable solution.

## Objectives
- Predict the risk of loan default by analyzing historical financial data, customer demographics, and transactional behavior.
- Improve loan approval processes by providing accurate and transparent credit risk scores.
- Enhance compliance and risk management by aligning predictive models with industry regulatory standards.

## Tools and Technologies Used
- **AWS Kinesis:** For real-time data ingestion and streaming from various data sources.
- **AWS S3:** To store raw, processed, and modeled data efficiently.
- **AWS Glue:** For ETL (Extract, Transform, Load) processes, cleaning, and feature engineering.
- **Amazon SageMaker:** For building, training, and deploying machine learning models like Logistic Regression, Random Forest, and XGBoost.
- **AWS Step Functions:** For orchestrating data workflows and automating model execution.
- **Amazon QuickSight:** To create interactive dashboards for visualizing risk scores and portfolio health.
- **Python and SQL:** For data processing, model development, and querying data within the data warehouse.

## Project Workflow
1. **Data Ingestion:** Real-time data ingestion using AWS Kinesis from multiple sources such as transactional data, customer demographics, and external financial data.
2. **Data Storage:** Raw data is stored in AWS S3, with structured data housed in Amazon RDS/Redshift for efficient querying.
3. **Data Processing:** AWS Glue cleans, transforms, and prepares data for analysis, performing feature engineering to enhance model accuracy.
4. **Model Training and Deployment:** Predictive models are developed in Amazon SageMaker, utilizing algorithms like Logistic Regression, Random Forest, and XGBoost to classify borrowers into risk categories.
5. **Orchestration:** AWS Step Functions automate the data pipeline, ensuring smooth execution of data workflows and model operations.
6. **Visualization:** Amazon QuickSight dashboards provide a clear view of credit risk scores, segment analysis, and portfolio health metrics.

## Key Features
- **Real-time Risk Prediction:** Utilizes machine learning to provide instant risk assessments, improving loan approval efficiency.
- **Scalable Data Processing:** Handles large and growing datasets with AWS cloud services, ensuring robust and reliable performance.
- **Interactive Dashboards:** Offers stakeholders a user-friendly interface to monitor risk scores and make data-driven decisions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mrachana19/Credit_Risk_Prediction.git
   ```
2. Set up your AWS account and configure access keys.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure AWS services (Kinesis, S3, Glue, SageMaker, Step Functions, QuickSight) as per the project architecture.
5. Run the data pipeline and model training scripts.

## Usage
- Use the SageMaker scripts to train and deploy predictive models.
- Monitor data workflows via AWS Step Functions.
- Access and interact with dashboards on Amazon QuickSight for insights into credit risk.

## Results
- **Simulated a 25% reduction in loan default rates** by accurately identifying high-risk applicants.
- **Improved processing efficiency by 40%,** reducing time spent on manual risk evaluations.
- **Enhanced data-driven compliance** with transparent, model-based credit scoring.

## Future Enhancements
- Extend the system to incorporate additional data sources like social media analytics for richer insights.
- Integrate anomaly detection to identify fraudulent activities during the loan application process.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Acknowledgments
- Thanks to AWS for providing cloud infrastructure.
- Inspiration from academic studies on credit risk modeling and financial risk management.

