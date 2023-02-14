import boto3

#define the connection
ec2 = boto3.resource('ec2')
 
def lambda_handler(event, context):
 
   # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
   filters = [
             {
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
 
    #filter the instances
    #ec2 = boto3.client('ec2', region_name=region)
   instances = ec2.instances.filter(Filters=filters)
 
    #locate all running instances
   RunningInstances = [instance.id for instance in instances]
 
    #print the instances for logging purposes
   print (RunningInstances) 
 
   