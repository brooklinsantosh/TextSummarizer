from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textsummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textsummarizer.logging import logger

# Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started! <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed! <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

# Data Valifdation
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started! <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed! <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

# Data Transformation
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started! <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> {STAGE_NAME} completed! <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

# Model Trainer
STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started! <<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> {STAGE_NAME} completed! <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

# Model Trainer
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} started! <<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>> {STAGE_NAME} completed! <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e