## デプロイ手順
ロググループ類(DestinatinlogGroup・SenderLogGroup)
↓
Lambdaに紐付けるロール
↓
Lambda関数
↓
サブスクリプションフィルター・EventBridgeルール

#### S3にテンプレートを配置する場合
aws cloudformation create-stack --stack-name 任意のスタック名 --template-url オブジェクトのURL --capabilities CAPABILITY_NAMED_IAM(IAMのRoleを作成する場合に必要)

