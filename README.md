## デプロイ
上記をS3に配置してCloudFormation実行とLambda関数にコードを参照させています。
aws cloudformation create-stack --stack-name 任意のスタック名 --template-url オブジェクトのURL --capabilities CAPABILITY_NAMED_IAM(IAMのRoleを作成する場合に必要)

