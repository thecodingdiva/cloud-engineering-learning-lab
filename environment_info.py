environment = "dev"
aws_region = "us-east-1"
application = "learning-lab"

valid = ["dev", "test", "prod"]

if environment not in valid:
    print('Error: Invalid environment specified')
elif environment == "dev":
    print('Development environment detected')
elif environment == "test":
    print('Test environment detected')
else:
    print ('Production environment detected')

if environment in valid:
    print(f'Environment: {environment}\nAWS Region: {aws_region}\nApplication: {application}')  
else:
    print(f'Environment: {environment} is invalid. Please choose from {valid}')
