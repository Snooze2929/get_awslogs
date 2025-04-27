aws cloudformation create-stack --stack-name Destination-LogGroup --template-url https://snooze-cf-bucket.s3.ap-northeast-1.amazonaws.com/projects/get-awslogs/DestinationLogGroup.yaml

aws cloudformation create-stack --stack-name Sender-LogGroup --template-url https://snooze-cf-bucket.s3.ap-northeast-1.amazonaws.com/projects/get-awslogs/SenderLogGroup.yaml

aws cloudformation create-stack --stack-name Lambda-Role --template-url https://snooze-cf-bucket.s3.ap-northeast-1.amazonaws.com/projects/get-awslogs/LambdaRole.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation create-stack --stack-name Lambda-Function --template-url https://snooze-cf-bucket.s3.ap-northeast-1.amazonaws.com/projects/get-awslogs/Lambda.yaml

