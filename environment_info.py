# environment = "dev"
# aws_region = "us-east-1"
# application = "learning-lab"

import config_check

valid = ["dev", "test", "prod"]

# if environment not in valid:
#     raise ValueError("Unsupported deployment environment")
# elif environment == "dev":
#     print('Development environment detected')
# elif environment == "test":
#     print('Test environment detected')
# else:
#     print ('Production environment detected')

# if environment in valid:
#     print(f'Environment: {environment}\nAWS Region: {aws_region}\nApplication: {application}')  
# else:
#     print(f'Environment: {environment} is invalid. Please choose from {valid}')

def validate_environment(env):
    if env not in valid:
        raise ValueError(f"Unsupported deployment environment: {env}")
    else:
        return env
    
def main():
    env = config_check.config["environment"]
    environment = validate_environment(env)
    print(f'Environment: {environment}\nAWS Region: {config_check.config["region"]}\nApplication: {config_check.config["application"]}')
    
if __name__ == "__main__":
    main()
