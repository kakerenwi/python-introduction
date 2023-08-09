import boto3
ssm_client = boto3.client('ssm')

def get_ssm_parameter(parameter_name):
    response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    parameter_value = response['Parameter']['Value']
    print(parameter_value)

get_ssm_parameter("netflix-user-db")
get_ssm_parameter("netflix-movies-db")
get_ssm_parameter("/jjtech/dev/instancetype")
get_ssm_parameter("/jjtech/dev/amiid")