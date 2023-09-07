import os
import numpy as np
import pandas as pd
import argparse
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
from get_data import read_params
import joblib

def metrics(pred, actual):
    mse = mean_squared_error(actual,pred)
    mae = mean_absolute_error(actual,pred)
    r2=r2_score(actual,pred)
    rmse = np.sqrt(mse)
    return mse,mae,r2,rmse

def train_evaluate(config_path):
    config = read_params(config_path)

    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    target = config["base"]["target_col"]
    random_state=config["base"]["random_state"]
    model_dir=config["model_dir"]

    train = pd.read_csv(train_data_path, sep=",", encoding='utf-8')
    test = pd.read_csv(test_data_path, sep=",", encoding='utf-8')

    x_train = train.drop(target, axis=1)
    x_test = test.drop(target,axis=1)
    y_train = train[target]
    y_test = test[target]

    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)

    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    (mse,mae,r2,rmse) = metrics(y_pred,y_test)
    print("MSE is : ",mse)
    print("MAE is : ",mae)
    print("r2 score is : ", r2)
    print("rmse is : ",rmse)

    os.makedirs(model_dir, exist_ok=True)
    model_path=os.path.join(model_dir,"model.joblib")

    joblib.dump(model,model_path)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    args=parser.parse_args()
    train_evaluate(config_path=args.config)