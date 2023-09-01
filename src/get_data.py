# Read params
# Process it
# Return the dataframe

import os
import yaml
import pandas as pd
import argparse

def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    print(df.head())

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default = "params.yaml")
    args = parser.parse_args()
    get_data(config_path=args.config)
    
