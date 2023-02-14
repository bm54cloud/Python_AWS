# Create a script that will stop all running instances

import boto3

region = 'us-east-1' # Insert the region of the instances
ec2 = boto3.client('ec2', region_name=region)
instance_attr = ec2.describe_instances()

data = instance_attr["Reservations"]

instance_list = []

for instances in data:
    instance = instances["Instances"]
    for ids in instance:
        instance_id = ids["InstanceId"]
        instance_list.append(instance_id)
      
ec2.stop_instances(InstanceIds=instance_list)


    