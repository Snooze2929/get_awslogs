
# 必要なライブラリのインポート
import boto3
import time

# CloudWatch Logsクライアントの定義
logs_client = boto3.client('logs')

# ログストリームを作成する
def create_log_stream(log_group_name, log_stream_name):
    response = logs_client.create_log_stream(
        logGroupName=log_group_name,
        logStreamName=log_stream_name
    )
    return response

# ログの送付
def send_logs_to_cloudwatch(log_group_name, log_stream_name, log_events):
    try:
        response = logs_client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=log_events
        )
        return response
    except Exception as e:
        print(f"Error sending logs: {e}")
        return None
