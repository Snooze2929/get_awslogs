
## 他ファイルに定義された関数をこのファイルでも使用できるようにする ##
# form ファイル名 import 関数名
from log_processing import process_event
from cloudwatch import create_log_stream, send_logs_to_cloudwatch

# メイン処理関数
def handler(event, context):

    # 送信先ロググループ定義
    log_group_name = 'destination-log-group'

    # 送信先ロググループへログストリームの定義
    log_stream_name = f"log-stream-{int(time.time())}"

    # トリガーで渡されたログデータの処理
    logs = process_event(event)

    # ログストリームに送信するログイベント
    log_events = [{'timestamp': int(time.time() * 1000), 'message': json.dumps(logs)}]

    # ログストリームを実際に作成する処理の実行
    create_log_stream(log_group_name, log_stream_name)

    # ロググループにログを送る処理
    response = send_logs_to_cloudwatch(log_group_name, log_stream_name, log_events)

    # 結果・内容の表示
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Logs processed successfully')
    }
