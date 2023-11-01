import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from textsummarizer.logging import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: Returns config as ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
#@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """Create list of directories

    Args:
        path_to_directories (list): list of path for the directories
        verbose (bool, optional): ignore if multiple dirs to be created. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of the given file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"