import os
import argparse
import pandas as pd
from get_data import read_params
from sklearn.model_selection import train_test_split

def split_data(config_path):
    config = read_params(config_path)
    raw_data_path = config['load_data']['raw_dataset_csv']
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    split_size=config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep=',', encoding='utf-8')
    # df_data =df.iloc[:,0:-1]
    # df_target = df.iloc[:,-1:]
    # df_data_train, df_data_test, df_target_train, df_target_test = train_test_split(df_data,df_target,train_size=0.70, random_state=1)


    df_train, df_test = train_test_split(df, test_size=split_size, random_state=random_state)

    df_train.to_csv(train_data_path,sep=",", index = False, encoding='utf-8')
    df_test.to_csv(test_data_path,sep=",",  index = False, encoding='utf-8')

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args = parser.parse_args()
    split_data(config_path=args.config)