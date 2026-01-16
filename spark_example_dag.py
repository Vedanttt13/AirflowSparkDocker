from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'spark_example_dag',
    default_args=default_args,
    description='A simple Spark DAG example',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

def start_task():
    print("Starting Spark job execution...")

def end_task():
    print("Spark job execution completed!")

# Task 1: Start
start = PythonOperator(
    task_id='start',
    python_callable=start_task,
    dag=dag,
)

# Task 2: Submit Spark Job
spark_job = SparkSubmitOperator(
    task_id='submit_spark_job',
    application='/opt/airflow/jobs/sample_spark_job.py',
    conn_id='spark_default',
    verbose=True,
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.memory': '1g',
        'spark.executor.cores': '1',
        'spark.driver.memory': '1g',
    },
    dag=dag,
)

# Task 3: End
end = PythonOperator(
    task_id='end',
    python_callable=end_task,
    dag=dag,
)

# Task dependencies
start >> spark_job >> end
