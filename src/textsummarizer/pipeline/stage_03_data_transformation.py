from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
       pass
    
    def main(self):
        config = ConfigurationManager()
        data_tranformation_config = config.get_data_transformation_config()
        data_tranformation = DataTransformation(config= data_tranformation_config)
        data_tranformation.convert()