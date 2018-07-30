import boto3

b_ec2 = boto3.client('ec2')
reservations = b_ec2.describe_instances()['Reservations']

targets = []
for res in reservations:
    instances = res['Instances']
    for ins in instances:
        tags = ins['Tags']
        for tag in tags:
            if tag['Key'] == 'AutoStop' and tag['Value'] == 'false':
                break
        else:
            targets.append(ins['InstanceId'])

print('# The list of instances to be stopped')
for ins_id in targets:
    print(ins_id)

b_ec2.stop_instances(InstanceIds=targets)
