config = {
    "application": "learning-lab",
    "environment": "dev",
    "region": "us-east-1",
    "instance_count": 2
}

def summarize_config(config_file):
    for element in config_file:
        print(element + f' : {(config_file[element])}')

    if config_file["instance_count"] > 5:
        print('Warning: High instance count')

summarize_config(config)