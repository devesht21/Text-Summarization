from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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


STAGE_NAME = "3 - Data Transformation"

try:
    logger.info(f"-------- Stage {STAGE_NAME} Started --------")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"-------- Stage {STAGE_NAME} Completed --------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "4 - Model Training"

try:
    logger.info(f"-------- Stage {STAGE_NAME} Started --------")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"-------- Stage {STAGE_NAME} Completed --------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "5 - Model Evaluation"

try:
    logger.info(f"-------- Stage {STAGE_NAME} Started --------")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"-------- Stage {STAGE_NAME} Completed --------")
except Exception as e:
    logger.exception(e)
    raise e
