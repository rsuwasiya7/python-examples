import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()


labours_with_cost = {"Mahesh" : 500, "Mithilesh": 400, "Ramesh" : 600, "Sumesh" : 700, "Naresh":1000, "Himesh":1200}
logger.info(labours_with_cost)

logger.info(f"Cost of Himesh is {labours_with_cost['Himesh']}")
labours_with_cost["Himesh"] = 1500
labours_with_cost["Naresh"] = 1100
logger.info(labours_with_cost)


logger.info(labours_with_cost.keys())
logger.info(labours_with_cost.values())
logger.info(labours_with_cost.items())

for k in labours_with_cost:
    logger.info(f"{k} {labours_with_cost[k]}")

for key,value in labours_with_cost.items():
    logger.info(f"{key} {value}")

nested_api = {
  "pipeline_id": "pl_etl_sales_prod_042",
  "pipeline_name": "Daily Sales Aggregator",
  "execution_date": "2026-07-16T12:00:00Z",
  "status": "Failed",
  "cluster_configuration": {
    "engine": "Apache Spark",
    "version": "3.5.1",
    "node_type": "m5.xlarge",
    "worker_nodes": 8,
    "auto_scaling": True
  },
  "stages": [
    {
      "stage_name": "Extraction",
      "sequence_order": 1,
      "status": "Success",
      "records_read": 1450000,
      "records_written": 1450000,
      "error_details": None
    },
    {
      "stage_name": "Transformation",
      "sequence_order": 2,
      "status": "Failed",
      "records_read": 1450000,
      "records_written": 412000,
      "error_details": {
        "error_type": "NonePointerException",
        "corrupted_files": [
          "s3://production-lake/raw/sales/2026-07-16/part-002.csv",
          "s3://production-lake/raw/sales/2026-07-16/part-005.csv"
        ],
        "line_number": 432
      }
    },
    {
      "stage_name": "Loading",
      "sequence_order": 3,
      "status": "Skipped",
      "records_read": 0,
      "records_written": 0,
      "error_details": None
    }
  ],
  "metrics": {
    "duration_seconds": 184.5,
    "data_processed_gb": 4.2
  }
}

logger.info(f"{nested_api['stages'][1]['error_details']['corrupted_files']}")