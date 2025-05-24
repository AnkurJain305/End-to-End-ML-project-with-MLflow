import os
import yaml
from mlProject import logger
import json
from ensure import ensure_annotations
from box import ConfigBox, BoxValueError
from pathlib import Path
from typing import Any
import joblib


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
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data to a JSON file.
    
    Args:
        path_to_json (Path): The path to the JSON file.
        data (Any): The data to save in the JSON file.
    """
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"json file:{path} saved successfully") 

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.
    
    Args:
        path (Path): The path to the JSON file.
        
    Returns:
        Any: The data loaded from the JSON file.
    """
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    logger.info(f"json file:{path} loaded successfully")
    return ConfigBox(data)

@ensure_annotations    
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file.
    
    Args:
        data (Any): The data to save in the binary file.
        path (Path): The path to the binary file.
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file:{path} saved successfully")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file.
    
    Args:
        path (Path): The path to the binary file.
        
    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file:{path} loaded successfully")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file or directory.
    
    Args:
        path (Path): The path to the file or directory.
        
    Returns:
        str: The size of the file or directory in a human-readable format.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

  
    