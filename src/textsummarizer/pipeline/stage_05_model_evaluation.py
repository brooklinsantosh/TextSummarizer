from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_evaluation import ModelEvaluation
from textsummarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self) -> None:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.evaluate()

