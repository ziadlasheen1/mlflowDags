import dagshub
dagshub.init(repo_owner='mahmoudradwaan98', repo_name='dage_churn_test', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)