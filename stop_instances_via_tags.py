#!/usr/bin/env python3.7
# Create a script that will stop running instances

import boto3

tag = { "Key": "Environment", "Value": "Dev"}

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_instances()



    # for instance in instance_list:
       #  if (tag in instance['Tags'] and 'running' in instance['State']['Name']):
           #  print(instance['InstanceId'])
            # ec2.stop_instances(InstanceIds=[instance['InstanceId']])

# def lambda_handler(event, context):
# for instance in instance_list: 
    # print(instance)
        
        # if (tag in instance['Tags'] and 'running' in instance['State']['Name']):
            # ec2.stop_instances(InstanceIds=instance)
            # print("Stopped the following instances: \n" + instance['InstanceID']) 
            
            # print("Stopped the following instances: " + str(instances))


# if (dev_tag in instance['Tags'] and 'running' in instance['State']['Name']):
            # print(instance['InstanceId'])
            # ec2.stop_instances(InstanceIds=[instance['InstanceId']])