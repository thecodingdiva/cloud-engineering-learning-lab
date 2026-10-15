import config_check

valid = ["dev", "test", "prod"]

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
