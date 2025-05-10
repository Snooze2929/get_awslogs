# 必要なライブラリのインポート
import gzip
import json
import base64
import io

# サブスクリプションフィルターだった場合、複合化する
def decompress_data(log_data):
    compressed_payload = base64.b64decode(log_data)
    with gzip.GzipFile(fileobj=io.BytesIO(compressed_payload), mode='rb') as f:
        return f.read().decode('utf-8')

# サブスクリプションフィルターかEventBridgeどちらか判定
def process_event(event):
    if 'awslogs' in event:
        log_data = event['awslogs']['data']
        decompressed_data = decompress_data(log_data)
        logs = json.loads(decompressed_data)
    else:
        logs = event
    return logs
