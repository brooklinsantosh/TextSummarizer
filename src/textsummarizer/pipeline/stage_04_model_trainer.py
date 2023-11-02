from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_trainer import ModelTrainer
from textsummarizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self) -> None:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()