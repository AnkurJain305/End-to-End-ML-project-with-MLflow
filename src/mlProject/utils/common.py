import os
import box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a Box object.
    
    Args:
        path_to_yaml (Path): The path to the YAML file.
        
    Returns:
        configBox: The contents of the YAML file as a Box object.
    """
    try:
        with open(path_to_yaml, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise
