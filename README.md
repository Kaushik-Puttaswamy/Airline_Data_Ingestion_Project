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
