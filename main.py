from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textSummarizer.logging import logger


STAGE_NAME = "1 - Data Ingestion"

try:
    logger.info(f"-------- Stage {STAGE_NAME} Started --------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"-------- Stage {STAGE_NAME} Completed --------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "2 - Data Validation"

try:
    logger.info(f"-------- Stage {STAGE_NAME} Started --------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"-------- Stage {STAGE_NAME} Completed --------")
except Exception as e:
    logger.exception(e)
    raise e
