# Airline Data Ingestion & Processing on AWS

## Project Overview

The Airline Data Ingestion & Processing Project is a cloud-based ETL pipeline built on AWS to process airline flight data. The project automates data ingestion, transformation, and storage using AWS S3, Glue, Redshift, EventBridge, Step Functions, and SNS. The processed data is stored in Amazon Redshift for further querying and analysis.

## Project Architecture

The architecture consists of:

1.	Data Source: Flight data in CSV format is uploaded to an S3 bucket.
 
2.	Event Trigger: AWS EventBridge detects new file uploads and triggers a Step Function workflow.
 
3.	Step Functions: Automates the ETL process by orchestrating Glue Crawlers and Glue Jobs.
 
4.	AWS Glue ETL: Processes and transforms raw flight data.
 
5.	Amazon Redshift: Stores the cleaned and processed data for querying.
 
6.	Amazon SNS: Sends notifications about job status.

## Project Execution on AWS

1. Setting Up EventBridge

📌 [Include the screenshot: Event_Bridge_Setup.png]

EventBridge monitors the S3 bucket for new CSV files and triggers Step Functions.

EventBridge Rule Configuration (event_bridge_rule.json):

```
{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": ["airlines-data-ingestion-project"]
    },
    "object": {
      "key": [{
        "suffix": ".csv"
      }]
    }
  }
}
```
📌 [Include the screenshot: Event_Bridge_Permision_Policies.png]

2. Setting Up AWS Glue ETL Job

The Glue job (glue_etl_job.py) extracts flight data from S3, enriches it with airport details, and loads it into Redshift.

📌 [Include the screenshot: Glue_ETL_Job_Status.png]

Key steps:
	
 •	Read raw flight data from S3.
	
 •	Join with airport codes for enrichment.
	
 •	Store processed data in Amazon Redshift.

3. Step Functions Orchestration

Step Functions automate the execution of Glue Crawlers and Glue Jobs.

📌 [Include the screenshot: Step_Function_Job_Graph_View.png]

Configuration (step_function_config.json):
	
 •	Starts Glue Crawlers to catalog raw data.
	
 •	Checks for crawler completion.
	
 •	Runs Glue ETL job to transform data.
	
 •	Sends success/failure notifications via SNS.


📌 [Include the screenshot: Step_Function_Job_Setup_Graph_View.png]

📌 [Include the screenshot: Step_Function_Permision_Policies.png]

📌 [Include the screenshot: Step_Function_Status.png]

4. Amazon Redshift for Processed Data Storage

Redshift tables store the cleaned flight data for analysis.

Schema & Table Creation (redshift_create_table_commands.txt):

```
CREATE TABLE airlines.daily_flights_processed (
    carrier VARCHAR(10),
    dep_airport VARCHAR(200),
    arr_airport VARCHAR(200),
    dep_city VARCHAR(100),
    arr_city VARCHAR(100),
    dep_state VARCHAR(100),
    arr_state VARCHAR(100),
    dep_delay BIGINT,
    arr_delay BIGINT
);



```
📌 [Include the screenshot: Redshift_Cluster_Setup.png]

📌 [Include the screenshot: Redshift_Permision_Policies.png]

Querying processed data:

```
SELECT * FROM airlines.daily_flights_processed LIMIT 5;

```
📌 [Include the screenshot: Querying_Flight_Processed_Data_in_Redshift.png]

5. S3 Data Storage

Flight data and airport codes are stored in S3 before processing.
📌 [Include the screenshot: S3_Setup_for_Airportdim_and_Flight_Data.png]

6. SNS Notifications for Job Status

Amazon SNS sends notifications on Glue job success/failure.
📌 [Include the screenshot: SNS_Notification_of_Job_Status.png]


How to Run the Project
	
 1.	Upload new flight data to the S3 bucket (airlines-data-ingestion-project).
	
 2.	EventBridge triggers the Step Function workflow.
	
 3.	Glue ETL job processes the data.
	
 4.	Processed data is stored in Amazon Redshift.
	
 5.	Query Redshift for flight insights.

## Conclusion

This project automates airline data ingestion, transformation, and storage using AWS services, making it scalable and efficient. 🚀

