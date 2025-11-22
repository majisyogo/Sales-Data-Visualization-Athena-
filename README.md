# 【Sales Data Visualization Project】

This repository is a sample project to analyze and visualize sales data using **S3 → Athena → QuickSight** with AWS CLI.

## Folder Structure
【Sales Data Visualization Project】
⇒data(CSV)
⇒query Athena(SQL)
⇒script
⇒README.md

## Prerequisites
- AWS account (QuickSight account already set up)
- AWS CLI v2 installed
- S3 bucket for Athena available

## Workflow
1. Place sample CSV files in `data/`
2. Create Athena tables using SQL in `queries/`
3. Execute Athena queries via `scripts/run_athena_query.sh`
4. Create QuickSight datasets via `scripts/create_quicksight_dataset.sh`
5. Visualize data in QuickSight dashboards

## Example Analyses
- Monthly sales trends (line chart)
- Customer sales ranking (bar chart)
- Sales performance by salesperson
- Regional sales distribution
