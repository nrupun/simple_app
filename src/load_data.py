import os
import yaml
import argparse
from get_data import get_data, read_params

def load_save_data(config_path):
    config = read_params(config_path)
    data = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in data.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    # print(raw_data_path)
    data.to_csv(raw_data_path, sep=",", index = False, header = new_cols)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()
    load_save_data(config_path=args.config)

