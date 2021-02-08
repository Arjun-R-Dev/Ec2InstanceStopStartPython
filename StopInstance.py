import boto3
region = 'specify the region here'
instances = ['instance id 1', 'instance id 2']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
