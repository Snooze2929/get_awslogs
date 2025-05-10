## デプロイ手順
ロググループ類(DestinatinlogGroup・SenderLogGroup)
↓
Lambda関数に紐づけるIAMロール(LambdaRole)
↓
lambdaのトリガー部分(20~36行目)をコメントアウトしてデプロイ
↓



#### S3にテンプレートを配置する場合
aws cloudformation create-stack --stack-name 任意のスタック名 --template-url オブジェクトのURL --capabilities CAPABILITY_NAMED_IAM(IAMのRoleを作成する場合に必要)

