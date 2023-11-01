import textsummarizer.constants as const
from textsummarizer.utils.common import read_yaml, create_directories

from textsummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(self, 
                 config_file_path = const.CONFIG_FILE_PATH,
                 params_file_path = const.PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )
        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_traansformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_name
        )
        return data_traansformation_config