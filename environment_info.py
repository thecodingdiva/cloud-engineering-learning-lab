environment = "dev"
aws_region = "us-east-1"
application = "learning-lab"

print(f'Environment: {environment}\nAWS Region: {aws_region}\nApplication: {application}')

if environment == "dev":
    print('Development environment detected')
elif environment == "test":
    print('Test environment detected')
else:
    print ('Production environment detected')
