config = {
    "application": "learning-lab",
    "environment": "dev",
    "region": "us-east-1",
    "instance_count": 2
}

def summarize_config(config_file):
    for element in config:
        print(element + f' : {(config_file[element])}')

summarize_config(config)