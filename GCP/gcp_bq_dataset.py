from google.cloud import bigquery
import os 

gcp_project_name = str(os.getenv("GCP_PROJECT_NAME"))
gcp_bq_dataset = str(os.getenv("GCP_BQ_DS"))
gcp_column_value = str(os.getenv("GCP_COL"))

def query_gcp_database(big_query_client: bigquery.Client):
    frequent_failure_query = f"""
    SELECT {gcp_column_val}, COUNT(*) AS Failure
    FROM `{gcp_bq_dataset}`
    WHERE status LIKE '%failure%'
    AND dateTimeIngested >= TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    GROUP BY failureReason
    ORDER BY Failure DESC
    LIMIT 5;
    """

    query_job = big_query_client.query(query=frequent_failure_query)
    frequent_failure_cause = query_job.result()

    for row in frequent_failure_cause:
        print(f"{row.failureReason}: {row.Failure}")
    
if __name__ == "__main__":
    # Initialize a BigQuery client
    client = bigquery.Client(project=f'{gcp_project_name}')

    # Call the function with the client
    query_gcp_database(client)