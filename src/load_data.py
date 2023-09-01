import os
import yaml
import argparse

def get_raw_data(config_path):
    config = get_params(config_path)
    path = config["data_source"]
    print(path)

def get_params(config_path):
    with open(config_path) as f :
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()
    print(args.config)
    get_raw_data(config_path=args.config)

